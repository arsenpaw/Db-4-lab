using iot_sim_func;
using iot_sim_func.Devices;
using Microsoft.Azure.Devices.Client;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);
builder.ConfigureFunctionsWebApplication();

builder.Services
    .AddApplicationInsightsTelemetryWorkerService()
    .ConfigureFunctionsApplicationInsights();
builder.Services
    .AddOptions<SimulatorConfig>()
    .Bind(builder.Configuration.GetSection("Config"));

builder.Services.AddSingleton<WeatherSensor>();
builder.Services.AddSingleton<Co2Device>();
builder.Services.AddSingleton<FakeLoad>();
builder.Build().Run();
