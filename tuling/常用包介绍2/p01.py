import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

import os

mydir = os.getcwd()
print(mydir)

os.chdir('/Users/zy/PycharmProjects/')

mydir = os.getcwd()
print(mydir)

ld = os.listdir()
print(ld)

if 1 > 2:
	rst = os.makedirs('新建文件夹')

rst = os.system('ls')

rst = os.getenv('PATH')
print(rst)

print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)
print(os.name)

stm2


