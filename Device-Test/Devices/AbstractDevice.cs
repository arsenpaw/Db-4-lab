namespace iot_sim_func.Abstraction;

public abstract class AbstractDevice<TTelemetry>
{
    public Guid DeviceId {get; } = Guid.NewGuid();
    public virtual string ConnectionString {get; private set;}
    public virtual Task<TTelemetry> GetTelemetry() => Task.FromResult(default(TTelemetry))!;
}

