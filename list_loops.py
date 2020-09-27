songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print("\n")
print(songs[2])
print("\n")
print(songs[0:2])
print("\n")

songs[2] = "All Star"
print(songs)
print("\n")

songs.extend(["Addict", "Shy", "Devils Don't Fly"])
print(songs)
print("\n")

del songs[1]
print(songs)
print("\n")

animals = ["Wolf", "Cat", "Fox"]
print(animals)
print("\n")

animals.append("Turtle")
print(animals)
print("\n")

print(animals[2])
print("\n")

del animals[0]
print(animals)
print("\n")

for i in range(len(animals)):
    print(animals[i])