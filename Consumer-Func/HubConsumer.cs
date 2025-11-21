using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using Consumer.Devices;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace MyIsolatedFunc;

public class HubListener
{
    private readonly ILogger _logger;

    public HubListener(ILoggerFactory loggerFactory)
        => _logger = loggerFactory.CreateLogger<HubListener>();

    [Function("HubListener")]
    public void Run(
        [EventHubTrigger(
            eventHubName: "my-event-hub",
            Connection = "HubConnection",
            ConsumerGroup = "%ConsumerGroup%")]  
        string[] messages)
    {
        var options = new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
            PropertyNameCaseInsensitive = true
        };
        foreach (var msg in messages)
        {
            var data = Encoding.UTF8.GetString(Encoding.UTF8.GetBytes(msg));
            var deviceData = JsonSerializer.Deserialize<IEnumerable<AbstractDevice>>(data, options);
            if (deviceData is null)
            {
                _logger.LogError($"Data {msg} was damaged");
            }
            _logger.LogInformation("📥 Event received: {data}", deviceData);
        }
     



    }
}