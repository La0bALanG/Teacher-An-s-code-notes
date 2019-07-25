#coding:utf-8

# 准备代码：
# 1.随机序列

from random import random
from math import floor
def makeList():
    l = []
    while True:
        num = floor(random()*20 + 1)
        l.append(num)
        if len(l) == 21:
            break
    return l






#1.输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

# import random
# import math
# def makeList():
#     l = []的
#     while True:
#         num = math.floor(random.random() * 20 + 1)
#         l.append(num)
#         if len(l) == 20:
#             break
#
#     return l
#
# def reverseList(l):
#     l.reverse()
#     return l
#
# def test():
#     result = reverseList(makeList())
#     print('反序后的列表为：%s'%result)
#
# if __name__ == '__main__':
#     test()


# 2.实现单例模式
#        1.定义：单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。
#            举例：比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。
#            我们先看看单例模式问题从何而来：
# class A(object):
#    def __init__(self):
#        pass
#    def foo(self):
#        pass

# a = A()
# print(id(a))
# b = A()
# print(id(b))
#            运行结果如下：
#            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#            140534096496512
#            140534096497128
#            很明显，通过打印实例的id可以发现，A类默认被创建了两个实例a和b
#            那么，如何让类只去实例化一个对象，而后再创建的实例是返回上一次的对象的引用呢？
#        2.单例模式实现方式——使用模块
#            其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：
# 创建一个单例模块mysingleton.py

# mysingleton.py
# class Singleton(object):
#    def __init__(self):
#        self.name = '小安安'
#    def foo(self):
#        print('我是：%s'%self.name)
# singleton = Singleton()


# from mysingleton import singleton
# singleton.foo()

#        3.单例模式实现方式——使用装饰器

# def singleton(cls,*args,**kwargs):
#    '''
#    使用装饰器的原理：
#    1.先创建外层函数，需要传入一个参数，此参数为类(对象)
#    2.创建一个空字典，用来保存单例
#    3.创建一个内层函数，用来获得单例
#    4.内层函数中进行判断：如果当前字典不存在单例，就创建单例，如果存在，直接返回该单例的引用
#    5.外层函数返回内层函数

#    '''
#    instances = {}
#    print('装饰器函数被调用！')
#    def get_singleton(*args,**kwargs):
#        if cls not in instances:
#            instances[cls] = cls(*args,**kwargs)
#        print('装饰器内层函数也被调用！')
#        print(instances)
#        return instances[cls]
#    return get_singleton

# @singleton
##此处，相当于：Student = singleton(Student)
# class Student(object):
#    '''
#    创建单例的原理：
#    1.先由类实例化对象：xiaoanan = Student(30,'小安安')并传参，此时，因为前面已添加装饰器@singleton，Student此时相当于绑定到了get_singleton函数，这句实例化对象的语句其实就是如下格式：xiaoanan = get_singleton(30,'小安安'),而实例化对象时，这句话相当于调用了装饰器的内部函数get_singleton，因为是第一次创建对象xiaoanan ,当前字典中并没有单例xiaoanan,所以内层函数get_singleton中会执行if语句真值表达式为True时的语句，即：instances[cls] = cls(*args,**kwargs)，而这里的cls接收到的参数是Student，所以此句代码相当于：instances[Student] = Student(30,'小安安'),即给字典键名为Student的键添加一个值，这个值是Student类实例化的对象
#    2.当又一次实例化对象xiaochaochao时，因为仍然还是通过Student类实例化该对象，而之前的单例已经存在于字典中了，所以不会再创建第二个单例，只会直接返回已有的单例并绑定当前的引用，进而真正实现了单例模式！

#    '''
#    def __init__(self,age,name):
#        self.age = age
#        self.name = name
#        print('__init__()方法被调用了')
# xiaoan = Student(30,'小安安')
# xiaochaochao = Student(18,'小超超')
# print(id(xiaoan))
# print(id(xiaochaochao))

