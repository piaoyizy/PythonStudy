# import  p01
# stu=p01.Student('张三',19)
# stu.say()
#
#
# p01.SayHello()

from importlib import  import_module
import importlib as importAs


stu=importAs.import_module('p01')
stu1 =stu.Student()
stu1.say()



