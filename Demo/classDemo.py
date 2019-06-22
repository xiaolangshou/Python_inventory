class Person:
	def __init__(self, name, age, price):
		self.name = name
		self.age = age
		self.price = price
	def say(self):
		print('my name is %s :and age is %s' %(self.name, self.age))
	def raisePrice(self, percent):
		self.price = self.price * (1.1 + percent)
	def __str__(self):
		return 'Name: %s Price: %s' %(self.name, self.price)


lily = Person('thomas','29',1000)
lily.say()
lily.raisePrice(0.2)
print(lily)