#            最终执行结果：
#            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#            装饰器函数被调用！
#            __init__()方法被调用了
#            装饰器内层函数也被调用！
#            {<class '__main__.Student'>: <__main__.Student object at 0x7fe08913f748>}
#            装饰器内层函数也被调用！
#            {<class '__main__.Student'>: <__main__.Student object at 0x7fe08913f748>}
#            140602349188936
#            140602349188936

#            此方式即实现了单例模式。


#        4.单例模式实现方式——使用类
# import threading
# import time

# class Singleton(object):
#    def __init__(self):
#        # time.sleep(1)
#        pass

#    @classmethod
#    def instance(cls,*args,**kwargs):
#        if not hasattr(Singleton,'_instance'):
#            Singleton._instance = Singleton(*args,**kwargs)
#        return Singleton._instance
# def test(args):
#    a = Singleton.instance()
#    print(id(a))
## b = Singleton.instance()


# for i in range(10):
#    t = threading.Thread(target=test,args=[i,])
#    t.start()

#            程序暂时先写成这样，我们先运行一下，看看结果：
#            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#            140291643101480
#            140291643101480
#            140291643101480
#            140291643101480
#            140291643101480
#            140291643101480
#            140291643101480
#            140291643101480
#            140291643101480
#            140291643101480
#            看上去，没毛病，恩，实现了单例，但其实！有毛病！此时看上去没问题是因为执行速度过快，如果我们让__init__方法存在一些IO操作，就会发现问题。
#            下面，我们用睡眠代替可能的IO操作看看会出现什么效果

# import threading
# import time

# class Singleton(object):
#    def __init__(self):
#        time.sleep(1)

#    @classmethod
#    def instance(cls,*args,**kwargs):
#        if not hasattr(Singleton,'_instance'):
#            Singleton._instance = Singleton(*args,**kwargs)
#        return Singleton._instance
# def test(args):
#    a = Singleton.instance()
#    print(id(a))
## b = Singleton.instance()


# for i in range(10):
#    t = threading.Thread(target=test,args=[i,])
#    t.start()

#            此时，我们再看看程序运行的结果：
#            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#            140107826004320
#            140107826107280
#            140107825398672
#            140107825883008
#            140107825392944
#            140107825882896
#            140107825398952
#            140107826107504
#            140107825835816
#            140107825881496

#            问题出现了！按照以上方式创建的单例，不支持多线程！
#            ok，如果非得采用这种方式来创建单例，解决办法是：加锁！
#            未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全
#            再看如下代码：

# import threading
# import time

# class Singleton(object):
#    _instance_lock = threading.Lock()
#    def __init__(self):
#        time.sleep(1)

#    @classmethod
#    def instance(cls,*args,**kwargs):
#        with Singleton._instance_lock:
#            if not hasattr(Singleton,'_instance'):
#                Singleton._instance = Singleton(*args,**kwargs)
#        return Singleton._instance
# def test(args):
#    a = Singleton.instance()
#    print(id(a))
## b = Singleton.instance()


# for i in range(10):
#    t = threading.Thread(target=test,args=[i,])
#    t.start()

# time.sleep(5)
# a = Singleton.instance()
# print(id(a))


#            此时，我们再看看程序运行的结果：
#            anwc@anwc:~/文档/课程资料$ python3 23+1种设计模式——Python实现.py
#            140142050939176
#            140142050939176
#            140142050939176
#            140142050939176
#            140142050939176
#            140142050939176
#            140142050939176
#            140142050939176
#            140142050939176
#            140142050939176

#            到此，其实大致解决了我们的需求了，但是还是有一些小问题，就是当程序执行时，执行了time.sleep(20)后，下面实例化对象时，此时已经是单例模式了，但我们还是加了锁，这样不太好，再进行一些优化，把intance方法，改成下面的这样就行：


# import threading
# import time

# class Singleton(object):
#    _instance_lock = threading.Lock()
#    def __init__(self):
#        time.sleep(1)

#    @classmethod
#    def instance(cls,*args,**kwargs):
#        if not hasattr(Singleton,'_instance'):
#            with Singleton._instance_lock:
#                if not hasattr(Singleton,'_instance'):
#                    Singleton._instance = Singleton(*args,**kwargs)
#        return Singleton._instance
# def test(args):
#    a = Singleton.instance()
#    print(id(a))
## b = Singleton.instance()


