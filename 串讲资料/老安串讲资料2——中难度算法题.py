# # 1.将一个正整数进行分解质因数
# # 基础算法实现
# n = num = int(input("请输入一个数字："))
# l = []
# for i in range(num // 2 + 1):
#     for j in range(2,n):
#         if n % j == 0:
#             l.append(j)
#             n //= j
#             break
# if len(l) == 0:
#     print('没有质因数！')
# else:
#     l.append(n)
#     print('%d = %d'%(num,l[0]),end=' ')
#     for x in range(1,len(l)):
#         print('*%d'%l[x],end=' ')
# # 函数封装功能
# def fenjie():
#     n = num = int(input("请输入一个数字："))
#     l = []
#     for i in range(num // 2 + 1):
#         for j in range(2, n):
#             if n % j == 0:
#                 l.append(j)
#                 n //= j
#                 break
#     if len(l) == 0:
#         print('没有质因数！')
#     else:
#         l.append(n)
#         print('%d = %d' % (num, l[0]), end=' ')
#         for x in range(1, len(l)):
#             print('*%d' % l[x], end=' ')
# fenjie()
# # 对象封装功能
# class Fenjie(object):
#     def __init__(self):
#         self.n = self.num = int(input("请输入一个数字："))
#         self.l = []
#     def fenjie(self):
#         for i in range(self.num // 2 + 1):
#             for j in range(2, self.n):
#                 if self.n % j == 0:
#                     self.l.append(j)
#                     self.n //= j
#                     break
#         if len(self.l) == 0:
#             print('没有质因数！')
#         else:
#             self.l.append(self.n)
#             print('%d = %d' % (self.num, self.l[0]), end=' ')
#             for x in range(1, len(self.l)):
#                 print('*%d' % self.l[x], end=' ')


# 2.在一个矩阵中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个矩阵和一个整数，判断矩阵中是否含有该整数。

# 基础算法实现
#手动生成一个二维数组
# l = [
#         [x for x in range(1,5)],
#         [y for y in range(2,6)],
#         [z for z in range(3,7)],
#         [m for m in range(4,8)]
#     ]
# # print(l)
# #你要查找的目标元素
# target = int(input('请输入您要查找的元素>>>：'))
# #标识行号，初始值为0
# row = 0
# #标识最大行号，且行号为列表索引，所以需要len(l) - 1为什么是l？因为二维数组的长度就代表当前二维数组有几行
# maxrow = len(l) - 1
# #标识列号，二维数组任意一行的元素数即当前二维数组的行号，且行号是列表索引，所以需要len(l[0]) - 1
# col = len(l[0]) - 1
# #功能变量，用于判断失败的结果输出
# test = 0
# #循环：col = 0代表是第一列；row = maxlow 代表是最后一行，最后一行，第一列，代表最左下角的元素，所以当前循环是从右上角开始遍历，直到循环到左下角元素，结束
# while col >= 0 and row <= maxrow:
#     #如果当前遍历的元素就是要找的目标元素
#     if l[row][col] == target:
#         #输出成功
#         print('您要查找的元素：%d在当前二维数组中！'%(target))
#         # 改变功能变量值
#         test = 1
#         # 跳出循环
#         break
#     # 否则，如果目标值大于当前遍历的值，说明当前遍历的值较小
#     elif target > l[row][col]:
#         # 增大行号，增大下一次遍历的数
#         row += 1
#     # 否则，如果目标值小于当前遍历的值，说明当前遍历的值较大
#     elif target < l[row][col]:
#         # 减小列号，减小当前遍历的数
#         col -= 1
# if test == 0:
#     print('您要查找的元素：%d不在当前二维数组中！'%(target))

# 函数封装功能

# 生成一个二维数组
# def makeArray():
#     l = [
#         [x for x in range(1, 5)],
#         [y for y in range(2, 6)],
#         [z for z in range(3, 7)],
#         [m for m in range(4, 8)]
#     ]
#     return l
#
# def findMax(l):
#     target = int(input('请输入您要查找的元素>>>：'))
#     row = 0
#     maxrow = len(l) - 1
#     col = len(l[0]) - 1
#     test = 0
#     while col >= 0 and row <= maxrow:
#         if l[row][col] == target:
#             return '您要查找的元素：%d在当前二维数组中！'%(target)
#             test = 1
#             break
#         elif target > l[row][col]:
#             row += 1
#         elif target < l[row][col]:
#             col -= 1
#     if test == 0:
#         return '您要查找的元素：%d不在当前二维数组中！'%(target)
#
# def test():
#     res = findMax(makeArray())
#     print(res)
#
# if __name__ == '__main__':
#     test()

# 闭包封装功能

# def out_():
#     l = [
#         [x for x in range(1, 5)],
#         [y for y in range(2, 6)],
#         [z for z in range(3, 7)],
#         [m for m in range(4, 8)]
#     ]
#     def in_():
#         nonlocal l
#         target = int(input('请输入您要查找的元素>>>：'))
#         row = 0
#         maxrow = len(l) - 1
#         col = len(l[0]) - 1
#         test = 0
#         while col >= 0 and row <= maxrow:
#             if l[row][col] == target:
#                 return '您要查找的元素：%d在当前二维数组中！' % (target)
#                 test = 1
#                 break
#             elif target > l[row][col]:
#                 row += 1
#             elif target < l[row][col]:
#                 col -= 1
#         if test == 0:
#             return '您要查找的元素：%d不在当前二维数组中！' % (target)
#     return in_
#
# def test():
#     res = findTarget = out_()()
#     print(res)
#

