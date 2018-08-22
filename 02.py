class A():
	name='ffff'
	age=19
	__hobby =None #私有变量


	def func(self):
		self.name='张三'
		self.age=200
		print('my name is {0}'.format(self.name))

	def sayAgain(s):
		print(s.name)
	def sayHello():
		print(__class__.name)
		print("Hello")


a=A()

a.func()
a.sayAgain()
A.sayHello()

class Student():
	def __init__(self,name,age):##self指的是实例自身# #
		self._name=name
		self.age=age
	def Say(self):
		print(self._name)
		print(self.age)
s2=Student("xiao333ming",21)##这时必须带上值，否则会报错
s2.Say()





