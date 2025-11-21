using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using Consumer;
using Consumer.Devices;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

namespace MyIsolatedFunc;

public class HubListener(ILogger<HubListener> _logger, CosmosService cosmosService)
{


    [Function("HubListener")]
    public async Task Run(
        [EventHubTrigger(
            eventHubName: "my-event-hub",
            Connection = "HubConnection",
            ConsumerGroup = "%ConsumerGroup%")]  
        string[] messages)
    {
        foreach (var msg in messages)
        {
            try
            {
                var deviceData = TelemetryParser.Deserialize(msg);
                _logger.LogInformation("Event received: {data}", JsonSerializer.Serialize(deviceData));
                await cosmosService.StoreTelemetryAsync(deviceData!);
            }
            catch (NotSupportedException ex)
            {
                _logger.LogError(ex, ex.Message);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"Error happen in msg:{JsonSerializer.Serialize(msg)}");
            }
        }
        
    }
}