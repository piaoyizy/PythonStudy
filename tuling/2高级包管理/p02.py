# import  p01
# stu=p01.Student('张三',19)
# stu.say()
#
#
# p01.SayHello()


import importlib

stu=importlib.import_module('p01')
stu1 =stu.Student()
stu1.say()