import time

def deco1(func):
	def _deco():
		beg = time.time()
		print('begin time is %s' %beg)
		func()
		end = time.time()
		print('end time is %s' %end)
		print('total time is %s' %(end - beg))
	return _deco

def deco2(func):
	def _deco():
		print('deco2 start...')
		func()
		print('deco2 end...')
	return _deco

@deco1
@deco2
def func():
	print('begin...')
	time.sleep(1)
	print('end...')

func()

