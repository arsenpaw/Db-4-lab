using Consumer.Devices;
using Microsoft.Extensions.Options;
using System;

namespace iot_sim_func.Devices;

public class Co2Telemetry: AbstractTelemetry
{
    public double Co2Level { get; set; }
    public DateTime CollectedOn { get; set; }
    
    public string Location { get; set; }  = string.Empty;
    public  string AirQualityCategory { get; set; } = string.Empty;
}