# for i in range(10):
#    t = threading.Thread(target=test,args=[i,])
#    t.start()

# time.sleep(5)
# a = Singleton.instance()
# print(id(a))

#            至此，支持多线程的单例实现结束，但这种方式还有弊端，不过不痛不痒了，很好发现：这种方式实现的单例，使用时会有限制，以后实例化对象必须通过调用类方法实现，即：
#            a = Singleton.instance()
#            而原本单单通过累的实例化，得到的就不是单例了。

#        5.单例模式实现方式——基于__new__方法实现
#            接上面的例子，已知，对于多线程情况下的单例，为了保证线程安全我们在内部加入了锁。
#            同时，再引入一个知识点。当我们实例化对象的时候，是先执行了__new__方法(如果不写，会默认调用Object.__new__,因为现版本中都是新式类，新式类默认继承自object)实例化对象，再调用__init__方法初始化实例化对象。基于以上，我们可以使用__new__方法实现单例模式
# import threading
# import time

# class Singleton(object):
#    _instance_lock = threading.Lock()
#    def __init__(self):
#        time.sleep(1)
#    def __new__(cls,*args,**kwargs):
#        if not hasattr(Singleton,'_instance'):
#            with Singleton._instance_lock:
#                if not hasattr(Singleton,'_instance'):
#                    Singleton._instance = object.__new__(cls)
#        return Singleton._instance

## o1 = Singleton()
## o2 = Singleton()
## print(o1)
## print(o2)

# def test(args):
#    o = Singleton()
#    print(id(o))

# for i in range(10):
#    t = threading.Thread(target=test,args=[i,])
#    t.start()
# class
#        6.单例模式实现方式——基于metaclass实现
#            1.知识点补充
#                1.Python中的类也是一个对象
#                2.类是由元类来创建的
#                3.type是众多类的元类
#                4.类由type创建。创建类时，type的__init__()方法自动执行；类()，即由类实例化对象时，执行type的__call__()方法(其中包含__new__()和__init__()方法)
#                5.对象由类创建。创建对象时，类的__init__()方法自动调用，对象()时执行类的__call__()方法
# import threading

# class SingletonType(type):
#    _instance_lock = threading.Lock()
#    def __call__(cls, *args, **kwargs):
#        if not hasattr(cls, "_instance"):
#            with SingletonType._instance_lock:
#                if not hasattr(cls, "_instance"):
#                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
#        return cls._instance

# class Foo(metaclass=SingletonType):
#    def __init__(self,name):
#        self.name = name


# obj1 = Foo('name')
# obj2 = Foo('name')
# print(obj1,obj2)


# 3.数组中重复的数字

#在长度为n的数组中，所有的元素都是0到n-1的范围内。 数组中的某些数字是重复的，但不知道有几个重复的数字，
#也不知道重复了几次，请找出任意重复的数字。 例如，输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出为2或3

# def findRepeat(l):
#     for index,value in enumerate(l):
#         if index != value:
#             l[index],l[value] = l[value],l[index]

#         if index != value and value == l[value]:
#             return l[index]

# def test():
#     print('找到的重复的元素为:%d'%findRepeat(makeList()))

# if __name__ == '__main__':
#     test()

#4.在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 生成一个二维数组
# def makeArray():
#     l = [
#         [x for x in range(1, 5)],
#         [y for y in range(2, 6)],
#         [z for z in range(3, 7)],
#         [m for m in range(4, 8)]
#     ]
#     return l

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

# def test():
#     res = findMax(makeArray())
#     print(res)

# if __name__ == '__main__':
#     test()


# 5.请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# def strReplace():
#     str = input('请随意输入一串字符>>>:')
#     newStr = ''
#     for i in str:
#         if i == ' ':
#             newStr = str.replace(i, '%20')
#     print(newStr)

# def test():
#     strReplace()

# if __name__ == '__main__':
#     test()

# 6.输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


