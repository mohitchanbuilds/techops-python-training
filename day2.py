room = "Conference Hall"
projector = "ON"
volume = int(input("Volume: "))

print(room)
print(projector)
print(volume)

if  volume >= 50:
    print("Volume is too high")
elif volume >= 35:
    print("Volume is  high")
elif volume <= 35 and volume >= 30:
    print("Volume is  low")
else:
    print("Volume is too low")
