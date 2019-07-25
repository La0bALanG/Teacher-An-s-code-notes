# # 1.形如ABCCBA形式的字符串我们都叫做回文字符。请问，如何判断输入的某个字符是回文字符？
# # 基础算法实现
# str = input("请输入一个字符串：")
# if str[::-1] == str:
#     print("您输入的字符串是回文字符")
# else:
#     print("您输入的字符串不是回文字符")
#
# # 函数封装功能
# def is_hui():
#     str = input("请输入一个字符串：")
#     if str[::-1] == str:
#         print("您输入的字符串是回文字符")
#     else:
#         print("您输入的字符串不是回文字符")
# is_hui()
#
# # 闭包封装功能
# def out_hui():
#     str = input("请输入一个字符串：")
#     def in_hui():
#         nonlocal str
#         if str[::-1] == str:
#             print("您输入的字符串是回文字符")
#         else:
#             print("您输入的字符串不是回文字符")
#     return in_hui
# is_hui = out_hui()
# is_hui()
# # 对象封装功能
# class Is_hui:
#     def __init__(self):
#         self.str = input("请输入一个字符串：")
#     def isReady_hui(self):
#         if self.str[::-1] == self.str:
#             print("您输入的字符串是回文字符")
#         else:
#             print("您输入的字符串不是回文字符")
# is_hui = Is_hui()
# is_hui.isReady_hui()
#
# # 2.有1,2,3,4四个数字，请问能组成多少个互不相同且无重复数字的三位数？
# # 基础算法实现
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and i != k and j != k:
#                 print(i,j,k)
#
# # 函数封装功能
# def is_Num():
#     for i in range(1,5):
#         for j in range(1,5):
#             for k in range(1,5):
#                 if i != j and i != k and j != k:
#                     print(i,j,k)
# is_Num()
#
# # 改为闭包
# def out_is():
#     it = range(1,5)
#     def in_is():
#         nonlocal it
#         for i in it:
#             for j in it:
#                 for k in it:
#                     if i != j and i != k and j != k:
#                         print(i,j,k)
#     return in_is
# ok = out_is()
# ok()
# # 3.输入三个整数，请把这三个数由小到大的输出（要求使用最简单的逻辑算法）
# # 基础算法实现
# a = int(input("请输入第一个数字："))
# b = int(input("请输入第二个数字："))
# c = int(input("请输入第三个数字："))
# print((a if a > c else c)if a > b else (b if b > c else c))
# # 函数封装功能
# def is_max():
#     a = int(input("请输入第一个数字："))
#     b = int(input("请输入第二个数字："))
#     c = int(input("请输入第三个数字："))
#     print((a if a > c else c)if a > b else (b if b > c else c))
# is_max()
# # 闭包封装功能
# def out_max():
#     a = int(input("请输入第一个数字："))
#     b = int(input("请输入第二个数字："))
#     c = int(input("请输入第三个数字："))
#     def in_max():
#         nonlocal a,b,c
#         print((a if a > c else c) if a > b else (b if b > c else c))
#     return in_max
# is_max = out_max()
# is_max()
# # 对象封装功能
# class Is_Max:
#     def __init__(self):
#         self.a = int(input("请输入第一个数字："))
#         self.b = int(input("请输入第二个数字："))
#         self.c = int(input("请输入第三个数字："))
#     def is_max(self):
#         print((self.a if self.a > self.c else self.c) if self.a > self.b else (self.b if self.b > self.c else self.c))
# is_max = Is_Max()
# is_max.is_max()
# # 4.输出9*9乘法口诀
# # 基础算法实现
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%s*%s=%s'%(i,j,i*j),end=" ")
#     print()
# # 函数封装功能
# def mul_list():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('%s*%s=%s'%(i,j,i*j),end=" ")
#     print()
# mul_list()
# # 闭包封装功能
# def out_():
#     it = range(1,10)
#     def in_():
#         nonlocal it
#         for i in it:
#             for j in it:
#                 print('%s*%s=%s'%(i,j,i*j),end=" ")
#                 if j > i:
#                     break
#             print()
#     return in_
# mul_list = out_()
# mul_list()
#
# # 5.输出1000以内所有的水仙花数。水仙花数：是指一个三位数，其各位数字的立方和等于这个数本身
# # 基础算法实现
# for i in range(100,1000):
#     if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
#         print(i)
# # 函数封装功能
# def flower():
#     for i in range(100,1000):
#         if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
#             print(i)
# flower()
# # 闭包封装功能
# def out_():
#     it = range(100,1000)
#     def in_():
#         nonlocal it
#         for i in it:
#             if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
#                 print(i)
#     return in_
# flower = out_()
# flower()
# # 对象封装功能
# class Flower:
#     def __init__(self):
#         self.it = range(100,1000)
#     def flower(self):
#         for i in self.it:
#             if (i // 100) ** 3 + (i // 10 % 10) ** 3 + (i % 10) ** 3 == i:
#                 print(i)
# flower = Flower()
# flower.flower()

