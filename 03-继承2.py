import os
os.system("01.py")

class Fish():
	def __init__(self,name):
		self.name=name
	def swim(self):
		print('i am swimming.....')
class Bird:
	def __init__(self,name):
		self.name=name
	def fly(self):
		print('I am flying....')
class Person:
	def __init__(self,name):
		self.name=name
	def work(self):
		print('I an working')

class SuperMan(Person,Bird,Fish):
	def __init__(self,name):
		self.name=name
	pass


s=SuperMan('fff')
s.fly()
s.swim()
s.work()

#多继承用的很少，  c#中有接口实现

sum=0
for x in range(1,4):
	sum+=x
print(sum)


