from typing import overload

server = "JP_Server_01"
cpu = 75
ram = 70

print("server:", server)
print("cpu:", cpu)
print("ram:", ram)

if cpu > 80:
    print("Server overload")
else:
    print("server healthy")