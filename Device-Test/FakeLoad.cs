using System.Text;
using iot_sim_func.Devices;
using Microsoft.Azure.Devices.Client;
using Microsoft.Extensions.Options;
using Newtonsoft.Json;

namespace iot_sim_func;

public class FakeLoad(WeatherSensor weatherDevice,Co2Device co2Device, IOptionsMonitor<SimulatorConfig> options)
{

    public async Task Run()
    {

        var weatherDeviceClient = DeviceClient.CreateFromConnectionString(
            weatherDevice.ConnectionString,
            TransportType.Mqtt
        );
        var co2DeviceClient = DeviceClient.CreateFromConnectionString(
            co2Device.ConnectionString,
            TransportType.Mqtt
        );

        var totalRequest = 0;

        while (totalRequest <= options.CurrentValue.MaxRequestCount)
        {
            var weatherTelemetry = await weatherDevice.GetTelemetry();
            var co2Telemetry = await co2Device.GetTelemetry();
            
            var weatherJson = JsonConvert.SerializeObject(weatherTelemetry);
            var co2Json = JsonConvert.SerializeObject(co2Telemetry);
            
            using var weatherMessage = new Message(Encoding.UTF8.GetBytes(weatherJson))
            {
                ContentType = "application/json",
                ContentEncoding = "utf-8"
            };

            using var co2Message = new Message(Encoding.UTF8.GetBytes(co2Json))
            {
                ContentType = "application/json",
                ContentEncoding = "utf-8"
            };
            
            await weatherDeviceClient.SendEventAsync(weatherMessage);
            await co2DeviceClient.SendEventAsync(co2Message);

            totalRequest+=2;
            
            await Task.Delay(TimeSpan.FromMilliseconds(options.CurrentValue.RequestDelayMS));
        }

        await weatherDeviceClient.CloseAsync();
        await co2DeviceClient.CloseAsync();
    }
}