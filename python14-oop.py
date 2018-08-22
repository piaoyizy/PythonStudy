# 操作类 函数：
# __new__ 函数   一般不用

# __call__:对象当函数使用的时候  来触发
class A():
	def __init__(self,name='123'):
		print("123321")
	def __call__(self, *args, **kwargs):
		print('call')
a=A()
a()

# __str__ :当对象被当做字符串的时候使用
print('*'*20)
class A():
	def __init__(self,name='123'):
		print("123321")
	def __call__(self, *args, **kwargs):
		print('call')
	def __str__(self):
		return '1233421321'
a=A()
a()
print(a)

##__repr__   当对象被当做字符串的时候使用  同 str


# __getattr__ ：找不到属性的时候提示

# print('*'*20)
# class B():
# 	name=''
# 	age=19
# 	def __getattr__(self, item):
# 		print('meiyou')
# 		print(item)
# b=B()
# print(b.addr)

#__setattr__ :对成员属性设置的时候使用

# print('*'*20)
#
# class Person():
# 	def __init__(self):
# 		pass
# 	def __setattr__(self, key, value):
# 		print('设置属性:{0}'.format(key))
# 		#self.name=value
# 		super().__setattr__(key,value)
# p=Person()
# print(p.__dict__)
# p.age=19



# __setattr__ :
#
# class JsonDict(dict):
# 	def __getattr__(self, attr):
#
# 			return self[attr]
#
#
# 	# 可以重写dict，使之通过“.”调用
# 	def __setattr__(self, attr, value):
# 		self[attr] = value
#
#
# j = JsonDict(name='python', age='28')
# print(j.name)
# print(j.age)


class Counter:
	@staticmethod
	def sleep():
		print()
	@classmethod
	def play(cls):
		pass

	def __setattr__(self, name, value):
		self.counter += 1
#既然需要 __setattr__ 调用后才能真正设置 self.counter 的值，所以这时候 self.counter 还没有定义，所以没法 += 1，错误的根源。”””
		super().__setattr__(name, value)
	def __delattr__(self, name):
		self.counter -= 1
		super().__delattr__(name)

