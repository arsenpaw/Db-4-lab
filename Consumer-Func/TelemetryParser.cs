using Consumer.Devices;
using iot_sim_func.Devices;
using System.Text.Json;

public static class TelemetryParser
{
    public static AbstractTelemetry? Deserialize(string json)
    {
        using var doc = JsonDocument.Parse(json);

        if (!doc.RootElement.TryGetProperty("DeviceType", out var typeProp))
            throw new NotSupportedException("Telemetry didn't contain required field 'DeviceType'.");

        var type = typeProp.GetString();

        return type switch
        {
            "Weather" => JsonSerializer.Deserialize<WeatherTelemetry>(json),
            "Co2" => JsonSerializer.Deserialize<Co2Telemetry>(json),
            _ => throw new NotSupportedException($"Unknown telemetry type: {type}")
        };
    }
}
