
#messing with psutil here
import psutil
psutil.cpu_times()
print("This is it:", psutil.cpu_times())
print("This is cpu percent:", psutil.cpu_percent(interval=10, percpu=True))
print("This is cpu count:", psutil.cpu_count(logical=True))
print("This is virtual memory:", psutil.virtual_memory())
print("This is disk usage:", psutil.disk_usage('/'))
print("This is memory info:", psutil.Process().memory_info())