# if __name__ == '__main__':
#     test()

# 面向对象封装功能

# class ErfenFindTarget(object):
#     def __init__(self,target):
#         self.l = [
#             [x for x in range(1, 5)],
#             [y for y in range(2, 6)],
#             [z for z in range(3, 7)],
#             [m for m in range(4, 8)]
#         ]
#         self.target = target
#         self.row = 0
#         self.maxrow = len(self.l) - 1
#         self.col = len(self.l[0]) - 1
#         self.test = 0
#
#     def findTarget(self):
#         while self.col >= 0 and self.row <= self.maxrow:
#             if self.l[self.row][self.col] == self.target:
#                     return '您要查找的元素：%d在当前二维数组中！'%(self.target)
#                     self.test = 1
#                     break
#             elif self.target > self.l[self.row][self.col]:
#                 self.row += 1
#             elif self.target < self.l[self.row][self.col]:
#                 self.col -= 1
#         if self.test == 0:
#             return '您要查找的元素：%d在不当前二维数组中！'%(self.target)
#
# def test():
#     find_obj = ErfenFindTarget(int(input('请输入您要查找的元素>>>:')))
#     res = find_obj.findTarget()
#     print(res)
#
# if __name__ == '__main__':
#     test()


# 3.随意输入一行字符，分别统计出其中空格，数字和下划线的个数
# 基本功能实现
# num_tric = 0
# num_num = 0
# num__ = 0
# s_str = input("请输入一串字符：")
# for i in s_str:
#     if i == ' ':
#         num_tric += 1
#     try:
#         is_int = int(i)
#     except ValueError:
#         pass
#     else:
#         num_num += 1
#     if i  == '_':
#         num__+=1
#
# print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n"%(num_tric,num_num,num__))
#
# # 函数封装功能
# def is_str():
#     num_tric = 0
#     num_num = 0
#     num__ = 0
#     s_str = input("请输入一串字符：")
#     for i in s_str:
#         if i == ' ':
#             num_tric += 1
#         try:
#             is_int = int(i)
#         except ValueError:
#             pass
#         else:
#             num_num += 1
#         if i == '_':
#             num__ += 1
#
#     print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n" % (num_tric, num_num, num__))
# is_str()
#
# # 闭包封装功能
#
# def out_():
#     num_tric = 0
#     num_num = 0
#     num__ = 0
#     s_str = input("请输入一串字符：")
#     def in_str():
#         nonlocal num_num,num__,s_str,num_tric
#         for i in s_str:
#             if i == ' ':
#                 num_tric += 1
#             try:
#                 is_int = int(i)
#             except ValueError:
#                 pass
#             else:
#                 num_num += 1
#             if i == '_':
#                 num__ += 1
#         print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n" % (num_tric, num_num, num__))
#     return is_str
# is_str = out_()
# is_str()
#
# # 对象封装功能
# class Is_str:
#     def __init__(self):
#         self.num_tric = 0
#         self.num_num = 0
#         self.num__ = 0
#         self.s_str = input("请输入一串字符：")
#     def begin_is(self):
#         for i in self.s_str:
#             if i == ' ':
#                 self.num_tric += 1
#             try:
#                 self.is_int = int(i)
#             except ValueError:
#                 pass
#             else:
#                 self.num_num += 1
#             if i == '_':
#                 self.num__ += 1
#             print("空格数为：%d\n数字为：%d\n下划线数量为：%d\n" % (self.num_tric, self.num_num, self.num__))
# is_str = Is_str()
# is_str.begin_is()

# 4.手写冒泡排序算法
# 基础算法实现
# l = [9,8,6,5,3]
# for i in range(len(l)-1):
#     for j in range(len(l)-1-i):
#         if l[j] > l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print(l)
#
# # 函数封装实现
#
# def bubble_sort():
#     l = [9, 8, 6, 5, 3]
#     for i in range(len(l) - 1):
#         for j in range(len(l) - 1 - i):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     print(l)
# bubble_sort()
#
# # 闭包封装实现
#
# def out_():
#     l = [9,7,5,4]
#     def in_():
#         nonlocal l
#         for i in range(len(l) - 1):
#             for j in range(len(l) - 1 - i):
#                 if l[j] > l[j + 1]:
#                     l[j], l[j + 1] = l[j + 1], l[j]
#         print(l)
#     return in_
# bubble_sort = out_()
# bubble_sort()
#
# # 对象封装实现
#
# class Bubble_sort:
#     def __init__(self):
#         self.l = [9,7,5,4]
#     def bubble_sort(self):
#         for i in range(len(self.l) - 1):
#             for j in range(len(self.l) - 1 - i):
#                 if self.l[j] > self.l[j + 1]:
#                     self.l[j], self.l[j + 1] = self.l[j + 1], self.l[j]
#         print(self.l)
# bubble_sort = Bubble_sort()
# bubble_sort.bubble_sort()


