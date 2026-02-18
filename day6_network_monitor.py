import psutil
import socket
from datetime import datetime
import speedtest

# Get current date and time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Check internet connection
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False

# Get active network name (Wi-Fi / Ethernet)
def get_network_name():
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                return iface
    return "No Network"

# Run speed test
def get_speed():
    st = speedtest.Speedtest()
    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    return round(download, 2), round(upload, 2)

# Main
connected = is_connected()
network = get_network_name()

if connected:
    download, upload = get_speed()
    status = f"Connected to {network}\nDownload: {download} Mbps\nUpload: {upload} Mbps"
else:
    status = "No Internet Connection"

log = f"\n[{now}]\n{status}\n--------------------"

# Save to file
with open("network_log.txt", "a") as file:
    file.write(log)

print(log)
