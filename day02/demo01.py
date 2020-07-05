"逻辑控制符练习"
# print("name" == 'name')  # 结果为True
# print("P" in "Python")  # 判断P是否在Python中

# """冒泡排序"""
# x = [1, 2, 6, 0.3, 0.5, -1, 4]
# l = len(x)
# for i in range(l):
#     for j in range(i):  # 冒泡排序在python中的表示方法
#         if x[j] > x[i]:  # 将>号改成<号就是降序排列
#             x[i], x[j] = x[j], x[i]  # python中交换两个数的值的方法
# print(x)

"""字符串的相关操作"""
# string1 = """01  # python中定义一个字符串也可以用三引号
#      23
# 45"""
# print(string1)  # 字符串中的内容会原样输出，包括空格
# a = "124" * 3  # 字符串的重复
# print(a)
# a = "my name is dedicationYu"
# b = a.split()  # split()函数可以分割字符串，且默认按照空格分隔字符串，返回的结果是一个列表
# print(b)
# c = a.split(sep="n")  # sep后面的内容表示按什么字符进行分割
# print(c)
# d = a.lower()  # lower()函数用来将大写字母变成小写字母
# print(d)
"""字符串是不可变的类型，里面的字符是不可以修改的，所作的相关操作都不会修改原先字符串的内容，列表是可变类型，
里面的元素是可以修改的"""

"""字典的相关操作"""
# a = {"one": 0.1, 2: "two"}  # 字典的定义,字典中的键必须是不可变的内容
# a["three"] = "three"  # 向字典中增加单个键值对
# a.update({"four": "four", "five": "five"})  # 使用update()函数向字典中增加多个键值对
# del a["three"]  # 删除键值对的值
# print(a)

"""字典推导式"""
# a = {i: i ** 2 for i in range(0,10)}  # :前面的i是键，后面的i ** 2是值
# print(a)

