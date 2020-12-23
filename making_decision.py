print("You enter a dark room . Do you go through door 1 or 2 ")
door = input(": ")
if door == '1':
	print("There's a gaint bear here eating cheese cake. What do you do?")
	print("1: Take the Cake.")
	print("2: Scream at the bear")
	bear = input(": ")
	if bear == '1':
		print("The bear eats your face off.")
	elif bear == '2':
		print("The bear eats your legs off .")
	else:
		print('Wel, doing %s is probably better> Bear runs away. ' % bear)
elif door == '2':
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1: Blueberries.")
	print("2: Yellow jacket Clothespins")
	print("3: Understanding revolvers yelling melodies.")
	insanity = input(':')
	if insanity == '1' or insanity == '2':
		print("Your body survives powered by a mind of jello.")
	else:
		print("The insanity rots your eyes into a pool of muck.")
else:
	print("You stumble around and fall on a knife and die .")