# 5.现有一个序列，这个序列是用户随机输入的一串字符（降低难度，用户只会输入26个小写字母的随机排列）。问当前用户输入的字符中出现次数最多的字符是谁，并统计次数
# 基础算法实现
# l = []
# dic = {}
# while True:
#     num = input("请输入一个字符：")
#     if num == "over":
#         break
#     l.append(num)
# for i in l:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# print(dic)
# iMax = 0
# iIndex = ''
# for key in dic:
#     if dic[key] > iMax:
#         iMax = dic[key]
#         iIndex = key
# print("出现次数最多的字符是：%s,总共出现了：%d次"%(iIndex,iMax))
# # 函数封装功能
# def is_max():
#     l = []
#     dic = {}
#     while True:
#         num = input("请输入一个字符：")
#         if num == "0":
#             break
#         l.append(num)
#     for i in l:
#         if i not in dic:
#             dic[i] = 0
#         else:
#             dic[i] += 1
#     # print(dic)
#     iMax = 0
#     iIndex = ''
#     for key in dic:
#         if dic[key] > iMax:
#             iMax = dic[key]
#             iIndex = key
#     print("出现次数最多的字符是：%s,总共出现了：%d次"%(iIndex,iMax))
#
# is_max()
# # 闭包封装功能
# def out_():
#     l = []
#     dic = {}
#     iMax = 0
#     iIndex = ''
#     def in_():
#         nonlocal l,dic,iMax,iIndex
#         while True:
#             num = input("请输入一个字符：")
#             if num == "0":
#                 break
#             l.append(num)
#         for i in l:
#             if i not in dic:
#                 dic[i] = 0
#             else:
#                 dic[i] += 1
#         print(dic)
#         for key in dic:
#             if dic[key] > iMax:
#                 iMax = dic[key]
#                 iIndex = key
#     return in_
# is_max = out_()
# is_max()
# # 对象封装功能
# class Is_max:
#     def __init__(self):
#         self.l = []
#         self.dic = {}
#         self.iMax = 0
#         self.iIndex = ''
#     def is_max(self):
#         while True:
#             num = input("请输入一个字符：")
#             if num == "0":
#                 break
#             self.l.append(num)
#         for i in self.l:
#             if i not in self.dic:
#                 self.dic[i] = 0
#             else:
#                 self.dic[i] += 1
#         print(self.dic)
#         for key in self.dic:
#             if self.dic[key] > self.iMax:
#                 self.iMax = self.dic[key]
#                 self.iIndex = key
#         print("出现次数最多的字符是：%s,总共出现了：%d次" % (self.iIndex, self.iMax))
# is_max = Is_max()
# is_max.is_max()


# 6.现有一个降序排列的列表，用户输入一个数字，将其插入列表中形成一个新的降序排序的列表
# 基础算法实现
# l = [9,8,5,3,1]
# num = int(input('请输入您想插入的数据：'))
# index = 0
# for i in range(len(l)):
#     if num > l[i]:
#         index = i
#         break
#
# l.insert(index,num)
# print(l)
#
# # 函数封装功能
# def numInsert():
#     l = [9, 8, 5, 3, 1]
#     num = int(input('请输入您想插入的数据：'))
#     index = 0
#     for i in range(len(l)):
#         if num > l[i]:
#             index = i
#             break
#
#     l.insert(index, num)
#     print(l)
#
# def test():
#     numInsert()
#
# if __name__ == '__main__':
#     test()
#
# # 闭包封装功能
#
# def out_():
#     l = [9, 8, 5, 3, 1]
#     num = int(input('请输入您想插入的数据：'))
#     index = 0
#     def in_():
#         nonlocal l,num,index
#         for i in range(len(l)):
#             if num > l[i]:
#                 index = i
#                 break
#         l.insert(index, num)
#         print(l)
#     return in_
#
# def test():
#     out_()()
#
# if __name__ == '__main__':
#     test()
#
#
# # 面向对象封装功能
#
# class NumInsert(object):
#     def __init__(self):
#         self.l = [9, 8, 5, 3, 1]
#         self.num = int(input('请输入您想插入的数据：'))
#         self.index = 0
#
#     def num_insert(self):
#         for i in range(len(self.l)):
#             if self.num > self.l[i]:
#                 self.index = i
#                 break
#         self.l.insert(self.index, self.num)
#         print(self.l)
#
# def test():
#     NumInsert().num_insert()
#
# if __name__ == '__main__':
#     test()
#



#
# 8.有n个人围成一圈，顺序排号。从第一个人开始报数（1~3报数），凡报到3的人退出圈子，问最后留下的人原来排在第几号。
# num = int(input("请输入人数："))
# k = 0#计算报数
# #根据人数生成列表，列表包含num个数，代表有num个人，num的值代表每个人的编号
# l = [x for x in range(1,num+1)]
# # print(l)
# while len(l) > 1:
#     l_copy = l[:]
#     for i in range(0,len(l_copy)):
#         k += 1
#         if k % 3 == 0:
#             l.remove(l_copy[i])
# print("最后留下来的是原来的第%d号兄弟"%l[0])
#
# #面向对象
#
# class Remove():
#     def __init__(self):
#         self.num = int(input("请输入你想要的人数："))
#         self.count = 0
#
#     def make_list(self):
#         self.L = [x for x in range(1,self.num+1)]
#         return self.L
#
#     def remove_number(self):
#         self.make_list()
#         while len(self.L) > 1:
#             self.L_copy = self.L[:]
#             for i in range(0,len(self.L_copy)):
#                 self.count += 1
#                 if self.count % 3 == 0:
#                     self.L.remove(self.L_copy[i])
#         return self.L
#
# rm = Remove()
# print("最后留下来的是原来的第%d号兄弟"%rm.remove_number()[0])


