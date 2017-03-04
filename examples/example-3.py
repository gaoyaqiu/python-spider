# Script Name	: example-3.py
# Author		: gaoyaqiu(球哥)
# Created		: 2017-03-04
# Description	: No.3 python函数详解

# 3.1 局部变量与全局变量
# 变量是有生效范围的, 也叫作用域
# 全局变量: 作用域从变量出现的地方开始,到这个变量作用范围结束的地方结束
# 局部变量: 作用域只在局部的变量

# 作用域
# i是全局变量
'''
i = 1000
def func():
    # j是局部变量
    j = 100
    print(j)
print(i)
func()
'''
# 执行下面代码会报错,因为j是局部变量,不是全局变量
#print(j)

# 3.2 认识python函数
# 函数的本质就是功能的封装。使用函数可以大大提高编程的效率与程序的可读性
'''
函数定义的格式:
def 函数名(参数):
    函数体
'''
def abc():
    print("abc")
# 调用函数: 函数名(参数)
#abc()

# 参数: 分为形参和实参
# 一般在函数定义的时候使用的参数是形参
# 一般在函数调用的时候使用的参数是实参
def func2(a, b):
    if(a > b):
        print("a 大于 b")
    elif( a == b):
        print("a 等于 b")
    else:
        print("a 小于 b")
# a=1, b=10
func2(1, 10)