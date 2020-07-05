"""文件写操作的练习"""
# string = "hello world"
# f = open("hello.txt", "w")  # 以写的方式打开文件hello.txt，没有该文件则自动创建
# f.write(string)  # 向文件中写入string
# f.close()  # 关闭文件

"""遍历的练习"""
# 机器学习 = ["决策树", "神经网络", "支持向量机"]  # 在python3中支持中文的变量名
# for i in 机器学习:
#     print(i)

"""基本数据的练习"""
# import math
# a = -1.5
# b = abs(a)  # abs()函数表示取绝对值
# print(b)
# c = round(math.sin(b),3)  # sin()方法用来计算正弦值，round()方法用来保留小数的位数
# print(c)

"""列表的相关操作"""
# all_list = [0.3, "hello", True, 3]
# a = all_list[-2]  # 列表的索引
# print(a)
# b = all_list[0:3]  # 切片操作取出从0开始的前3个下标的值，从下标为零开始，但不包括下表为3的数，左闭右开
# print(b)
# all_list.append("a")  # append()方法默认在列表末端插入元素
# all_list.insert(2, "b")  # insert()方法可以在列表的指定位置插入元素
# all_list.insert(4, "b")
# all_list.remove("b")  # remove()方法可以删除列表中的指定元素，当存在多个相同的元素时默认删除第一个出现的元素
# """
# del关键字也可以删除列表中的元素，这里表示删除列表中从下标为0开始到下标为2的元素，不包括下标为2的元素,这里的0可以不写,
# 可以写成[:2]的形式，默认从下标为0开始，如果写成[:]表示将整个列表的元素都删除
# """
# del all_list[0:2]
# print(all_list)
# all_list[2] = 1  # 修改列表中指定位置的元素
# print(all_list)
# l = list("python")  # 将python中每一个元素作为列表的一个元素
# print(l)
# a = list(range(0,10,2))  # list()函数也可以生成一个列表
# print(a)
# b = 2,3,4,5  # 这种是定义一个元组
# print(b)
"""for循环"""
# a = []  # 定义一个空的列表
# for i in range(10):  # range(n)函数可以构造一个从0到n的整数，但不包括n
#     a.append(i)
# print(a)
# b = [i for i in range(1, 11)]  # 列表推导式
# c = [i ** 2 for i in range(1, 11)]  # 将每一个遍历的值i都平方后放进列表中
# d = [i ** 2 for i in range(1, 11) if i % 2 == 0]  # 将每一个遍历的值i进行与2相除，如果余数为0则将i进行平方后放进列表
"""
zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
也就是说，该函数返回一个以元组为元素的列表，其中第 i 个元组包含每个参数序列的第 i 个元素。
返回的列表长度被截断为最短的参数序列的长度。只有一个序列参数时，它返回一个1元组的列表。没有参数时，它返回一个空的列表。
"""
# list1 = [1, 2, 3, 4]
# list2 = ["a", "b", "c", "d"]
# list3 = ["A", "B", "C", "D"]
# a = [str(i) + j + k for i,j,k in zip(list1,list2,list3)]  # 这里的i,j,k分别是zip返回的列表中的每一元组中的3个元素
# print(a)
# print(zip(list1, list2, list3))  # 直接输出zip()函数无法得到对应的列表
# print(list(zip(list1, list2, list3)))  # 在zip()函数前加上list()函数可以就可以得到对应的列表
# print(b)
# print(c)
# print(d)

"""练习1：求曲边图形的面积【方法一：for循环】"""
# import math
#
# n = 10000  # 划分要分割的份数
# width = 2 * math.pi / n  # 求每一个矩形的宽度
# height = []  # height为所有矩形的端点横坐标对应的高度列表
# x = []  # x是所有矩形的端点横坐标的列表
# for i in range(n):
#     x.append(i * width)  # 得到所有矩形的端点横坐标
# for i in x:
#     height.append(abs(math.sin(i)))  # 得到所有矩形的端点横坐标对应的高度，abs()取绝对值是因为有一部分的sin()值为负数
# area = width * sum(height)  # sum()可以对列表中的所有元素进行求和
# print("曲边图形的面积为：" + str(area))

"""练习1：求曲边图形的面积【方法二：列表推导式】"""
# import math
#
# n = 10000
# width = 2 * math.pi / n
# area = [abs(math.sin(i * width)) * width for i in range(n)]  # area是一个包含每一个矩形面积的列表
# print("曲面图形的面积为：" + str(sum(area)))

