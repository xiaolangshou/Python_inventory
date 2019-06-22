class Person:
	def __init__(self, name, age, price):
		self.name = name
		self.age = age
		self.price = price

	def say(self):
		print('my name is %s and age is %s' %(self.name, self.age))
	
	def raisePrice(self, percent):
		self.price = self.price * (1.1 + percent)
	
	def __str__(self):
		return 'Name: %s Price: %s' %(self.name, self.price)

lily = Person('lily', '20', 1000)
lily.raisePrice(0.2)
print(lily)

class Manager(Person):
	def raisePrice(self, percent, other=0.1):
		Person.raisePrice(self, percent + other)

tom = Manager('thomas',21,1000)
tom.raisePrice(0.2)
print(tom)
 
class A(object):
	def __init__(self, name):
		self.name = name
		print('name:', self.name)
	def getName(self):
		return 'A ' + self.name

class B(A):
	def getName(self):
		return 'B ' + self.name


b = B('hello')
print(b.getName())


class c1(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return 'c1 my name is %s my age is %s' %(self.name, self.age)

class c2(c1):
	def __init__(self, name, age, job):
		self.name = name
		self.age = age
		self.job = job
	def __str__(self):
		return 'c2 my name is %s my age is %s job is %s' %(self.name, self.age, self.job)
	
x = c2('lily','20','hr')
print(x)