# 9.直接插入排序
# 思想：将一个记录插入到已排序好的有序表中，从而得到一个“新的”，记录数增1的有序表。
# 思路：先将第一个元素看作一个有序的子序列（说白了就是先把第一个元素假设单独放在一个序列里面，那么这个序列目前只有一个元素，当然就是已经有序了），然后从第二个元素开始依次进行插入，直至整个序列有序为止。
# 算法具体实现步骤：
# 1.	先获得一个随机序列
# 2.	拿出序列第一个元素后，从第二个开始用for循环遍历序列
# 3.	定义一个循环变量j，该变量用来控制插入的位置，因为是后一个和前一个比较，所以让j = i-1
# 4.	定义一个哨兵，专门用来临时存放元素
# 5.	循环的让后一个元素和前一个元素比较，如果后一个元素比前一个元素小，就将其插入前一个元素之前。此时可能存在：已插入的元素仍然比前面某个元素小，所以，j -= 1，在比较一次，直至前面没有比自己大的元素，结束一次遍历
# 6.	最终输出排序完成的列表即可。
#
#初始化序列
# l = [45,34,78,78,98,23,12]
# # 拿出序列第一个元素后，从第二个开始用for循环遍历序列
# for i in range(1,len(l)):
#     # 后面的和前面的比较
#     j = i - 1
#     # 哨兵，临时存放元素
#     key = l[i]
#     # 每一次遍历决定插入的最终位置
#     while j >= 0:
#         # 如果后面的值小于前面的值
#         if key < l[j]:
#             # 后面的值赋值给前面的值，相当于交换位置
#             l[j+1] = l[j]
#             # 前面的值拿出来存在哨兵中
#             l[j] = key
#         # 继续向前比较
#         j -= 1
# print(l)
#
#



# 10.选择排序之简单选择排序
# 思想：在需要排序的序列中选择最小的一个数与第一个数交换位置，
# 在剩余的n-1个数中在选择一个最小的数与剩余n-1个数的序列中第一个元素交换位置，
# 直至剩余元素个数为1，排序结束
# 算法实现步骤：
# 1.遍历序列
# 2.将每一次遍历取到的数和剩余n-1个数的序列中的第一个元素进行交换位置
# l = [3,1,5,7,2,4,9,6]
# for i in range(0, len(l)):
#     # 默认设置最小值的下标为当前值
#     min = i
#     # 在剩余n-1个元素的序列中找到最小元素的下标
#     for j in range(i + 1, len(l)):
#         # if l[i] > l[i+1]
#         # 如果找到，就把最小元素的下标赋值给min
#         if l[min] > l[j]:
#             min = j
#     # 将找到的最小值的元素和当前元素做位置交换
#     temp = l[min]
#     l[min] = l[i]
#     l[i] = temp
# print(l)


# 11.选择排序之堆排序
#     1.算法介绍
#         堆排序是一种树形选择排序，是对直接选择排序的有效改进
#     2.首先先介绍几个知识点概念：
#         1.二叉树：在计算机科学中，每个结点最多有两个子结点的树就叫做二叉树
#             比如：有一个一维数组(python中用列表代替)[3,6,7,2,3,5,6,7,8,9,5,4,3,6,7]
#             将其用以下树形结构展示：
#                             3
#                     6               7
#                 2       3       5       6
#              7     8 9    5  4     3 6     7
#             此树即为二叉树
#             二叉树的子数有左右之分，顺序绝不能颠倒
#
#         3.深度遍历优先算法：指代一种搜索算法，其算法核心是尽可能先对纵深方向进行搜索，
#         当一条分支搜索到叶子结点后，终止，从左往右找到下一条分支，继续开始纵深方向的搜索
#         4.广度遍历优先算法：指代一种搜素算法，其算法核心是针对树形结构的每一层，从根结点出发，按照一层一层的顺序，
#         每层从左至右的顺序搜索，当搜索到某一层最后一个非叶子结点，结束该层搜索，进入下一层，继续搜索，
#         直至搜索到最后一个叶子节点，停止搜索。
#         5.完全二叉树：设二叉树的深度为h，除了h层外，其他各层(h-1)层结点数都达到了最大个数，第h层所有的结点都连续集中在最左边，就是一颗完全二叉树
#         6.叶子结点：没有子女的结点就叫叶子结点
#         7.堆：计算机科学中一类特殊的数据结构的总称。定义如下：n个元素的序列[k1,k2,k3,...ki,...,kn](i = 1,2,3,4,...,n/2),当且仅当满足以下条件：
#         (ki <= k2i,ki <= k2i+1)或>=时，就称之为堆。
#         如果用一个列表存储一个堆，则该堆一定对应一个完全二叉树。那么该完全二叉树的根结点就叫做堆的堆顶元素。
#         当上述条件均为小于时，就会产生小顶堆，反之产生大顶堆。所以由堆的定义可以看出，第一个元素，即堆顶元素必为最小项或最大项，
#         同时，所有非叶子结点的值均不大于或不小于其子女的值
#         比如：
#             大顶堆：[87,84,85,36,11,32]
#                           87
#                     84          45
#                 36      11  32
#             小顶堆：[12,23,26,32,24,30,28,43,35]
#                               12
#                         23          26
#                     32      24  30      28
#                 43      35
#     3.算法实现步骤：
#         初始时把要排序的n个数的序列看作是一棵顺序存储的二叉树（一维数组存储二叉树），调整它们的存储序，
#         使之成为一个堆，将堆顶元素输出，得到n 个元素中最小(或最大)的元素，这时堆的根节点的数最小（或者最大）。
#         然后对前面(n-1)个元素重新调整使之成为堆，输出堆顶元素，得到n 个元素中次小(或次大)的元素。
#         依此类推，直到只有两个节点的堆，并对它们作交换，最后得到有n个节点的有序序列。称这个过程为堆排序。
#         因此，实现堆排序需解决两个问题：
#             1. 如何将n 个待排序的数建成堆；
#             2. 输出堆顶元素后，怎样调整剩余n-1 个元素，使其成为一个新堆。


