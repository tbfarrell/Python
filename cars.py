print("Let's list some car brands. We got: \n")

cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car.lower() == 'bmw':
		print(car.upper())
	else:
		print(car.title())