import psutil

# Number of CPU
print(f"Logical CPU avilable now", psutil.cpu_count(logical=True))

# CPU usage percentage
print(f"CPU utilization", psutil.cpu_percent(interval=1))

# CPU times
print(f"CPU utilization time is", psutil.cpu_times())

# Virtual memory of an system
virtual_memo = psutil.virtual_memory()

print(f"\n Total memory: {virtual_memo.total // (1024 ** 3)} GB")
print(f"\n Availbale memory: {virtual_memo.available // (1024 ** 3)} GB")
print(f"\n Memory usage {virtual_memo.percent}")

# swap memory

swap_mem = psutil.swap_memory()

print(f"\n Total swap memory : {swap_mem.total // (1024 ** 3)} GB")
print(f"\n Total used swap memory : {swap_mem.used // (1024 ** 3)} GB")

# Disk partition

partitions = psutil.disk_partitions()
for partion in partitions:
    print(f"\n Device : {partion.device}")
    print(f"\n Mount Point :{partion.mountpoint}")
    print(f"\n File System: {partion.fstype}")
    
# Disk uage 
disk_use = psutil.disk_usage('/')

print(f"Total disk uage: {disk_use.total // (1024 ** 3)} GB")    
print(f"Used Disk Space: {disk_use.used // (1024**3)} GB")
print(f"Free Disk Space: {disk_use.free // (1024**3)} GB")
print(f"Disk Usage (%): {disk_use.percent}")

# Running process 
for process in psutil.process_iter(['pid', 'name', 'username']):
    print(process.info)