#
# import random
# import math
#
# #随机生成0~100之间的数值，此随机生成的序列无序
# def get_randomNumber():
#     list=[]
#     i=0
#     num = int(input("请输入元素个数："))
#     while i<num:
#         list.append(math.floor(random.random()*100+1))
#         i += 1
#     return list
#
# # 将一个无序序列形成完全二叉树，此完全二叉树同样无序
# def PrintList_Dui(l):
#     # 提供一个初始化好的列表
#     # 第一行时只有一个数
#     # 每行的数字数量
#     number_count=1#2  4
#     # 行数
#     row_number=1   #2  3
#     # 遍历这个列表
#     # 形成的堆结构
#     print("形成的完全二叉树结构：")
#     for i in range(len(l)):
#         # 因为要形成一个完全二叉树，每一层(行)的元素数量为2 ** (行数-1)个
#         # 使用一个巧妙的算法来实现打印出一个完全二叉树
#         # 此段算法分析：
#         # i = 0时，循环刚开始，因为0和number_count不等，if跳过，直接先打印arr[0]的值，10
#         # i = 1时，1和1相等，执行if,number_count(每行元素个数)变为3，然后换行，行数加1，再输出arr[1] 9
#         # i = 2时，2 和 3 不等，直接打印arr[2] 8
#         # i = 3时，3和3相等，if执行，number_count变为7，换行，行数变为3，输出arr[3] = 7
#         # ...
#         # 直至程序结束
#         #-----------------------------#
#         if i==number_count:
#             number_count += 2 ** row_number# i = 1时，a = 3
#             print("\n")
#             row_number += 1# i = 1时 row = 2
#         #-----------------------------#
#         print (l[i],end="  ")# i = 0,if跳过，直接运行这行，10被打印  i = 1时，if执行，换到第二行，打印9
#         #-----------------------------#
#     print("Over")
#     return l
#
# # 至此，基本功能实现，接下来就是详细实现步骤(大顶堆，形成升序序列)
# # 第一步：创建堆。
# # 将一个无序列表写为顺序二叉树，从最后一个非叶子节点开始，按照从下至上，从左至右的顺序遍历，依次寻找每一个非叶子节点的左右子节点，然后将其与父节点大小进行比较
# # ，如果子节点比父节点大，就将父子节点交换值
#
# # 第一步：创建堆
# def build_heap(l, size):
#     # 从最后一个非叶子结点开始遍历，从下至上，从左至右遍历
#     for i in range(0, (size // 2))[::-1]:
#         adjust_heap(l, i, size)
#         # 此时需要进行调整堆，所以调用调整堆的函数，创建堆其实只是先需要创建一个初始化的堆结构，但因为形成堆结构就需要进行依次
#         # 调整堆，所以在这里需要调用调整堆函数
#
# # 第二步：调整堆
# def adjust_heap(l, i, size):
#     # 父节点i的左子节点
#     lchild = 2 * i + 1
#     # 父节点i的右子节点
#     rchild = 2 * i + 2
#     # 堆顶(最大值)的下标
#     max = i
#     if i < size // 2:
#         # 如果没有超出数组的深度，且非叶子节点左子节点的值大于父节点的值
#         if lchild < size and l[lchild] > l[max]:
#             # 将该非叶子节点的左子节点的值存在在max变量
#             max = lchild
#         # 如果没有超出数组的深度，且非叶子节点右子节点的值大于父节点的值
#         if rchild < size and l[rchild] > l[max]:
#             # 将该非叶子节点的右子节点的值存放在max变量
#             max = rchild
#         # 挑出来的非叶子节点的值的下标此时已经存在max(堆顶，也是最大值)中，将max(带着的就是挑出来的左或者右子节点的下标)跟父节点进行交换
#         if max != i:
#             l[max], l[i] = l[i], l[max]
#             # 到此，准备遍历第二遍，第二遍仍然是在重复调整堆，所以调整函数需要再执行一遍，形成递归。
#             adjust_heap(l, max, size)
#
# # 第三步：堆排序
# def heap_sort(l):
#     # 获取列表长度
#     size = len(l)
#     # 堆排序之前，先创建堆
#     build_heap(l, size)
#     # 从后向前遍历，将每一次调整堆之后获得的堆顶和最后一个元素交换位置，先得到第一大最大值
#     for i in range(0, size)[::-1]:
#         # 循环内，继续进行调整堆，不断得到第二大最大值，第三大最大值，...第n大最大值
#         # 这里是交换位置
#         l[0], l[i] = l[i], l[0]
#         # 重复进行调整堆，直至剩下最后两个元素交换位置，排序完成
#         adjust_heap(l, 0, i)
#         # 整个完整的调整堆的过程就是一个堆排序过程
#         # 所以，其实可以发现，创建堆的过程其实只需要一遍调整堆就ok，但因为第二步是重复调整堆，
#         # 所以很自然的直接过度到调整堆函数，
#         # 而重复调整堆之后每一次调整堆都会交换堆顶和最后一个元素的位置
#         # 不断的形成升序方向的最大值，所以完整的重复调整堆的过程就是堆排序
#     return l
#
#
# l = get_randomNumber()
# print("排序之前(随机生成的列表)：%s" %l)
# b = PrintList_Dui(l)
# print("排序之前，形成完全二叉树结构之后的无序列表:%s"
#       "(其实跟原列表一样一样的，只不过是对照着这个无序列表形成完全二叉树结构)"%b)
# finall_list = heap_sort(l)
# print('排序之后的列表为：%s'%finall_list)




