using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
var host = new HostBuilder()
    .ConfigureFunctionsWorkerDefaults(worker =>
    {
        worker.UseMiddleware<ErrorHandlingMiddleware>();
    })
    .ConfigureServices(services =>
    {
       
        services.AddHttpClient();
    })
    .Build();

host.Run();