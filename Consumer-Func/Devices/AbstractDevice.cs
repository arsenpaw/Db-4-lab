using System.Text.Json.Serialization;
using iot_sim_func.Devices;

namespace Consumer.Devices;
[JsonPolymorphic(TypeDiscriminatorPropertyName = "deviceType")]
[JsonDerivedType(typeof(WeatherTelemetry), "weather")]
[JsonDerivedType(typeof(Co2Telemetry), "co2")]
public abstract class AbstractDevice
{
    public Guid DeviceId {get; } = Guid.NewGuid();
    public required string DeviceType { get; set; } 

}

