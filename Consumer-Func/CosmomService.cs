using Consumer.Devices;
using Microsoft.Azure.Cosmos;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using System.Net;
using System.Text.Json;
using System.Threading.Tasks;

namespace Consumer;

public class CosmosService
{
    private readonly Container _container;

    private readonly ILogger _logger;

    public CosmosService(CosmosClient cosmosClient, ILogger<CosmosService> logger)
    {
        var databaseId = "DeviceTelemetry";
        var containerId = "DeviceTelemetry";
        _logger = logger;
        _container = cosmosClient.GetContainer(databaseId, containerId);
    }

    public async Task StoreTelemetryAsync(AbstractTelemetry telemetry)
    {
        var result = await _container.UpsertItemAsync(telemetry, new PartitionKey(telemetry.DeviceType));
        if (result.StatusCode != HttpStatusCode.OK &&
            result.StatusCode != HttpStatusCode.Created)
        {
            throw new CosmosException(
                $"Failed to upsert telemetry. Status: {result.StatusCode}",
                result.StatusCode,
                0,
                null,
                0
            );
        }
        _logger.LogInformation("Telemtry with DeviceId:{ID}, saved", telemetry.DeviceId);

    }
}