# 12.交换排序之冒泡排序
# 算法归类：交换排序
# 算法思想：使用交换思想，即：前一个元素和后一个元素进行大小比较，如果前面比后面大，就交换位置，然后继续向后比较，直至一次冒泡结束，将最大值(或最小值)
# 放到最后一个位置。通过多次的冒泡，最终实现排序-

# 举例：
# [9,7,5,3]                   [9,8,6,4,3]             ......
# ---------                   ------------
# [7,9,5,3]                   [8,9,6,4,3]
# [7,5,9,3]                   [8,6,9,4,3]
# [7,5,3,9]                   [8,6,4,9,3]             ......
# ---------                   [8,6,4,3,9]
# [5,7,3,9]                   ------------
# [5,3,7,9]                   [6,8,4,3,9]
# ---------                   [6,4,8,3,9]
# [3,5,7,9]                   [6,4,3,8,9]             ......
#                             ------------
#                             [4,6,3,8,9]
#                             [4,3,6,8,9]
#                             ------------
#                             [3,4,6,8,9]
#
# 通过以上的模拟冒泡排序的算法举例，可以总结出如下规律：
# n个元素的序列，总共需要冒泡n-1次
# 设冒泡次数为i，那么每一次冒泡需要比较的次数就为n-i次
# 至此，算法结束

# 算法实现：
# import random
# import math
# l = []
# counts = int(input("请输入您想生成的序列的元素个数："))
# while True:
#     num = math.floor(random.random()*100+1)
#     l.append(num)
#     if len(l) == counts:
#         break
# print('排序前，生成好的随机列表为:%s'%l)
# for i in range(len(l)-1):
#     for j in range(len(l)-i-1):
#         if l[j] > l[j+1]:
#             temp = l[j]
#             l[j] = l[j+1]
#             l[j+1] = temp
# print("排序后的列表为：%s"%l)
#
#

# 13.数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# 基础算法实现

# l = []
# while True:
#     num = int(input("请输入数字>>>："))
#     l.append(num)
#     if len(l) == 10:
#         break
# print(l)
#
# dict = {}
# for i in l:
#     if i not in dict:
#         dict[i] = 1
#     else:
#         dict[i] += 1
#
# print(dict)
#
# for j in dict:
#     if dict[j] > len(l) // 2:
#         print(j)

# 函数封装功能

# def makeList():
#     l = []
#     while True:
#         num = int(input("请输入数字>>>："))
#         l.append(num)
#         if len(l) == 10:
#             break
#     return l
#
# def makeDict(l):
#     dict = {}
#     for i in l:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
#     return dict
#
# def iter(dict,l):
#     for j in dict:
#         if dict[j] > len(l) // 2:
#             return j
#         else:
#             return 0
#
# def test():
#     list = makeList()
#     dict = makeDict(list)
#     res = iter(dict,list)
#     if res == 0:
#         print('当前列表中没有出现次数超过列表长度一半的元素！')
#     else:
#         print('当前列表中出现次数超过列表长度一半的元素为：%d'%res)
#
# if __name__ == '__main__':
#     test()
#
# # 面向对象封装功能
#
# class NumMax(object):
#     def __init__(self):
#         self.l = []
#         self.dict = {}
#
#     def makeList(self):
#         while True:
#             num = int(input('请输入数字>>>:'))
#             self.l.append(num)
#             if len(self.l) == 10:
#                 break
#         return self.l
#
#     def makeDict(self):
#         for i in self.l:
#             if i not in self.dict:
#                 self.dict[i] = 1
#             else:
#                 self.dict[i] += 1
#
#         return self.dict
#
#     def iter(self):
#         for j in self.dict:
#             if self.dict[j] > len(self.l) // 2:
#                 return j
#             else:
#                 return 0
#
#
# def test():
#     n_max = NumMax()
#     n_max.makeList()
#     n_max.makeDict()
#     res = n_max.iter()
#     if res == 0:
#         print('当前列表中没有出现次数超过列表长度一半的元素！')
#     else:
#         print('当前列表中出现次数超过列表长度一半的元素是：%s！'%res)
#
# if __name__ == '__main__':
#     test()


# 14.输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

# 基础算法实现

# l = []
# while True:
#     num = int(input("请输入数字>>>："))
#     l.append(num)
#     if len(l) == 10:
#         break
# print(l)
#
# l_2n = []
# l_2n_1 = []
#
# for i in l:
#     if i % 2 == 1:
#         l_2n_1.append(i)
#     else:
#         l_2n.append(i)
# newl = l_2n_1 + l_2n
# print(newl)

# 函数封装功能

# def makeList():
#     l = []
#     while True:
#         num = int(input("请输入数字>>>："))
#         l.append(num)
#         if len(l) == 10:
#             break
#     return l
#
# def iter(l):
#     l_2n = []
#     l_2n_1 = []
#     for i in l:
#         if i % 2 == 1:
#             l_2n_1.append(i)
#         else:
#             l_2n.append(i)
#     newl = l_2n_1 + l_2n
#     return newl
#
# def test():
#     res = iter(makeList())
#     print(res)
#
# if __name__ == '__main__':
#     test()


# 面向对象封装功能

