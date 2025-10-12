using AzureFunctionLoad.Models;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Text.Json;

public class LoadController
{

    private readonly ILogger<LoadController> _log;
    private readonly HttpClient _client;

    public LoadController(ILogger<LoadController> log, IHttpClientFactory factory)
    {
        _log = log;
        _client  = factory.CreateClient();
        _client.BaseAddress = new Uri("https://lab2cloudrun.nicebeach-974168e5.polandcentral.azurecontainerapps.io/");
        _client.Timeout = Timeout.InfiniteTimeSpan;
    }


    private const string ROUTE = "gender";
    private static readonly JsonSerializerOptions _jsonOptions =
    new(JsonSerializerDefaults.Web);

    private async Task<List<GenderDto>> CreateBulkGender(int count, int batchSize = 10)
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
                var jsonBody = new
                {
                    name = $"Gender_{i}"
                };

                var content = new StringContent(
                    JsonSerializer.Serialize(jsonBody, _jsonOptions),
                    Encoding.UTF8,
                    "application/json"
                );

                tasks.Add(_client.PostAsync(ROUTE, content));
            }

            _log.LogInformation("🔹 Batch {Batch}/{Total} [{Start}-{End}) started...", batch + 1, totalBatches, start, end);
            var sw = System.Diagnostics.Stopwatch.StartNew();

            var responses =  await Task.WhenAll(tasks);
            foreach (var response in responses)
            {
                if (!response.IsSuccessStatusCode)
                {
                    _log.LogWarning("Request failed with {Code}", response.StatusCode);
                    continue;
                }

                await using var stream = await response.Content.ReadAsStreamAsync();
                var dto = await JsonSerializer.DeserializeAsync<GenderDto>(stream, _jsonOptions);

                if (dto != null)
                    result.Add(dto);
            }

            sw.Stop();
            _log.LogInformation("✅ Batch {Batch}/{Total} completed in {Ms} ms", batch + 1, totalBatches, sw.ElapsedMilliseconds);
        }

        _log.LogInformation("🎯 All {Count} requests completed successfully.", count);
        return result;
    }


    private async Task<List<GenderDto>> GetAllGendersAsync()
    {
        using var response = await _client.GetAsync(ROUTE);
        response.EnsureSuccessStatusCode();

        await using var stream = await response.Content.ReadAsStreamAsync();
        var genders = await JsonSerializer.DeserializeAsync<List<GenderDto>>(stream, _jsonOptions);

        return genders ?? new List<GenderDto>();
    }
    private Task DeleteGender(int id)
    {
        return _client.DeleteAsync($"{ROUTE}/{id}");
    }

    [Function("fireALgo")]
    public  async Task<HttpResponseData> Run(
        [HttpTrigger(AuthorizationLevel.Anonymous, "post", Route = "fire/{id}/{batchSize}")] HttpRequestData req,
        int id, int batchSize)
    {
        _log.LogInformation($"Fire endpoint called with id: {id}");
        var result = await CreateBulkGender(id, batchSize);
        var res = req.CreateResponse(HttpStatusCode.OK);
        await res.WriteAsJsonAsync(result);
        return res;
    }
    [Function("getGenders")]
    public async Task<HttpResponseData> GetAll(
    [HttpTrigger(AuthorizationLevel.Anonymous, "get", Route = "genders")] HttpRequestData req)
    {
        var items = await GetAllGendersAsync();
        var res = req.CreateResponse(HttpStatusCode.OK);
        await res.WriteAsJsonAsync(items);
        return res;
    }
    [Function("cleanGenders")]
    public async  Task<HttpResponseData> Clean([HttpTrigger(AuthorizationLevel.Anonymous,  "delete", Route = "genders")] HttpRequestData req)
    {
        var genders = await GetAllGendersAsync();
        if (genders is null)
        {
            var res = req.CreateResponse(HttpStatusCode.OK);
            return res;
        }
        var tasks = genders.Select(g => DeleteGender(g.Id));
        await Task.WhenAll(tasks);
        var response = req.CreateResponse(HttpStatusCode.OK);
        return response;

    }
}
