using Consumer;
using Microsoft.Azure.Cosmos;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Builder;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = FunctionsApplication.CreateBuilder(args);

builder.ConfigureFunctionsWebApplication();

builder.Services
    .AddApplicationInsightsTelemetryWorkerService()
    .ConfigureFunctionsApplicationInsights();

builder.Services.AddSingleton(sp =>
{
    var connection = builder.Configuration["CosmosConnection"]
        ?? throw new InvalidOperationException("Missing CosmosConnection environment variable");

    return new CosmosClient(connection);
});
builder.Services.AddSingleton<CosmosService>();
builder.Build().Run();