# class NewList(object):
#     def __init__(self):
#         self.l = []
#
#     def makeList(self):
#         while True:
#             num = int(input('请输入数字>>>:'))
#             self.l.append(num)
#             if len(self.l) == 10:
#                 break
#         return self.l
#
#     def iter(self):
#         l_2n = []
#         l_2n_1 = []
#         for i in self.l:
#             if i % 2 == 1:
#                 l_2n_1.append(i)
#             else:
#                 l_2n.append(i)
#         newl = l_2n_1 + l_2n
#         return newl
#
# def test():
#     newlist = NewList()
#     newlist.makeList()
#     res = newlist.iter()
#     print(res)
#
# if __name__ == '__main__':
#     test()


# 15.某城镇进行人口普查，得到了全体居民的生日。现请你写个程序，找出镇上最年长和最年轻的人。
#
# 这里确保每个输入的日期都是合法的，但不一定是合理的——假设已知镇上没有超过200岁的老人，而今天是2019年5月1日，所以超过200
# 岁的生日和未出生的生日都是不合理的，应该被过滤掉。

# 基础算法实现
n = int(input('请输入人口数量：'))
# 用于计数生日合理的人数
count = 0
# 年龄范围截止到今天的算合法
max1 = ['', '2019/05/01']
# 年龄范围最早到200年前的算合法
min1 = ['', '1819/05/01']
# 循环的创建n个居民的生日信息
for i in range(n):
    # 输入居民生日信息,用空格分割字符串,存为列表
    person = input('请输入居民姓名及生日信息：').split()
    print(person)
    # 如果当前居民的生日数据合理
    if '1819/05/01' <= person[1] <= '2019/05/01':
        # 计数+1,代表多1个合理的居民生日信息
        count += 1
        # 如果当前居民的生日在2019/05/01之前：
        if person[1] < max1[1]:
            # 把年份最大的变量赋值为当前居民的生日
            max1 = person
        # 如果当前居民的生日在1819/05/01之后
        if person[1] > min1[1]:
            # 把年份最小的变量赋值为当前居民的生日
            min1 = person
# 如果计数为0，代表没有合法的生日数据
if count == 0:
    print('0')
else:
    # 否则，输出总共的合理的生日的居民数，输出年龄最大的（年份值最小），输出年龄最小的（年份值最大）
    print(count, max1[0], min1[0])


# 16.给定数字0-9各若干个。你可以以任意顺序排列这些数字，但必须全部使用。目标是使得最后得到的数尽可能小（注意0不能做首位）。例如：给定两个0，两个1，三个5，一个8，我们得到的最小的数就是10015558。
# 现给定数字，请编写程序输出能够组成的最小的数。
# 输入格式：
#
# 每个输入包含1个测试用例。每个测试用例在一行中给出10个非负整数，顺序表示我们拥有数字0、数字1、……数字9的个数。整数间用一个空格分隔。10个数字的总个数不超过50，且至少拥有1个非0的数字。
#
# 输出格式：
#
# 在一行中输出能够组成的最小的数。
# 输入样例：
#
# 2 2 0 0 0 3 0 0 1 0
# 输出样例：
#
# 10015558

# 具体思路：只要首位不是0，是最小的数字，后续位数按照升序排列，得到的就是最小的数

# 基础算法实现

# 生成列表
# l = []
# while True:
#     num = input('请输入数字>>>:')
#     if num == 'exit':
#         break
#     l.append(int(num))
# print('您输入的数字所组成的列表:%s,后续将生成最小数字'%l)
#
# # 除去‘0’元素
# n = 0
# count = 0
# while n < len(l):
#     if l[n] == 0:
#         l.pop(n)
#         n -= 1
#         count += 1
#     n += 1
# print('去除0之后的列表;%s'%l)
# print('删除了%d个0'%count)
#
#
# # 将除去0之后的列表升序排列
# for i in range(len(l)-1):
#     for j in range(len(l)-1-i):
#         if l[j] > l[j+1]:
#             l[j],l[j+1] = l[j+1],l[j]
# print('排序之后的列表：%s'%l)
#
# # 将count个0插入第一个元素后面
# for y in range(count):
#     l.insert(1,0)
#
# print('生成最小数的列表：%s'%l)
#
# # 将此列表转化为字符串
# str1 = ''.join([str(m) for m in l])
# print(str1)


# 函数封装功能

# def makeList():
#     l = []
#     while True:
#         num = input('请输入数字>>>:')
#         if num == 'exit':
#             break
#         l.append(int(num))
#     return l #'您输入的数字所组成的列表,后续将生成最小数字'
#
# def deleteZero(l):
#     n = 0
#     count = 0
#     while n < len(l):
#         if l[n] == 0:
#             l.pop(n)
#             n -= 1
#             count += 1
#         n += 1
#     return (l,count)#'去除0之后的列表;'删除0的个数'
#
# def bubbleSort(l):
#     for i in range(len(l) - 1):
#         for j in range(len(l) - 1 - i):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]
#     return l  #除去0之后，排序之后的列表
#
# def zeroInsert(l,count):
#     for y in range(count):
#         l.insert(1,0)
#     return l #生成最小数的列表
#
# def listToStr(l):
#     return ''.join([str(m) for m in l]) #列表转化为字符串
#
# def test():
#     res1 = deleteZero(makeList())
#     # res2 = bubbleSort(res1[0])
#     # res3 = zeroInsert(res2,res1[1])
#     # resStr = listToStr(res3)
#     resStr = listToStr(zeroInsert(bubbleSort(res1[0]),res1[1]))
#     print(resStr)
#
#
# if __name__ == '__main__':
#     test()
#


