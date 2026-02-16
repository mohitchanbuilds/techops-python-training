import socket

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except:
        return False

if check_internet():
    print("Internet: Connected")
else:
    print("Internet: NOT Connected")




import os

target = "8.8.8.8"   # Ye Google ka server hai

print("\nChecking device:", target)

result = os.system("ping -n 2 " + target)

if result == 0:
    print("Device is ONLINE")
else:
    print("Device is OFFLINE")
