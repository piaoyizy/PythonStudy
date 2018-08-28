##一次写入多行
from time import sleep

f = open(r'text1.txt', 'w')

for i in range(1, 5):
	f.writelines('{0}+123\n'.format(i))
f.close()

##读取文件内容
with open(r'text.txt', 'r') as f:
	strline = f.readline(1)  # 入参：N行
	while strline:
		print(strline)
		strline = f.readline()

with open(r'text1.txt', 'r') as f:
	l = list(f)
	for line in l:
		print(line)
	strchar = f.read()
	print(strchar)

print('--' * 10)
# 每次读取三个字符
with open(r'text.txt') as f:
	strChar = f.read(30)  # 30个字符
	pos = f.tell()
	while strChar:
		print('---' + strChar.strip() + '---')
		print(f.tell())
		sleep(0.1)
		strChar = f.read(30)
		pos = f.tell()

# 序列化 经常用到，重要
import pickle

age = 19
with open(r'test03xu.txt', 'wb')as f:
	pickle.dump(age, f)
with open(r'test03xu.txt', 'rb')as f:
	print('反实例化:{0}'.format(pickle.load(f)))

a = [19, 'zhangyao', 'i love zhangyucheng', [185, 86]]
with open(r'test03xu.txt', 'wb')as f:
	pickle.dump(a,f)
with open(r'test03xu.txt', 'rb')as f:
	print('反实例化:{0}'.format(pickle.load(f)))



