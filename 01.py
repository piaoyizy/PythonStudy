class Student():
	x = 5


class PythonStudent():
	name = None
	age = None

	def doSub(self):
		print('我在做作业')
		pass



yueyue= PythonStudent()
yueyue.doSub()
yueyue.name='123'
yueyue.age=19
print(yueyue.__dict__)



class Person:
	def fget(self):
		return	self._name * 2
	def fset(self,name):
		self._name=name.upper()

	def fdel(self):
		pass
	name = property(fget,fset,fdel,'123')