# PAT介绍:浙江大学计算机程序设计能力考试（Programming Ability Test，简称PAT）是由浙江大学计算机科学与技术学院组织的统一考试，旨在培养和展现学生分析问题、解决问题和计算机程序设计的能力，科学评价计算机程序设计人才，并为企业选拔人才提供参考标准。

# 以下内容，为2018年PAT乙级(Basic Level)真题及参考答案。
# 注意：所有编码，全部按照算法的最佳性能标准，即：从时间复杂度，空间复杂度及稳定性角度，三个维度考察算法的性能。

# 1.给定区间[-2的31次方, 2的31次方]内的3个整数A、B和C，请判断A+B是否大于C。

# import sys
# def Is_more():
#   global a,b,c
#   a = int(input('请输入第一个数>>:'))
#   b = int(input('请输入第二个数>>:'))
#   c = int(input('请输入第三个数>>:'))
#   if a is int and b is int and c is int:
#     if (a + b) == c:
#       return '相等'
#     elif (a + b) > c:
#       return True
#     else:
#       return False


# def test():
#   result = Is_more()
#   if result == '相等':
#     print('%d+%d的值为%d,之和等于第三个数%d'%(a,b,a+b,c))
#   elif result == True:
#     print('%d+%d的值为%d,之和大于第三个数%d'%(a,b,a+b,c))
#   else:
#     print('%d+%d的值为%d,之和小于第三个数%d'%(a,b,a+b,c))


# if __name__ == '__main__':
#   test()



# 2.给定一系列正整数，请按要求对数字进行分类，并输出以下5个数字：

# A1 = 能被5整除的数字中所有偶数的和；
# A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；
# A3 = 被5除后余2的数字的个数；
# A4 = 被5除后余3的数字的平均数，精确到小数点后1位；
# A5 = 被5除后余4的数字中最大数字。
# import math
# import random
# def make_random_number_list():
#   # global l
#   l = []
#   while True:
#     num = math.floor(random.random()*100+1)
#     l.append(num)
#     if len(l) == 30:
#       break
#   return l
# # L = make_random_number_list()
# # print('生成的随机序列为：%s'%L)

# def A1(l):
#   l_A1 = []
#   for i in l:
#     if i % 5 == 0 and i % 2 == 0:
#       l_A1.append(i)
#   return sum(l_A1)

# def A2(l):
#   l_A2 = []
#   num_2n = 0
#   num_2n_1 = 0
#   for i in l:
#     if i % 5 == 1:
#       l_A2.append(i)
#   for key in range(len(l_A2)):
#     if key % 2 == 0:
#       num_2n += l_A2[key]
#     else:
#       num_2n_1 += l_A2[key]
#   return num_2n - num_2n_1

# def A3(l):
#   l_A3 = []
#   for i in l:
#     if i % 5 == 2:
#       l_A3.append(i)
#   return len(l_A3)

# def A4(l):
#   l_A4 = []
#   for i in l:
#     if i % 5 == 3:
#       l_A4.append(i)
#   return round(sum(l_A4) / len(l_A4),1)

# def A5(l):
#   l_A5 = []
#   for i in l:
#     if i % 5 == 4:
#       l_A5.append(i)
#   return max(l_A5)

# def test():
#   finall_list = make_random_number_list()
#   a1 = A1(finall_list)
#   a2 = A2(finall_list)
#   a3 = A3(finall_list)
#   a4 = A4(finall_list)
#   a5 = A5(finall_list)
#   print('当前生成的随机列表为：%s'%finall_list)
#   print('当前列表中，能被5整除的数字中所有偶数的和为%d'%a1)
#   print('当前列表中，被5除后余1的数字按给出顺序进行交错求和后的值为%d'%a2)
#   print('当前列表中，被5除后余2的数字的个数为%d'%a3)
#   print('当前列表中，被5除后余3的数字的平均数为:%f'%a4)
#   print('当前列表中，被5除后余4的数字中最大数字为%d'%a5)

# if __name__ == '__main__':
#   test()


# 3.令Pi表示第i个素数。现任给两个正整数M <= N <= 10000，请输出PM到PN的所有素数。

# def is_sushu():
#   global m,n
#   l = []
#   m = int(input('请输入>>>:'))
#   n = int(input('请输入>>>:'))
#   for i in range(m,n+1):
#     j = 2
#     for j in range(2,i):
#       if i % j == 0:
#         break
#     else:
#       l.append(i)
#   return l



# def test():
#   result = is_sushu()
#   print('%d到%d之间所有的素数为:'%(m,n),end=' ')
#   for k in result:
#     print('%d'%k,end=' ')



# if __name__ == '__main__':
#   test()




# 4.大侦探福尔摩斯接到一张奇怪的字条：“我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm”。大侦探很

#  快就明白了，字条上奇怪的乱码实际上就是约会的时间“星期四 14:04”，因为前面两字符串中第1对相同的大写英文字母（大小写有区分）是

#  第4个字母'D'，代表星期四；第2对相同的字符是'E'，那是第5个英文字母，代表一天里的第14个钟头（于是一天的0点到23点由数字0到9、

#  以及大写字母A到N表示）；后面两字符串第1对相同的英文字母's'出现在第4个位置（从0开始计数）上，代表第4分钟。现给定两对字符串，

