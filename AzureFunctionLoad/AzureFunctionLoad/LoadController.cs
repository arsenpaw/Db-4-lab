using AzureFunctionLoad.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;
using System.Net;
using System.Text;
using System.Text.Json;

public class LoadController
{
    private readonly ILogger<LoadController> _log;
    private readonly HttpClient _client;

    public LoadController(ILogger<LoadController> log, IHttpClientFactory factory)
    {
        _log = log;
        _client = factory.CreateClient();
        _client.BaseAddress = new Uri("https://lab2cloudrun.nicebeach-974168e5.polandcentral.azurecontainerapps.io/");
        _client.Timeout = Timeout.InfiniteTimeSpan;
    }

    private const string ROUTE = "gender";
    private static readonly JsonSerializerOptions _jsonOptions = new(JsonSerializerDefaults.Web);

    private async Task<List<GenderDto>> CreateBulkGender(int count, int batchSize, CancellationToken ct)
    {
        var result = new List<GenderDto>(count);
        int totalBatches = (int)Math.Ceiling(count / (double)batchSize);
        for (int batch = 0; batch < totalBatches; batch++)
        {
            var tasks = new List<Task<HttpResponseMessage>>(batchSize);
            int start = batch * batchSize;
            int end = Math.Min(start + batchSize, count);
            for (int i = start; i < end; i++)
            {
                var jsonBody = new { name = $"Gender_{i}" };
                var content = new StringContent(JsonSerializer.Serialize(jsonBody, _jsonOptions), Encoding.UTF8, "application/json");
                tasks.Add(_client.PostAsync(ROUTE, content, ct));
            }
            var responses = await Task.WhenAll(tasks);
            foreach (var response in responses)
            {
                if (!response.IsSuccessStatusCode) continue;
                await using var stream = await response.Content.ReadAsStreamAsync(ct);
                var dto = await JsonSerializer.DeserializeAsync<GenderDto>(stream, _jsonOptions, ct);
                if (dto != null) result.Add(dto);
            }
        }
        return result;
    }

    private async Task<List<GenderDto>> GetAllGendersAsync(CancellationToken ct)
    {
        using var response = await _client.GetAsync(ROUTE, ct);
        response.EnsureSuccessStatusCode();
        await using var stream = await response.Content.ReadAsStreamAsync(ct);
        var genders = await JsonSerializer.DeserializeAsync<List<GenderDto>>(stream, _jsonOptions, ct);
        return genders ?? new List<GenderDto>();
    }

    private Task DeleteGender(int id, CancellationToken ct) => _client.DeleteAsync($"{ROUTE}/{id}", ct);

    [Function("fireALgo")]
    public async Task<HttpResponseData> Run(
        [HttpTrigger(AuthorizationLevel.Anonymous, "post", Route = "fire/{id}/{batchSize}")] HttpRequestData req,
        int id, int batchSize, CancellationToken ct)
    {
        var result = await CreateBulkGender(id, batchSize, ct);
        var res = req.CreateResponse(HttpStatusCode.OK);
        await res.WriteAsJsonAsync(result, ct);
        return res;
    }

    [Function("getGenders")]
    public async Task<HttpResponseData> GetAll(
        [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = "genders")] HttpRequestData req,
        CancellationToken ct)
    {
        var items = await GetAllGendersAsync(ct);
        var res = req.CreateResponse(HttpStatusCode.OK);
        await res.WriteAsJsonAsync(items, ct);
        return res;
    }

    [Function("cleanGenders")]
    public async Task<HttpResponseData> Clean(
        [HttpTrigger(AuthorizationLevel.Anonymous, "delete", Route = "genders")] HttpRequestData req,
        CancellationToken ct)
    {
        var genders = await GetAllGendersAsync(ct);
        if (genders is null)
        {
            var res = req.CreateResponse(HttpStatusCode.OK);
            return res;
        }
        var tasks = genders.Select(g => DeleteGender(g.Id, ct));
        await Task.WhenAll(tasks);
        var response = req.CreateResponse(HttpStatusCode.OK);
        return response;
    }
}
