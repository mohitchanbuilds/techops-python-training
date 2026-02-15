import psutil

# CPU usage
cpu = psutil.cpu_percent(interval=1)

# RAM usage
ram = psutil.virtual_memory().percent

# Disk usage
disk = psutil.disk_usage('/').percent

print("---- SYSTEM HEALTH REPORT ----")
print(f"CPU Usage   : {cpu}%")
print(f"RAM Usage   : {ram}%")
print(f"Disk Usage  : {disk}%")

# Alert system
if cpu > 80:
    print("⚠ WARNING: CPU is very high!")

if ram > 80:
    print("⚠ WARNING: RAM is very high!")

if disk > 90:
    print("⚠ WARNING: Disk almost full!")
