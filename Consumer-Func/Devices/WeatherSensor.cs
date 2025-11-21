namespace Consumer.Devices;

public class WeatherTelemetry: AbstractTelemetry
{
    public double Temperature { get; set; }
    
    public  string Location { get; set; } = string.Empty;
    public DateTime CollectedOn { get; set; }
    public double Humidity { get; set; }
}