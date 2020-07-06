# 1.学校python培训笔记

## 1.1python基础知识

1. 列表的性质：

   > 1.列表中每个元素都是可变的。
   >
   > 2.列表中可以存放各种数据类型的数值

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

4. **运算符

   ```python
   x = 2
   x *= 2 ** 2 ** 3 // 100
   """2 ** 2 ** 3 // 100 的结果是2，**的优先级高于//，后者表示取整，2 ** 2 ** 3 的结果是2的8次方而不是4的3次方，
   先算2**3"""
   print(x)
   y = 2 ** 2 ** 3
   print(y)
   ```

5. 字符串为不可变类型

   ```python
   example = "abcd"
   print(example.replace("a", "e"))  # replace()方法用来将a替换为b
   print(example)  # 字符串为不可变类型
   ```

6. 另类的if else表示形式

   ```python
   """如果6>6则i=5,否则如果4>3则i=2,还不满足则i=3"""
   i = 5 if 6 > 6 else (2 if 4 > 3 else 3)
   print(i)
   ```

7. 另一种函数的定义形式

   ```python
   # 第二种函数定义的方式
   a = lambda x: x + 2  # 定义一个函数，a为函数名，x为形参，x+2为返回值
   b = a(2)
   print(b)
   c = lambda x: x[1] # 定义一个函数，c为函数名，x为形参，返回x中下标为1的元素
   d = c([1,2,3])
   print(d)
   ```

8. 列表推导式

   ```python
   # b = [i for i in range(1, 11)]  # 列表推导式，将每一个遍历的值放入列表中
   ```

9. 字典推导式

   ```python
   a = {i: i ** 2 for i in range(0,10)}  # :前面的i是键，后面的i ** 2是值
   print(a)
   ```

10. pass

