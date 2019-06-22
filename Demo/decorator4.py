def deco(func):
	def _deco(*args, **kwargs):
		print('before %s called.' % func.__name__)
		ret = func(*args, **kwargs)
		print('after %s called. result %s' %(func.__name__, ret))
	return _deco

@deco 
def myfunc(a,b):
	print('myfunc(%s, %s) called.' %(a,b))
	return a + b

myfunc(1,2)

@deco
def myfunc2(a,b,c):
	print('myfunc(%s, %s, %s) called' %(a, b, c))
	return a+b+c
myfunc2(1,2,3)

