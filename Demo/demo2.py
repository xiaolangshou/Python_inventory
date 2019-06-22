import time

def producer(c):
	c.__next__()
	n = 0
	while n < 5:
		n = n + 1
		print('producer.. %s' %n)
		c.send(n)
		print('producer.. %s over' %n)
	c.close()

def customer():
	import time
	while 1:
		n = yield
		if not n:
			return 
		print('customer %s' %n)
		time.sleep(1)

x = customer()
producer(x)


