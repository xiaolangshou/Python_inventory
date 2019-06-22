def deco(func):
	def _deco(a,b):
		print('before my func() called')
		ret = func(a,b)
		print('after my func() called')
		return ret
	return _deco

@deco
def myFunc(a,b):
	print('my func %s, %s called' %(a,b))
	return a+b
myFunc(1,2)
myFunc(3,4)
