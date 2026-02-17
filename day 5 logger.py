import psutil
from datetime import datetime

# Get system data
cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Time
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

log = f"{time} | CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%\n"

# Write to file
with open("system_log.txt", "a") as file:
    file.write(log)

print("Log saved:", log)






import psutil

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent

if cpu > 80:
    print("⚠️ CPU Overload")

if ram > 80:
    print("⚠️ RAM Overload")

if cpu < 80 and ram < 80:
    print("System Healthy")