#  请帮助福尔摩斯解码得到约会的时间。

# 分析：对比每一对字符串，遵循如下规律：
# 第一对字符串：
#   1.第一对相同的大写英文字母代表星期几，用A-G代表星期一到星期四
#   2.按位向后继续比较，第二对相同的字符代表几点，用0-9 + A-N代表0到23点
# 第二对字符串：
#   第一对相同的英文字母出现在第几个位置(从0开始计数)上，代表几分
# s = '我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm'
# s1 = s.split(' ')
# print(s1[1][1])


# def _encode():
#   week = {'A':'星期一','B':'星期二','C':'星期三','D':'星期四','E':'星期五','F':'星期六','G':'星期日'
#   }
#   hour = {'0':'00','1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17','I':'18','J':'19','K':'20','L':'21','M':'22','N':'23'}
#   return (week,hour)
#
# def make_str():
#   str = input('请输入福尔摩斯码>>：')
#   return str
#
# def _decode(code_book,code):
#   weeks = ''
#   hours = ''
#   minutes = ''
#   code_list = code_book.split(' ')
#   for i,j in zip(code_list[0],code_list[1]):
#     if i == j:
#       hours = i
#     if i.isupper() and j.isupper() and i == j:
#       weeks = j
#   for x,y in zip(code_list[2],code_list[3]):
#     if x == y:
#       minutes = x
#   return (code[0][weeks],code[1][hours],code_list[2].index(minutes))
#
# def test():
#   result = _decode(make_str(),_encode())
#   print(result)
# test()
# def _decode(code,):
# x = [1,2,3]
# y = [4,5,6]
# for i,j in zip(x,y):
#   print(i)
#   print(j)



# 5.在一个矩阵中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个矩阵和一个整数，判断矩阵中是否含有该整数。

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


# 6.数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

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





# 8.输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

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





# 9.某城镇进行人口普查，得到了全体居民的生日。现请你写个程序，找出镇上最年长和最年轻的人。
#
# 这里确保每个输入的日期都是合法的，但不一定是合理的——假设已知镇上没有超过200岁的老人，而今天是2019年5月1日，所以超过200
# 岁的生日和未出生的生日都是不合理的，应该被过滤掉。

# 基础算法实现
# n = int(input('请输入人口数量：'))
# # 用于计数生日合理的人数
# count = 0
# # 年龄范围截止到今天的算合法
# max1 = ['', '2019/05/01']
# # 年龄范围最早到200年前的算合法
# min1 = ['', '1819/05/01']
# # 循环的创建n个居民的生日信息
# for i in range(n):
#     # 输入居民生日信息,用空格分割字符串,存为列表
#     person = input('请输入居民姓名及生日信息：').split()
#     print(person)
#     # 如果当前居民的生日数据合理
#     if '1819/05/01' <= person[1] <= '2019/05/01':
#         # 计数+1,代表多1个合理的居民生日信息
#         count += 1
#         # 如果当前居民的生日在2019/05/01之前：
#         if person[1] < max1[1]:
#             # 把年份最大的变量赋值为当前居民的生日
#             max1 = person
#         # 如果当前居民的生日在1819/05/01之后
#         if person[1] > min1[1]:
#             # 把年份最小的变量赋值为当前居民的生日
#             min1 = person
# # 如果计数为0，代表没有合法的生日数据
# if count == 0:
#     print('0')
# else:
#     # 否则，输出总共的合理的生日的居民数，输出年龄最大的（年份值最小），输出年龄最小的（年份值最大）
#     print(count, max1[0], min1[0])


# 10.给定数字0-9各若干个。你可以以任意顺序排列这些数字，但必须全部使用。目标是使得最后得到的数尽可能小（注意0不能做首位）。例如：给定两个0，两个1，三个5，一个8，我们得到的最小的数就是10015558。
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


# 11.给定一个正整数数列，和正整数p，设这个数列中的最大值是M，最小值是m，如果M <= m * p，则称这个数列是完美数列。
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


# 12.给定任一个各位数字不完全相同的4位正整数，如果我们先把4个数字按非递增排序，再按非递减排序，然后用第1个数字减第2个数字，将得到
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

# def makeNumberBlackHole():
#     num_bl = input('请输入数字>>>：')
#     if len(num_bl) < 4:
#         num_bl += '0' * (4 - len(num_bl))
#     return num_bl
#
# def numberBlackHole(num_bl):
#     m = sorted(num_bl,reverse=True)
#     n = sorted(num_bl)
#     strm = ''
#     strn = ''
#     for i in m:
#         strm += i
#     for i in n:
#         strn += i
#     result = str(int(strm) - int(strn))
#     if len(result) < 4:
#         result = '0' * (4-len(result)) + result
#     if result == '0000':
#         print('%s %s %s %s %s'%(strm,'-',strn,'=','0000'))
#     else:
#         print('%s %s %s %s %s'%(strm,'-',strn,'=',result))
#     return result
#
# def test():
#     str1 = numberBlackHole(makeNumberBlackHole())
#     while str1 != '0000':
#         if str1 == '6174' or str1 == '0':
#             break
#         str1 = numberBlackHole(str1)
#
# if __name__ == '__main__':
#     test()



