using System;
using Microsoft.Extensions.Options;

namespace iot_sim_func.Devices;

public class Co2Telemetry
{
    public double Co2Level { get; set; }
    public DateTime CollectedOn { get; set; }
    
    public string Location { get; set; } = string.Empty;
    public string AirQualityCategory { get; set; } = default!;
}
