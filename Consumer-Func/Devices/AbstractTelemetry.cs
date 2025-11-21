using System.Text.Json.Serialization;
using iot_sim_func.Devices;
using Newtonsoft.Json;

namespace Consumer.Devices;

[JsonPolymorphic(TypeDiscriminatorPropertyName = "DeviceType")] 
[JsonDerivedType(typeof(WeatherTelemetry), "Weather")]           
[JsonDerivedType(typeof(Co2Telemetry), "Co2")]
public class AbstractTelemetry
{
    public Guid DeviceId { get; set; }
    [JsonPropertyName("id")]
    [JsonProperty("id")]
    public Guid Id { get; set; } = Guid.NewGuid();

    public string DeviceType { get; set; } = string.Empty;

}

