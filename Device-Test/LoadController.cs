using System.Threading.Tasks;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;

namespace iot_sim_func;

public class LoadFunction(FakeLoad fakeLoad)
{
    private readonly FakeLoad _fakeLoad = fakeLoad;

    // [Function("FakeLoadTimer")]
    // public async Task RunTimerAsync(
    //     [TimerTrigger("%TimerSchedule%")] TimerInfo myTimer)
    // {
    //     await _fakeLoad.Run();
    // }

    [Function("FakeLoadHttp")]
    public async Task<HttpResponseData> RunHttpAsync(
        [HttpTrigger(AuthorizationLevel.Function, "post", Route = "fake-load")]
        HttpRequestData req,
        FunctionContext context)
    {
        await _fakeLoad.Run();

        var response = req.CreateResponse(System.Net.HttpStatusCode.OK);
        await response.WriteStringAsync("Fake load executed.");
        return response;
    }
}