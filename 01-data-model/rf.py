#test return function
def add(a,b):
	return a+b
def home():
	return "Hello Boss!"
def trf(a,b):
	if a>b:
		return add(a,b)
	else:
		#you must konw  home() is a return value then
	    return home()#it will produce "hello boss"