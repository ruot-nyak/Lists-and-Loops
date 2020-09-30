songs = ["ROCKSTAR", "Do It", "For The Night"]
#I know that the index starts at one and that "ROCKSTAR" is 0 and "For The Night"
#  is 2 but when I ran it wasn't giving me what I wanted
print(songs[0:3])

print(songs[1:3])

songs[0] = "Dynamite"

print(songs)

songs.append("Something Special")
songs.append("To The Top")
songs.append("Already")

songs.remove("Do It")

print(songs)


animals = ['snakes','dogs','cats',]

animals.append('fish')
print(animals[0])

animals.remove('snakes')

for i in range(len(animals)):
    print(animals[i])
