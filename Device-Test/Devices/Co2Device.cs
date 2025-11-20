using System;
using iot_sim_func.Abstraction;
using Microsoft.Extensions.Options;

namespace iot_sim_func.Devices;

public class Co2Telemetry
{
    public double Co2Level { get; set; }
    public DateTime CollectedOn { get; set; }
    
    public string Location { get; set; } = string.Empty;
    public string AirQualityCategory { get; set; } = default!;
}

public class Co2Device(IOptionsMonitor<SimulatorConfig> config) : AbstractDevice<Co2Telemetry>
{
    public override string ConnectionString =>  config.CurrentValue.Co2Endpoint;
    
    public override Task<Co2Telemetry> GetTelemetry()
    { 
        Random rnd = new();
        var co2 = Math.Round(400 + rnd.NextDouble() * 1600, 2);

        var category = co2 switch
        {
            <= 800 => "Good",
            <= 1200 => "Moderate",
            <= 2000 => "Poor",
            _ => "Very Poor"
        };

        double latitude = Math.Round(-90 + rnd.NextDouble() * 180, 6);
        double longitude = Math.Round(-180 + rnd.NextDouble() * 360, 6);

        var telemetry = new Co2Telemetry
        {
            Co2Level = co2,
            CollectedOn = DateTime.UtcNow,
            Location = $"{latitude};{longitude}",
            AirQualityCategory = category
        };

        Console.WriteLine(
            $"CO2={telemetry.Co2Level}ppm, Category={telemetry.AirQualityCategory}, Location={telemetry.Location}, Time={telemetry.CollectedOn:O}");

        return Task.FromResult(telemetry);
    }
}