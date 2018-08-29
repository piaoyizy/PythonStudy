stm2 = lambda x, y: x * 10 + y * 20
print(stm2(100, 10))

stm2 = lambda x: x + 1
print(stm2(1))


# 利用map实现
def mulTen(n):
	return n * 10


l1 = [i for i in range(10)]
l3 = map(mulTen, l1)
l4 = list()
# map类型是一个可迭代的结构，所以可以使用for遍历
for i in l3:
	print(i)
	l4.append(i)  # ???1=f

print(l4)

# 以下列表生成式得到的结果为空， why？
l4 = [i for i in l3]
print(l4)

print(list(l4))

def isEven(a):
	return a % 2 == 0


l = [1, 2, 3, 4, 5, 6, 7, 33, 22]
rst = filter(isEven, l)
print(rst)
print(list(rst))

print('--' * 10)


def do(f):
	def wrapper(*args, **kwargs):
		print('先打印一句话')
		return f(*args, **kwargs)

	return wrapper


@do
def hello():
	print('hello')


hello()

import time


# 高阶函数，以函数作为参数
def printTime(f):
	def wrapper(*args, **kwargs):
		print("Time: ", time.ctime())
		return f(*args, **kwargs)

	return wrapper


# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数

def hello3():
	print("我是手动执行的")


# hello3()

hello3 = printTime(hello3)
hello3()

print('----------' * 5)
f = printTime(hello3)
print('----------' * 5)
f()
print(f.__doc__)
# 作业：
# 解释下面的执行结果


l1 = ['1', '23f', '432']
l2 = [89, 23, 78]
z = zip(l1, l2)

print(z)
print(type(z))

l3 = [i for i in z]
print(l3)

l3 = [i for i in z]
print(l3)
