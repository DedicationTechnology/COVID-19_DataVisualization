# 1.学校python培训笔记

## 1.1python基础知识

### 1.1.1列表

1. 列表的性质：

   > 1.列表中每个元素都是可变的。
   >
   > 2.列表中可以存放各种数据类型的数值

2. 练习题

   - 题目

     ![1](https://raw.githubusercontent.com/DedicationTechnology/picgo/master/img/1.jpg)

   - 代码实现

     ```python
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
     ```

3. zip()函数

   - 说明：zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。也就是说，该函数返回一个以元组为元素的列表，其中第 i 个元组包含每个参数序列的第 i 个元素。返回的列表长度被截断为最短的参数序列的长度。只有一个序列参数时，它返回一个1元组的列表。没有参数时，它返回一个空的列表。

   - 代码理解

     ```python
     list1 = [1, 2, 3, 4]
     list2 = ["a", "b", "c", "d"]
     list3 = ["A", "B", "C", "D"]
     a = [str(i) + j + k for i,j,k in zip(list1,list2,list3)]  # 这里的i,j,k分别是zip返回的列表中的每一元组中的3个元素
     print(a)
     print(zip(list1, list2, list3))  # 直接输出zip()函数无法得到对应的列表
     print(list(zip(list1, list2, list3)))  # 在zip()函数前加上list()函数可以就可以得到对应的列表
     ```

4. 冒泡排序

   ```python
   """冒泡排序"""
   x = [1, 2, 6, 0.3, 0.5, -1, 4]
   l = len(x)
   for i in range(l):
       for j in range(i):  # 冒泡排序在python中的表示方法
           if x[j] > x[i]:  # 将>号改成<号就是降序排列
               x[i], x[j] = x[j], x[i]  # python中交换两个数的值的方法
   print(x)
   ```

5. pass

