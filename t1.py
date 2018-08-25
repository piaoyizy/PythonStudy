class Person():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def sayHello(self):
        print('{0}说：你好，人类会说话'.format(self.name))


class MyClass:
    def fun1(self):
        print("fun1")


me: MyClass = MyClass()
me.fun1()