# 6.实现功能：将一个字符串中的空格替换成"%20"

# # 基础算法实现
# str = input('请随意输入一串字符>>>:')
# newStr = ''
# for i in str:
#     if i == ' ':
#         newStr = str.replace(i,'%20')
# print(newStr)
#
# # 函数封装功能
#
# def strReplace():
#     str = input('请随意输入一串字符>>>:')
#     newStr = ''
#     for i in str:
#         if i == ' ':
#             newStr = str.replace(i, '%20')
#     print(newStr)
#
# def test():
#     strReplace()
#
# if __name__ == '__main__':
#     test()
#
# # 闭包封装功能
# def out_():
#     str = input('请随意输入一串字符>>>:')
#     def in_():
#         nonlocal  str
#         newStr = ''
#         for i in str:
#             if i == ' ':
#                 newStr = str.replace(i, '%20')
#         print(newStr)
#     return in_
#
# def test():
#     out_()()
#
# if __name__ == '__main__':
#     test()
#
# # 面向对象封装功能
#
# class StrReplace(object):
#     def __init__(self):
#         self.str = input('请随意输入一串字符>>>:')
#         self.newStr = ''
#     def iter(self):
#         for i in self.str:
#             if i == ' ':
#                 self.newStr = self.str.replace(i, '%20')
#         print(self.newStr)
#
# def test():
#     StrReplace().iter()
#
# if __name__ == '__main__':
#     test()


# 7.动态生成一个列表
# # # 基础算法实现
# l = []
# while True:
#     num = int(input("请输入一个数字："))
#     if num == '0':
#         break
#     l.append(num)
# print(l)
#
# # 函数封装功能
#
# def make_list():
#     l = []
#     while True:
#         num = int(input("请输入一个数字："))
#         if num == '0':
#             break
#         l.append(num)
#     print(l)
# make_list()
#
# # 闭包封装功能
#
# def out_():
#     l = []
#     def in_():
#         nonlocal l
#         while True:
#             num = int(input("请输入一个数字："))
#             if num == '0':
#                 break
#             l.append(num)
#         print(l)
#     return in_
# make_list = out_()
# make_list()
#
# # 对象封装功能
# class Make_list:
#     def __init__(self):
#         self.l = []
#     def make_list(self):
#         while True:
#             num = int(input("请输入一个数字："))
#             if num == '0':
#                 break
#             self.l.append(num)
#         print(self.l)
# make_list = Make_list()
# make_list.make_list()


# 8.将一个列表进行反序
# 基础算法实现
# l = [4,5,3,2]
# newL = l[::-1]
# print(newL)
# # 函数封装功能
# def res():
#     l = [4, 5, 3, 2]
#     newL = l[::-1]
#     print(newL)
# res()
# # 闭包封装功能
# def out_():
#     l = [4, 5, 3, 2]
#     def in_():
#         nonlocal l
#         newL = l[::-1]
#         print(newL)
#     return in_
# res = out_()
# res()
# # 对象封装功能
# class Res:
#     def __init__(self):
#         self.l = [3,2,4,5]
#     def res(self):
#         self.newL = self.l[::-1]
#         print(self.newL)
# res = Res()
# res.res()
#
# # 9.去除一个列表中重复的元素
# # 基础算法实现
# l = [2,2,3,3,5,6,7,5]
# newL = []
# for i in l:
#     if i not in newL:
#         newL.append(i)
# print(newL)
# # 函数封装功能实现
# def rep():
#     l = [2, 2, 3, 3, 5, 6, 7, 5]
#     newL = []
#     for i in l:
#         if i not in newL:
#             newL.append(i)
#     print(newL)
# rep()
# # 闭包封装功能
# def out_():
#     l = [2, 2, 3, 3, 5, 6, 7, 5]
#     newL = []
#     def in_():
#         nonlocal l, newL
#         for i in l:
#             if i not in newL:
#                 newL.append(i)
#         print(newL)
#     return in_
# rep = out_()
# rep()
# # 对象封装功能
# class Rep:
#     def __init__(self):
#         self.l = [2, 2, 3, 3, 5, 6, 7, 5]
#         self.newL = []
#     def rep(self):
#         for i in self.l:
#             if i not in self.newL:
#                 self.newL.append(i)
#         print(self.newL)
# rep = Rep()
# rep.rep()