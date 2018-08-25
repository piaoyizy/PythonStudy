# class Student():
# 	x = 5
#
#
# class PythonStudent():
# 	name = None
# 	age = None
#
# 	def doSub(self):
# 		print('我在做作业')
# 		pass
# #fdsfds
#
#
# yueyue= PythonStudent()
# yueyue.doSub()
# yueyue.name='123'
# yueyue.age=19
# print(yueyue.__dict__)
#
#
#
# class Person:
# 	def fget(self):
# 		return	self._name * 2
# 	def fset(self,name):
# 		self._name=name.upper()

#
# 	def fdel(self):
# 		pass
# 	name = property(fget,fset,fdel,'123')


# 给出提示信息
try:
    num = int(input("Plz input your number:"))
    rst = 100 / num
    print("计算结果是： {0}".format(rst))
# 捕获异常后，把异常实例化，出息信息会在实例里
# 注意以下写法
# 以下语句是捕获ZeroDivisionError异常并实例化实例e
except ValueError as e:
    print("你特娘的输入的啥玩意儿")
    print(e)
    # exit是退出程序的意思
    exit()
