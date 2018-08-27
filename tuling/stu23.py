stm2 = lambda x, y:   x * 10 + y * 20
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
	l4.append(i)

print(l4)

# 以下列表生成式得到的结果为空， why？
l4 = [i for i in l3]
print(l4)

print(list(l4))

def isEven(a):
	return  a % 2 ==0
l=[1,2,3,4,5,6,7,33,22]
rst=filter(isEven,l)
print(rst)
print(list(rst))

print('--'*10)




def do(f):
	def wrapper(*args,**kwargs):
		print('先打印一句话')
		return f(*args,**kwargs)
	return  wrapper

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




l1 =['1','23f','432']
l2=[89,23,78]
z=zip(l1,l2)

print(z)
print(type(z))

l3=[i for i in z ]
print(l3)


l3=[i for i in z ]
print(l3)

s='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\
=mHY9'
print(s)


ss='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mHY9'
print(len(ss))
print(len(s))