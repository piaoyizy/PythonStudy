class Person():
	name = None
	__age = 18
	gender = None
	def sleep(self):
		print('sleeping')


class Teacher(Person):
	def make_test(self):
		print('老师会考试')

print(Person.__dict__)
wang=Person()
wang.name='王老师'


liu=Teacher()
liu.name='Ff'


liu.sleep()
liu.make_test()


# 所有类都是object的基类 同 Java c#


print(type(super))

print(super.__dict__)


class Animel():
	def __init__(self):
		print("我是动物")
class Dog(Animel):
	def __init__(self):
		print("我是狗")

a=Dog()