# 基本思想介绍：二叉树是一种非常重要的数据结构，非常多其他数据结构都是基于二叉树的基础演变而来的。对于二叉树，有深度遍历和广度遍历，深度遍历有前序、中序以及后序三种遍历方法，广度遍历即我们寻常所说的层次遍历。由于树的定义本身就是递归定义，因此採用递归的方法去实现树的三种遍历不仅easy理解并且代码非常简洁，而对于广度遍历来说，须要其他数据结构的支撑。比方堆了。所以。对于一段代码来说，可读性有时候要比代码本身的效率要重要的多。

# 四种基本的遍历思想为：

# 前序遍历：根结点 ---> 左子树 ---> 右子树

# 中序遍历：左子树---> 根结点 ---> 右子树

# 后序遍历：左子树 ---> 右子树 ---> 根结点

# 层次遍历：仅仅需按层次遍历就可以

# 算法实现：
# class Treenode(object):
#     def __init__(self,x):
#         self.value = x
#         self.left = None
#         self.right = None

# class AlogorithmRelization(object):

#     def reConstractBinaryTree(self,pre,mid):
#         if len(pre) == 0:
#             return None

#         root_data = Treenode(pre[0])
#         i = mid.index(pre[0])
#         root_data.left = self.reConstractBinaryTree(pre[1:i + 1],mid[:i])
#         root_data.right = self.reConstractBinaryTree(pre[1 + i:],mid[i + 1:])
#         return root_data

# def test():
#     pre_order = [1,2,4,7,3,5,6,8]
#     mid_order = [4,7,2,1,5,3,6,8]
#     BinartTree = AlogorithmRelization().reConstractBinaryTree(pre_order,mid_order)
#     print(BinartTree.value)
#     print(BinartTree.left)
#     print(BinartTree.right)

# if __name__ == '__main__':
#     test()



# 7.用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# class Solution(object):
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def push(self, node):
#         # write code here
#         self.stack1.append(node)
#     def pop(self):
#         #检查stack2是否为空，不为空弹出，
#         #为空继续判断stack1是否为空，不为空放入stack2中，为空表示栈内无元素
#         try:
#             _pop = self.stack2.pop()
#         except IndexError as e:
#             if len(self.stack1) != 0:
#                 for i in range(len(self.stack1)):
#                     self.stack2.append(self.stack1.pop())
#                 _pop = self.stack2.pop()
#             else:
#                 _pop = None
#         return _pop

# def test():
#     s = Solution()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#     s.push(5)
#     s.push(6)
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     s.push(7)
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())

# if __name__ == '__main__':
#     test()



# 8.把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# def minNumberInRotateArray(rotateArray):
#     left = 0
#     right = len(rotateArray)-1
#     while left < right:
#         mid = int((left+right)/2)
#         if rotateArray[mid] > rotateArray[right]:
#             left = mid+1
#         elif rotateArray[mid] < rotateArray[right]:
#             right = mid
#         else:
#             right -= 1
#     return rotateArray[left]

# def test():
#     res = minNumberInRotateArray([2,1,3,4,7])
#     print(res)

# if __name__ == "__main__":
#     test()




# 9.大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39



# def fib_num(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib_num(n-1) + fib_num(n-2)

# def fib_factory():
#     l = []
#     for i in range(20):
#         l.append(fib_num(i))
#     return l

# def test():
#     fib_list = fib_factory()
#     print(fib_list)

# if __name__ == '__main__':
#     test()




# 10.一个青蛙，一次可以跳上1级台阶，也可以跳上2级台阶。问青蛙跳上一个n级台阶总共有多少种跳法

# def fib(n):
#     if n == 0:
#         return "不合法！"
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(4))


# # 11.一个青蛙，一次可以跳上1级台阶，也可以跳上2级台阶……也可以跳上n级台阶。问青蛙跳上一个n级台阶总共有多少种跳法


# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return 2 * fib(n-1)


# print(fib(4))


# 12.我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# def fib(n):
#     if n == 0:
#         return "不合法！"
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(4))

# 13.输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# def binary_num(n):
#     str = bin(n)
#     target = str[2:]
#     count = 0
#     for i in target:
#         if i == '1':
#             count += 1
#
#     print(target)
#     print(count)
# binary_num(100)


