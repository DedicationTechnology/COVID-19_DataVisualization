"""方法和函数的区别"""
# # 方法需要跟在对象的后面，而函数不需要
# str = "this is a string"
# res = str.split()
# print(str)  # 字符串是一个不可变类型，不可以修改其中的值
# print(res)
# """这里split()是一个方法，要使用这个方法就需要跟在对象的后面(这里的对象是str),
# 这里的print()是一个函数，不需要跟在对象的后面就可以直接使用"""

"""面向对象"""

"""简单理解：人是一个大类，张飞一个对象，张飞拥有人这个类的相关属性和方法"""
# class Human:  # 定义类，类名的第一个字母一般要大写
#     def __init__(self, a, b):
#         self.age = a  # age是类的属性
#         self.sex = b
#
#     def sq(self, x):  # sq是类的方法
#         return x ** 2
#
#
# human01 = Human(a=21, b="男")  # 类的实例化
# human01_age = human01.age
# human01_sex = human01.sex
# human01_sq = human01.sq(4)
# print("年龄是:" + str(human01_age) + "," + "性别是:" + human01_sex + "," + "求和结果是:" + str(human01_sq))

"""模块"""
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py
# import math
# a = math.sin(2)  # 使用import直接导入模块，如果需要调用模块中的属性和方法，需要使用模块.方法的形式来调用
# print(a)
# from math import *
# b = sin(2)  # 使用from math import *表示导入math模块中的所有内容，需要调用模块中的属性和方法可以直接写属性和方法
# print(b)
# import math as m  # as 表示将模块进行重命名为m,后面就可以直接用m来表示math库
# a = m.sin(2)
# print(a)
"""第三方库的安装"""
"""在Windows的doc命令下输入 pip install 库名就可以安装第三方库，安装成功后,就可以在pycharm中用导入模块的方式导入库"""

"""assert的应用"""
# import math
#
#
# def f(n):
#     assert n > 0, "n must be positive"  # assert(断言)用于判断一个表达式，当表达式为false时才会产生异常
#     # n > 0的结果时True,所以不会触发后面的异常
#     return math.sqrt(n)  # sqrt()方法用于求根号
#
#
# print(f(4))

"""递归函数的调用"""
# def a(n):
#     if (n == 1):
#         return 1
#     else:
#         return n + a(n - 1)
# 返回的结果是：4+a(3)=4+3+a(2)=4+3+2+a(1)=4+3+2+1


# print(a(4))

"""map方法的应用"""

# # list()为创建一个列表
# b = list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))  # map方法用于将序列的每一个元素作为函数的参数进行运算
# print(b)
"""求长方形周长和面积的类"""


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def getCircumference(self):
#         return (self.width + self.length) * 2
#
#     def getArea(self):
#         return self.length * self.width
#
#
# rectangle = Rectangle(3, 4)  # 在调用类时，尽量把要传递的参数属性设置在__init__方法中
# print("周长是:", rectangle.getCircumference(), "面积是:", rectangle.getArea())
