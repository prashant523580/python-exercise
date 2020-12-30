#create a mapping of state to abbreviation
states = {
	'Bheri' : 'Bh',
	'Karnali': 'Ka',
	'Bagmati': 'Ba',
	'Sutkhet' : 'Skt'
}

#create a basic set of states and some cities in them
cities = {
	'Bh' : "kohalpur",
	'Ka' : 'Lamki',
	'Ba' : 'New road'
}

#add more cities 

cities['Skt'] = 'Birendranagar'

#print out some cities

print("-"*30)
print('Bh state has :', cities['Bh'])
print("Ka state has :", cities['Ka'])

#print some sstate
print('-' * 30)
print("Bheri  abbreviation is ", states['Bheri'])
print("Karnali abbreviation is ", states["Karnali"])


#do it by using  the statw then cities  dict

print("-"*30)
print("Karnali has : ", cities[states['Karnali']])
print('Bheri has : ', cities[states["Bheri"]])

#print every state abbreviation 
print("-" * 30)
for state , abbreviation in states.items():
	print(f"{state} state is abbreviated  {abbreviation}") # string format method
#	print("%s state is abbreviated %s" % (state, abbreviation))

#print every city in states

print("-"*30)
for abbre,  city in cities.items():
	print("%s has the city %s" % (abbre,city))

#both at the same time

print("-"*30)
for  state, abbre in states.items():
	#print('%s state is abbreviated %s and has city %s ' % (state, abbre,cities[abbre]))
	print(f"{state} state is abbreviated {abbre} and has  city {cities[abbre]}")
