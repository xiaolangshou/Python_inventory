import time

def deco1(func):
	def _deco():
		print('begin time...')
		func()
		print('end time...')
	return _deco

def deco2(func):
	def _deco():
		print('2 begin time...')
		func()
		print('2 end time...')
	return _deco

@deco1
@deco2
def func():
	print('begin...')
	time.sleep(1)
	print('end...')

func()
