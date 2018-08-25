# class Counter:
# 	@staticmethod
# 	def sleep():
# 		print()
# 	@classmethod
# 	def play(cls):
# 		pass
#
# 	def __setattr__(self, name, value):
# 		self.counter += 1
# #既然需要 __setattr__ 调用后才能真正设置 self.counter 的值，所以这时候 self.counter 还没有定义，所以没法 += 1，错误的根源。”””
# 		super().__setattr__(name, value)
# 	def __delattr__(self, name):
# 		self.counter -= 1
# 		super().__delattr__(name)
#


# import calendar
#
# cal = calendar.isleap(2020)
# print(cal)
# cal = calendar.leapdays(2018, 2050)
# print(cal)
# cal = calendar.monthrange(2018, 2)
# print(cal)
# cal = calendar.month(2018, 5)
# print(cal)
# cal = calendar.monthcalendar(2018, 3)
#
# cal = calendar.weekday(2018, 8, 25)
# print(cal)

# time 模块
import time
from datetime import datetime, timedelta

# t = time.time() # 时间辍 1970-1-1 00:00：00
t = time.localtime()
d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(d)
print(t)

t = time.localtime()
ft = time.strftime("%Y-%m-%d %H:%M", t)
print(ft)

dt = datetime.today()
print(dt)
print('*' * 20)
# datetime.timedelta
t1 = datetime.now()
print(type(t1))
print(t1.strftime("%Y-%m-%d %H:%M:%S"))

# datetime 加 1小时
td = timedelta(days=1, hours=2)

print((t1 - td).strftime("%Y-%m-%d %H:%M:%S"))


t2=datetime(2015,1,1)
print(not (t1 - t2).days3)