# 输入一组测试用例，结构为n n n n n n n n n n,各个元素的下标从0开始，，所以每个n对应的下标为 0 1 2 3 4 5 6 7 8 9 代表0-9 10个数字，每个n的值代表当前数字的个数，然后将其分割为列表
# n = input('请输入测试用例>>>:').split()
# print(n)
# # 预备一个空字符串str1，等待存数据
# str1 = ''
# # 遍历列表的每一个元素
# for i in range(len(n)):
#     # i此时取到了每个元素的下标，代表一个数字，该数字乘以其个数，个数即为每个元素（字符串）对应的整型值，不断累加，实现根据测试用例生成一个整数（此整数此时为字符型）这个整数就是我们要操作的，生成目标最小值的原型整数
#     str1 += str(i)*int(n[i])
# print(str1)
# # 遍历当前整数，拿到每一个字符值
# for i in range(len(str1)):
#     # 如果每次循环拿到的字符值不为0，即，一直循环，直到拿到第一个不为0的值时，
#     if str1[i]!='0':
#         # 跳出循环
#         break
# # 跳出循环后，此时循环变量i保存的值为某个元素的索引，这个索引所对应的元素就是当前字符串中第一个不为0的整数值，先输出这个整数值
# print(str1[i],end="")
# # 然后，再从头遍历到当前第一个整数值之前的元素，这区间的数全都为0
# for j in range(0,i):
#     # 再把这些0从第二个位置开始挨个输出
#     print(str1[j],end="")
# # 最后，从第一个整数值之后的元素开始，遍历到字符串结束
# for j in range(i+1,len(str1)):
#     # 输出剩余的整数值
#     print(str1[j],end="")
# #


# 17.给定一个正整数数列，和正整数p，设这个数列中的最大值是M，最小值是m，如果M <= m * p，则称这个数列是完美数列。
# 即：随机生成一个数列并给定一个正整数p，如果数列最大值 <= 最小值 × p，则是完美数列，否则就不是完美数列

# 函数封装功能
# def makeList():
#     l = []
#     while True:
#         num = input('请输入数字>>>:')
#         if num == 'exit':
#             break
#         l.append(int(num))
#     return l
#
# def iter(l):
#     p = int(input('请输入正整数p>>>:'))
#     if max(l) <= min(l) * p:
#         print('%s数列是完美数列！')
#     else:
#         print('%s数列不是完美数列！')
#
# def test():
#     iter(makeList())
#
# if __name__ == '__main__':
#     test()
#


# 18.给定任一个各位数字不完全相同的4位正整数，如果我们先把4个数字按非递增排序，再按非递减排序，然后用第1个数字减第2个数字，将得到
# 一个新的数字。一直重复这样做，我们很快会停在有“数字黑洞”之称的6174，这个神奇的数字也叫Kaprekar常数。
#
# 例如，我们从6767开始，将得到
#
# 7766 - 6677 = 1089
# 9810 - 01
# 89 = 9621
# 9621 - 1269 = 8352
# 8532 - 2358 = 6174
# 7641 - 1467 = 6174
# ......
#
# 现给定任意4位正整数，请编写程序演示到达黑洞的过程。


# 思路：定义一个递增算法和递减算法，每一遍运算循环分别调用递减算法和递增算法生成两个运算数，然后做运算即可。

# 基础算法实现

# # 递减算法
# def Descending(l):
#     for i in range(len(l)-1):
#         for j in range(len(l)-1-i):
#             if l[j] < l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#     return l
# #递增算法
# def Ascending(l):
#     for i in range(len(l)-1):
#         for j in range(len(l)-1-i):
#             if l[j] > l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]
#     return l
#
# # 功能算法-生成数字序列，用于后续运算
# def Kaperekar():
#     num = input('请输入一个正整数>>>:')
#     l = num.split(',')
#     print(l)
#
# Kaperekar()

# def hei(a):
#     x = sorted(a,reverse = True)
#     y = sorted(a)
#     str1 = ''
#     str2 = ''
#     for i in x:
#         str1+=i
#     for i in y:
#         str2+=i
#     result = str(int(str1)-int(str2))
#     if len(result)<4:
#         result = '0'*(4-len(result))+result
#     if result=='0000':
#         print('%s %s %s %s %s'%(str1,'-',str2,'=','0000'))
#     else:
#         print('%s %s %s %s %s'%(str1,'-',str2,'=',result))
#     return result
# a = input('请输入数字>>>：')
#
def makeNumberBlackHole():
    num_bl = input('请输入数字>>>：')
    if len(num_bl) < 4:
        num_bl += '0' * (4 - len(num_bl))
    return num_bl

def numberBlackHole(num_bl):
    m = sorted(num_bl,reverse=True)
    n = sorted(num_bl)
    strm = ''
    strn = ''
    for i in m:
        strm += i
    for i in n:
        strn += i
    result = str(int(strm) - int(strn))
    if len(result) < 4:
        result = '0' * (4-len(result)) + result
    if result == '0000':
        print('%s %s %s %s %s'%(strm,'-',strn,'=','0000'))
    else:
        print('%s %s %s %s %s'%(strm,'-',strn,'=',result))
    return result

def test():
    str1 = numberBlackHole(makeNumberBlackHole())
    while str1 != '0000':
        if str1 == '6174' or str1 == '0':
            break
        str1 = numberBlackHole(str1)

if __name__ == '__main__':
    test()