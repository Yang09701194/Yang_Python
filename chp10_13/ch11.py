
# OOP
# 封裝 encapsulation  繼承  inheritance (code重用 或 override) 
# 多型  polymorphism (子類 override(覆寫 重寫)  或父開 abstract 同名稱介面  子類不同實作)

# 方法同名參數不同   多載 重載 overload  也可以算是多型  wiki 多型
# 動態綁定  late binding   執行時才確定型別  找出對應的屬性方法執行

# 建立實體  1 直譯器配置mem空間  2 呼叫 __init__ 建構式 constructor

import abc


class MyClass(): # 括號內放繼承的父類
    pass
MyClass.pi = 3.14 # 可以動態加屬姓  類似 javascript 
# 但是通常不這樣用   按一般規則都是先定義好再用
#430
class BankAccount():
    def __init__(self, name, id): #-> None:
        #pass
        self.balance = 0
        self.name = name;
        self.id = id;
    def deposit(self, amount):# 存款
        self.balance += amount
    def withdraw(self, amount):# 提款
        self.balance -= amount
    def getbalance(self, amount):# 餘額
        return self.balance
# 方法的第一個參數  是物件本身
a0 = BankAccount('test', '123')
print(a0.balance)
a0.deposit(100)
a0.withdraw(30)
print(a0.getbalance())

# 434
class MyClass():
    # 這是 static 變數的意思 而且還不會被方法裡 self.x 修改 
    # 不同東西  但是又跟 static 有小差異 因為方法直接 z 看不到
    x, y, z = 3, 4, 5 
    def sfoo():
        #print(z)  #error  方法執行時  視野是全域  看不到區域變數
        print(MyClass.z)
    def __init__(self,x ,y):
        # 這兩個名字 跟 static一樣  但是是不同變數  是一般區域變數 不同物件各自獨立
        self.x = x  
        self.y = y
    def foo(self): print(self.x + self.z)
    def bar(self):
        #print(self.y - z)  # error z 看不到
        print(self.y -MyClass.z)
c0 = MyClass(2,3)
c1 = MyClass(1,5)
c0.bar()  # 相當 MyClass.bar(c0)
c1.bar()
c1.sfoo() # err 因為沒有 self參數 不能 MyClass.sfoo(c1)


# 繼承   如果沒有繼承可以省略括號
# 所有 class 都預設繼承 object
class Foo(): pass
class Foo: pass

class Sub(MyClass, Foo):
    ww = 1000
    x = 200
    def subFooBar(self):
        self.foo() # 呼叫父類的方法
        self.bar()
s0 = Sub(2,3)
s0.foo() #父
s0.subFooBar() #子
# 物件方法的辨識順序    MRO Method Resolution Order
# A : B
# B 無 __init__  會用 A
# B 有 __init__  不會預設呼叫 A 要手動呼叫
class Sub2(MyClass, Foo):
    def __init__(self, x, y):
        super().__init__(x, y)  # vsc  的 intellisense 不錯自動產生
        #或者
        MyClass.__init__(x, y)
        self.tt = 3

# 覆寫  重載  多型
class Animal():
    def shout(self): print('Animal shout')
class Dog(Animal):
    def shout(self): print('Dog shout') # override
class Cat(Animal):
    def shout(self): print('Cat shout') # override  也是多型
# python 是動態型別  所以同個樣式的參數方法  可以傳入不同型別  所以有點就算是多載
# 靜態型別語言 java 就會試  test(int)  test(float) 不同型別的參數

#  print 時 是呼叫類的 __str__ 也可覆寫
class Foo:
    def __str__(self): return 'Foo'
# 其他 object 可覆寫方法  ex
# __new__
# __class__
# __hash__
# __getattr__
# __setattr__
# __repr__
# __sizeof__
# __dir__(self)

# 抽象類別  Sized __len__  Sequence __getitem__ Hashable _hash___
# 只要類別中  覆寫抽象類的全部方法  就會自動符合抽象類

class Frange():
    def __init__(self, start, stop=None, step=None):
        self.start = start + 0.0
        self.stop = stop
        self.step = step
        if self.stop is None:
            self.stop = self.start + 0.0
            self.start = 0.0
        if self.step is None:
            self.step = 1.0
    def __iter__(self):  # Iterable
        return self
    def __next__(self):  # Iterable
        next = self.start
        self.start += self.step
        if abs(next) < abs(self.stop):
            return next
        else:
            raise StopIteration

for x in Frange(3):
    print(x)
print([i for i in Frange(2.55, 3.7, 0.1)])
print([i for i in Frange(0, 1, 0.1)])

# 運算子重載  operator overlaoding   ex +
# + __add__
# - __sub__
# * __mul__
# / __div__
# // __truediv__
# ...
# override 就可以改變行為
# a+b  變 a.__add__(b)

# 私有方法
# 方法名稱前加兩底線 __  直譯器會自動轉成 _classname_name 不會被子類覆寫
# 但是 python 沒有真正的私有屬性   知道名稱還是可用  A._A__name()

class Foo:
    x = 3
    @staticmethod  # decorator 轉成靜態方法 參數第一個  不用是實體本身  直接吃參數
    def foo(x, y): pass
    @classmethod  # decorator 轉成類別方法  第一參 是類別  不是實體
    def foo2(cls, y): 
        return cls.x
    @property
    def name(self):
        # 可做其他事  呼叫  f.name 會調用
        return self.name
    @name.setter
    def name(self, value):
        # 可做其他事  呼叫   f.name = xx 會調用
        self.name = value        
    @name.deleter
    def name(self):
        # 可做其他事  呼叫  del f.name 會調用
        del self.name

# 多重繼承 multiple inheritance  446
#   S     鑽石  菱形繼承
# A   B
#   C
class S(object):
    def foo(self): print('S')
class A(S):
    def foo(self): print('A')
class B(S):
    def foo(self): print('S')
class C(A, B):
    # 搜尋順序  往上一層層  左到右  C-A-B-S-object
    def foo(self): pass   

# 如果   D(A,B) E(B,A)  P(D, E)  會 error MRO  因為 A B 順序不一致

# 有多重繼承  C++ Eiffel Perl
# 認為問題多不支援  可能就改成用 介面 Interface 達成  Smalltalk Java C#

# 447 後設類別 metaclass  就是  type   幾乎等同 object  
# 是繼承層級架構的頂端中的頂端  


# 自訂抽象父類別  ABC abstract base class  類似 Sequence Mapping
from abc import ABCMeta, abstractclassmethod, abstractmethod
class S(metaclass = ABCMeta):
    @abstractmethod
    def method1(self, arg1): pass
    def method2(self, arg1, arg2): pass
# s = S()  err 不能建立實體

class Sub(S):
    def method1(self, arg1):  # 厲害 vsc intellisense 自動完成
        print(arg1)
    def method2(self, arg1, arg2):
        print(arg2)




# 445
class FromNtoM():
    def __init__(self, n, m):
        self.n = n
        self.m = m
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.m:
            tmp, self.n = self.n, self.n+1
            return tmp
        else:
            raise StopIteration

print(sum(FromNtoM(1, 100+1)))
print(sum(range(1, 100+1)))

