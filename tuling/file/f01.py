##一次写入多行
from time import sleep

f = open(r'text1.txt', 'w')

for i in range(1, 5):
	f.writelines('{0}+123\n'.format(i))
f.close()

##读取文件内容
with open(r'text.txt', 'r') as f:
	strline = f.readline(100)  # 入参：N行
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
# seek
with open(r'text.txt', 'r') as f:
	strChar = f.read(3)
	pos=f.tell()
	while strChar:
		print('---'+strChar.strip()+'---')
		print(f.tell())
		sleep(0.1)
		strChar = f.read(3)
		pos = f.tell()