# 14.给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

# def get_pow(base,exp):
#     return base ** exp
#
# res = get_pow(2.1,3)
# print(res)

# 15.输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

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

# 16.输入一个链表，输出该链表中倒数第k个结点。

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution(object):
#     def FindKthToTail(self, head, k):
#         # write code here
#         pre = post = head
#         # 快指针先走k步
#         for i in range(k):
#             # 如果k大于链表长度，返回空
#             if pre == None:
#                 return None
#             pre = pre.next
#         # 快慢指针同时往前走
#         while pre != None:
#             pre = pre.next
#             post = post.next
#         return post


# 17.输入一个链表，反转链表后，输出新链表的表头。

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution(object):
#     # 返回ListNode
#     def ReverseList(self, pHead):
#         # write code here
#         if not pHead or not pHead.next:
#             return pHead
#
#         last = None
#
#         while pHead:
#             tmp = pHead.next  # 将下一步的地址指向给tmp
#             pHead.next = last  # 将一个新的链表指向给旧链表pHead，这个时候就把pHead截断了，只剩下前面的链表值
#             last = pHead  # 将旧链表的地址指向给新链表
#             pHead = tmp  # 将旧链表原来的下一步只指向给pHead
#         return last

# 18.输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

# class Node(object):
#         def __init__(self, elem, next_=None):
#                 self.elem = elem
#                 self.next = next_
#
# class List(object):
#         def __init__(self):
#                 self.head = None
#                 self.num = 0
#
#         def is_empty(self):
#                 return self.head is None
#
#         def prepend(self, elem):
#                 self.head = Node(elem, self.head)
#                 self.num += 1
#
#         def prepop(self):
#                 if self.is_empty():
#                         raise ValueError("List is Empty")
#                 e = self.head.elem
#                 self.head = self.head.next
#                 self.num -= 1
#                 return e
#
#         def append(self, elem):
#                 if self.is_empty():
#                         self.head = Node(elem)
#                         return
#                 p = self.head
#                 while p.next:
#                         p = p.next
#                 p.next = Node(elem)
#                 self.num += 1
#
#         def bianli(self):
#                 p = self.head
#                 li = []
#                 while p:
#                         li.append(p.elem)
#                         p = p.next
#                 return li
#
# def merge_list(lista,listb):
#         indexa = lista.head
#         indexb = listb.head
#         ml = List()
#         while indexa and indexb:
#                 if indexa.elem <= indexb.elem:
#                         ml.append(indexa.elem)
#                         indexa = indexa.next
#                 else:
#                         ml.append(indexb.elem)
#                         indexb = indexb.next
#         while indexa:
#                 ml.append(indexa.elem)
#                 indexa = indexa.next
#         while indexb:
#                 ml.append(indexb.elem)
#                 indexb = indexb.next
#         return ml.bianli()
#
# if __name__ == "__main__":
#         lista = List()
#         for i in range(10,-1,-2):
#                 lista.prepend(i)
#         print(lista.bianli())
#         listb = List()
#         for i in range(21,0,-2):
#                 listb.prepend(i)
#         print(listb.bianli())
#         print(merge_list(lista,listb))

# 19.输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

# class Solution:
#     # 给定两个二叉树（的根节点）A、B，判断B 是不是A 的二叉树
#     def HasSubtree(self, pRoot1, pRoot2):
#         if pRoot1 == None or pRoot2 == None:
#             return False
#
#         result = False
#         if pRoot1.val == pRoot2.val:
#             result = self.isSubtree(pRoot1, pRoot2)
#         if result == False:
#             result = self.HasSubtree(pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)
#         return result
#
#     def isSubtree(self, root1, root2):
#         if root2 == None:
#             return True
#         if root1 == None:
#             return False
#         if root1.val == root2.val:
#             return self.isSubtree(root1.left, root2.left) & self.isSubtree(root1.right, root2.right)
#         return False
#
#
#     # 给定二叉树的前序遍历和中序遍历，获得该二叉树
#     def getBSTwithPreTin(self, pre, tin):
#         if len(pre)==0 | len(tin)==0:
#             return None
#
#         root = treeNode(pre[0])
#         for order,item in enumerate(tin):
#             if root .val == item:
#                 root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
#                 root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
#                 return root
#
# class treeNode:
#     def __init__(self, x):
#         self.left = None
#         self.right = None
#         self.val = x
#
# if __name__ == '__main__':
#     solution = Solution()
#     preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
#     middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
#     treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
#     preorder_seq = [1, 2, 3]
#     middleorder_seq = [2, 1, 3]
#     treeRoot2 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
#     print(solution.HasSubtree(treeRoot1, treeRoot2))

