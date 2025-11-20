using iot_sim_func.Abstraction;
using Microsoft.Extensions.Options;

namespace iot_sim_func.Devices;

public class WeatherTelemetry
{
    public double Temperature { get; set; }
    
    public string Location { get; set; } = string.Empty;
    public DateTime CollectedOn { get; set; }
    public double Humidity { get; set; }
}
public class WeatherSensor(IOptionsMonitor<SimulatorConfig> config) : AbstractDevice<WeatherTelemetry>
{
    private IOptionsMonitor<SimulatorConfig> _simulatorConfig = config;

    public override string ConnectionString => config.CurrentValue.WeatherEndpoint;
    public override Task<WeatherTelemetry> GetTelemetry()
    {
        Random rnd = new();
        
        double latitude = Math.Round(-90 + rnd.NextDouble() * 180, 6);
        double longitude = Math.Round(-180 + rnd.NextDouble() * 360, 6);
        
        var telemetry = new WeatherTelemetry
        {
            Temperature = Math.Round(15 + rnd.NextDouble() * 10, 2),
            Humidity = Math.Round(40 + rnd.NextDouble() * 40, 2),
            Location = $"{latitude};{longitude}",
            CollectedOn = DateTime.UtcNow
        };
         
        Console.WriteLine(
            $"Sending Weather Telemetry: T={telemetry.Temperature}°C, H={telemetry.Humidity}%, Location={telemetry.Location}");
        return Task.FromResult(telemetry);
    }
}