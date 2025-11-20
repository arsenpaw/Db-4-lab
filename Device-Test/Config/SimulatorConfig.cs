namespace iot_sim_func;

public class SimulatorConfig
{
    public int RequestDelayMS { get; set; }
    public int MaxRequestCount { get; set; }

    public string Co2Endpoint { get; set; } = string.Empty;
    public string WeatherEndpoint { get; set; } = string.Empty;
}