

# 可迭代的 iterable  迭代器 iterator

e = [1,2]
type(e) is list  # is 也可以用於 型別判斷
# type(方法名) is type.FunctionType 或  type.ModuleType 

# p114 還有  type.BuiltinFunctionType type.BuiltinMethodType  fractions.Fraction 
# dict slice set
# callable isinstance p115

# 型別有許多屬性 attribute   > C#  類別有許多屬性 properties
# dir() 可以看類別有那些東西  類似 C# GetProperties
# 物件都有 .__class__  相同  type 語法

# namespace 命名空間  是  名稱  真正存在的地方  p116
# Local Enclosing Global Builtin

# 抽象型別  p118  有點像是 interface
# 例如 序列 Sequence 是 抽象  list tuple str 是 實際型別
# 有點像是  動物 抽象 > 貓 狗  實際
# 118 有類別架構圖  就是一般看到的  類型名稱  還有包含的屬性  和箭頭指向代表繼承關係
# 抽象形別放在 模組 collections.abc
from collections.abc import *
# issubclass(子型別, 父型別) T F

# Iterable 抽象形別  定義建立 Iterator 的介面  Iterator 定義 取下個元素的介面
li = [11,12,13]
lit = iter(li)
next(lit)  # 11
next(lit)  # 12

# 序列型別共同操作
# x in s  not in 
# < <= >= != ==
# + * [index]   [i:j] # i~j  [i:j:k]  len min max index(ele)  index(ele[, i[, j]]) count

# 可變序列共同操作  t是可迭代者  x是值
# s[i]=x  del[si] # 刪除  s[i:j]=t 都t  del s[i:j] s[i:j:k]=t  del s[i:j:k] append(x)
# extend(t)  clear # 等同del s[:]  copy  insert  pop(index)  remove 等同 del   reverse sort

li = [1,2,3,4,5,6] 
li[-1] # 是 li[li.length - 1] 也就是 倒數第一個元素
# li[2:]
# li[:4]

# >>> li = [1,2,3,4,5]
# >>> first, *rest = li   星號序列指派  拿出第0個 和其他
# >>> rest
# [2, 3, 4, 5]
# >>> first
# 1

# li[0:2] = a,b
# (3,4,5) in li

# list tuple 的 + 會產生新物件  效能不好  可改用  list.extend 原地修改
# str 可以改用 join 
#  * 是  淺複製   li2 = li * 3    li修改  li2 會跟著修改
# += *=  如果是不可變物件  右邊建立新物件給左邊   否則原地修改

# slice 很像是 li[:] 
# li = [0,1,2,3]
# s0 = slice(0,2) ; s1 = slice(1,5,2)
# li[s0] # [0,1]
# li[s1] # [0,2] # index 1, 1+2

# range 是建立 不可變的序列型別    #2.x分成 range > list可變 xrange > tuple不可變
# 3.x range 2.x xrange 數字大的時候  不會直接全部建立  是把參數記錄在物件理  用到才產生 省記憶體

# reversed(li)  是回傳迭代器  所以一次給出一個逆向元素
# sorted 直接排完回傳串列

#zip 滿有趣的  蒐集每個元素的第 0 1 2 個 成為 tuple 組合成 list

# 淺複製  書是寫會別名  所以 == 判斷會 T  但是現在測試 3.7 會 F 可能後來都改成 淺深 都新物件
li = [0,[1,2],2]
li2 = li.copy()
import copy
li3 = copy.copy(li)
li4 = copy.deepcopy(li)

# p135  while + iterator 模擬 for  except 相當 catch  iter 超過就是  StopIteration exception
li = [30, 41, 52]
itb = iter(li)
while True:
    try:
        x = next(itb)
        print(x)
    except StopIteration:
        break
 
 # p137 更清楚的說  2.x 的 range 是 ls    3.x 的 range 就是  Iterable 的抽象型別  所以才不會一次產生  
 # LC 有刷到同概念的題目

# p139  enumerate
# >>> li = ['a','b']
# >>> en = enumerate(li)
# >>> next(en)
# (0, 'a')   # 是 tuple
li = [1,2]
for i, v in enumerate(li):
    print(i, v)

# sorted 傳參版本   sorted(ls, reverse = True)  
# sorted(ls, key=方法)  # 方法 回傳元素 轉換的值 當作排序的依據

#p141   for i in range(len(li))  一邊 del  會造成 index 超出 li exception
#  for i, x in enumerate(li)  一邊 del  會造成迭代下一個會跳到被刪除的下下個
# 書建議不要像上面原地修改  可以建立新串列 或複製  去操作
# 但是這個回答在 LC 是 0 分  效能 和 記憶體  一定過不了要求 LC 一直講求特殊用途的 DS  linkedList DEQueue
# Queue Stack List  C# 用 for i-- 可以輕鬆達成原地刪除  python 這點不知道在幹嘛

def ftoc(ft):
    ct = []
    for x in ft:
        ct.append((x-32)*5/9)
    return ct
#可以簡寫為  串列生成式 
ft = [1,2,3]
ct = [(x-32)* 5/9 for x in ft]   #類似  倒反語法  三原運算子也來來這招
# 有很多變化用法 p143   for 雙層也可以












# p137
def my_sum(iterable, start=0):
    result = start
    for x in iterable:  # !!!
        result += x
    return result
a = ('a', 'b', 'c', 'd')
b = range(1, 10+1)
c = ['abc', 'def', 'gh', 'i']
print(my_sum(a, ''))
print(my_sum(b))
print(my_sum(c, ''))

def product(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result

a = range(1, 10+1)
b = [2, 3, 4, 5]
c = [1.1, 3.5, 5.6]
print(product(a, 0.1))
print(product(b))
print(product(c))


def product(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result

def my_factorial(n):
    return product(range(2, n+1))

from math import factorial
print('6! is ' + str(my_factorial(6)))
print('math.factorial: ' + str(factorial(6)))
print('10! is ' + str(my_factorial(10)))
print('math.factorial: ' + str(factorial(10)))
print('15! is ' + str(my_factorial(15)))
print('math.factorial: ' + str(factorial(15)))

def cumulative_sum(iterable, start=0):
    result = []
    acc = start
    for x in iterable:
        acc += x
        result.append(acc)
    return result

print(cumulative_sum(range(10+1)))
print(cumulative_sum(range(0, 1000, 100)))


def unique(iterable):
    result = []
    for x in iterable:
        if x not in result:
            result.append(x)
    return result

print(unique([1, 2, 1, 3, 2, 5, 5, 6, 1])) # [1, 2, 3, 5, 6]
print(unique([1, 2, 1, 3, 2, 5])) # [1, 2, 3, 5]
print(unique(range(10)))

def duplicate(iterable):
    fst = []
    snd = []
    for x in iterable:
        if x not in fst:
            fst.append(x)
        elif x not in snd:
            snd.append(x)
        else:
            pass
    return snd
        
print(duplicate([1, 2, 6, 1, 3, 2, 5]))
print(duplicate(range(10)))
print(duplicate([1, 1, 3, 1, 3, 3, 1, 2, 1, 5, 2]))


def group(iterable, size):
    result = []
    li = list(iterable)
    length = len(li)
    for i in range(0, length, size):
        result.append(li[i:i+size])
    return result

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
# [[1, 2, 3, 4], [5, 6, 7, 8], [9]]

print(group(range(20), 5))

def flatten(iterable):
    result = []
    for x in iterable:
        result.extend(x)
    return result

print(flatten([[0, 1, 2], [3, 4, 5], [6], [7, 8], [9]]))
print(flatten([[0, 1], [3, 5], [6], [7, 8], [9]]))



