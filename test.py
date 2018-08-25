

# 给出提示信息
try:
    num = int(input("Plz input your number:"))
    rst = 100/num
    print("计算结果是： {0}".format(rst))
# 捕获异常后，把异常实例化，出息信息会在实例里
# 注意以下写法
# 以下语句是捕获ZeroDivisionError异常并实例化实例e
except ZeroDivisionError as e:
    print("你特娘的输入的啥玩意儿")
    print(e)
    # exit是退出程序的意思
    exit()