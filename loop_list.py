count_num = [1,2,3,4,5]
fruits = ['banana','apple','mango','oranges']
change = [1,'cricketball',2,'football']

for number in count_num:
	print("this is count %d number" % number)

for fruit in fruits:
	print('A fruits of type; %s ' % fruit)
for i in change:
	print("i got %r" % i)
elements = []
for i in range(0,6):
		print('Adding %d to the list.' % i)
		elements.append(i)
#noe we can print them out too
for element in elements:
	print('Elements was: %d' % element)
