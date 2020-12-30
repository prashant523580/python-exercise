ten_things = "Apple Balls Orange Crows Telephone Light"

stuff = ten_things.split(' ')
print(stuff)
print("there's not 10 things in that list , let fix that ")

more_stuff = ["Day","night","summer","winter","year","month"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print("adding ", next_one)
	stuff.append(next_one)
print(stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)

print(" ".join(stuff))

print(" ".join(stuff[3:5]))