# 20.操作给定的二叉树，将其变换为源二叉树的镜像。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回镜像树的根节点
#     def Mirror(self, root):
#         if not root:
#             return None
#         root.left, root.right = root.right, root.left
#         if root.left:
#             self.Mirror(root.left)
#         if root.right:
#             self.Mirror(root.right)

# 21.输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         # write code here
#         if matrix==[[]]:
#             return
#         row=len(matrix)
#         column=len(matrix[0])
#         start=0
#         res=[]
#         while row>start*2 and column>start*2:
#             endX=column-1-start
#             endY=row-1-start
#             #从左到右打印一行
#             for i in range(start,endX+1):
#                 res.append(matrix[start][i])
#                 #print(matrix[start][i])
#             #从上往下打印一列
#             if start<endY:
#                 for i in range(start+1,endY+1):
#                     res.append(matrix[i][endX])
#                     #print(matrix[i][endX])
#             #从右到左打印一行
#             if start<endX and start<endY:
#                 for i in range(endX-1,start-1,-1):
#                     res.append(matrix[endY][i])
#                     #print(matrix[endY][i])
#             #从下到上打印一列
#             if start<endX and start<endY-1:
#                 for i in range(endY-1,start,-1):
#                     res.append(matrix[i][start])
#                     #print(matrix[i][start])
#             start+=1
#         return res

# 22.定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
#!/usr/bin/env python3

# class Node(object):
#     def __init__(self, elem, next_=None):
#         self.elem = elem
#         self.next = next_
#
# class LStack(object):
#     def __init__(self):
#         self.top = None
#
#     def is_empty(self):
#         return self.top is None
#
#     def push(self, elem):
#         self.top = Node(elem, self.top)
#
#     def pop(self):
#         if self.is_empty():
#             raise ValueError("Stack is Empty")
#         e = self.top.elem
#         self.top = self.top.next
#         return e
#
#     def peek(self):
#         if self.is_empty():
#             raise ValueError("Stack is Empty")
#         return self.top.elem
#
# class Stack_Find_Min(object):
#     def __init__(self):
#         self.s1 = LStack()
#         self.s2 = LStack()
#         self.minvalue = 0
#
#     def is_empty(self):
#         return self.s1.is_empty()
#
#     def push(self, elem):
#         self.s1.push(elem)
#         if self.s2.is_empty():
#             self.s2.push(elem)
#             self.minvalue = elem
#         elif elem < self.minvalue:
#             self.s2.push(elem)
#             self.minvalue = elem
#
#     def pop(self):
#         if self.s1.is_empty():
#             raise ValueError("Stack is Empty")
#             e = self.s1.pop()
#         if e == self.minvalue:
#             self.s2.pop()
#             self.minvalue = self.s2.peek()
#         return e
#
#     def peek(self):
#         return self.s1.peek()
#
#     def minx(self):
#         return self.s2.peek()
#
# if __name__=="__main__":
#     sm = Stack_Find_Min()
#     for i in [3,2,7,9,4,6,8,1]:
#         sm.push(i)
#     print("minx:",sm.minx())
#     print("pop:",sm.pop())
#     print("minx:",sm.minx())

# 23.输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）


# class Solution:
#     def IsPopOrder(self, pushV, popV):
#         # write code here
#         stack = []
#         for i in pushV:
#             stack.append(i)
#             while stack and stack[-1] == popV[0]:
#                 stack.pop()
#                 popV.pop(0)
#         return True if not stack else False



# 24.从上往下打印出二叉树的每个节点，同层节点从左至右打印。






























