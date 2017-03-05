# Script Name	: example-7.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-05
# Description	: No.7 面向对象编程

# 7.1 类和对象
'''
    类: 具有某种特征的事物的集合(群体)。
    对象: 群体(类)里面的个体。
    类是抽象的,对象是具体的。

    定义类格式:
    class 类名:
        类里面的内容
'''
class cl1:
    pass

# 实例化
a = cl1()

# 构造函数(构造方法)
# self 在类中的方法必须加上self参数
# __init__(self, 参数)
class c1:
    def __init__(self):
        print("hello world!")

# 给构造方法加参数
class c2:
    def __init__(self, name, job):
        print("my name is " + name + " my job is " + job)

# 7.2 属性和方法
# 属性: 类里面的变量 self, 属性名
class c3:
    def __init__(self, name):
        self.myname = name

# 方法: 类里面的函数 def 方法名(self, 参数)
class c4:
    def show(self, name):
        print("hello " + name)

class c5:
    def __init__(self, name):
        self.myname = name
    def show(self, name):
        print("hello " + self.name)


# 继承(单继承、多继承)
# 父亲-父类(基类)
class father():
    def speak(self):
        print("i can speak")

# 单继承,子类继承父类
class son(father):
    pass

# 子类可以调用父类中得方法
s = son()
s.speak()

# 母亲-父类
class mother():
    def write(self):
        print("i can write")
# 多继承
class daughter(father, mother):
    def listen(self):
        print("i can listen")
# 重载
class son2(father):
    def speak(self):
        print("i can speak to")

d = daughter()
d.speak()
d.write()
d.listen()

s2 = son2()
s2.speak('sssss')

