

# list 如果只用 append pop 就可當  stack  LIFO
# 只從尾端放  頭端取  可當 queue  FIFO
# list<list>  可當 tree

# named tuple 可以取名字 建構式  
# namedtuple(typename, field_names, verbose=False, rename=False)
from collections import deque, namedtuple
from time import perf_counter, process_time
Point = namedtuple('Point', ['x', 'y', 'z'])
pa = Point(1,2,3)
Point(x=1, y=2, z=3)
pa[0],pa[1],pa[2] # (1, 2, 3)
pa.x, pa.y,pa.z #   (1, 2, 3)

#namedtuple 是  tuple 和 Sequence 類別
Color = namedtuple('Color', 'red green blue')
c_red = Color(red=1.0, green=0, blue=0)
Person = namedtuple('Rec', 'name, age, titles')
bob = Person(name='Bob', age=40, titles=['teacher', 'manager'])
# 具名群組  csv 可以把表頭欄位轉成  namedtuple 就可以輕鬆用屬性存取資料
from __future__ import print_function
from io import open 
from collections import namedtuple
import csv

with open('csv.txt', 'r', encoding='ascii') as fin:
    csvreader = csv.reader(fin, delimiter=',')
    header = next(csvreader)
    Data = namedtuple('Header', ','.join(header))
    for row in csvreader:
        d = Data._make(row)
        print(d.name, d.eng, d.history, d.math)

# 347 deque 
from collections import deque
d = deque()
d.append(1)
d.extend([3,5,7,9]) # 1 3 5 7 9
d.pop() # 9
d.popleft() # 1
d.reverse()
d # 7 5 3
# rotate 循環位移  remove appendleft extendleft  maxlen in len
ls = 1,2,3,4,5,6
deque(ls, maxlen=3) # deque([4, 5, 6], maxlen=3)

# Counter 計數器  是 dict 子型別  可計算補雜湊者  鍵是項目 值是共幾個
from collections import Counter
Counter('hello') # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
Counter([1,2,3,4,3,1])  # Counter({1: 2, 3: 2, 2: 1, 4: 1})
# >>> c=Counter({'miss': 54, 'hit': 33})
# >>> c['hit']  # 不存在 得 0
# 33
# >>> del c['hit']
# >>> c
# Counter({'miss': 54})
# elements most_common(3) 最多的三組   c2-c 只會留 >0 的  subtract 複數也保留

c1=Counter({1: 2, 3: 2})
c2=Counter({1: 2, 3:1})
c1 - c2 # Counter({3: 1})

from collections import Counter
from io import open
with open('i_have_a_dream.txt', 'r', encoding='ascii') as fin:
    c = Counter()
#計算一篇文章的單字數量  用 update 
    for line in fin:
        if line[0] == '#':
            continue
        c.update(line.split())
    print(sorted(c.items(), key=lambda x: x[1]))
    
# heap queue 堆積佇列 351  min heap max heap
# remove insert 可能會連動其他元素移動以保持順序
import heapq # min heap 實作
h= [19,17,11,12,13,16,15]
heapq.heapify(h)
h
# [11, 12, 15, 17, 13, 16, 19]
heapq.heappush(h, 18)
heapq.heappop(h)
heapq.heappushpop(h, 14) # 放 14  拿出最小
heapq.heapreplace(h,20) #  拿出最小 放 20 比上面快
# merge nlargest nsmallest 
# heapq 最小的特性  為基礎  可以寫出 priority queue

# ChainMap 可把多個 dict 鏈在一起 key 重複時  取第一個找到的  更新也是
from collections import ChainMap
d1={'a': 3, 'b':4}
d2={'b': 3, 'c':5}
cm =ChainMap(d1, d2)
# 特別適合紀錄有前後順序階層式關係   例如 全域名稱 local 
# 可以建立多層  new_child  parents  
# dict update 真的有唯一鍵的更新效果

# array  類似串列  元素單一型別 所以大小型型別固定  宣告時指定 所以效能好 354  
from array import array
a = array('i', [3,13, 68])
a.typecode
a.tobytes()
# 索引 切片 迭代  extend index insert pop  
a.frombytes()
a.fromfile()
a.fromlist()

#  ch9  p360  
#  遞迴間接呼叫  不是直接自己呼叫自己
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
def is_even(n): # n 是不是 even 等同  n-1 是不是 odd
    if n == 0:
        return True
    else:
        return is_odd(n-1)

# 標準 cs 的運算樹  括號包括號 的  父子層關係  就可以用樹柱結構表示
# 就可以用遞迴運算
tree_a = ['-', 4, 1]
tree_b = ['/', 10, 2]
tree_c = ['+', tree_a, tree_b]
tree_d = ['+', 3, tree_c]
tree_e = ['-', 4, 2]
tree_f = ['*', tree_e, tree_d]
import operator
ops = {'+': operator.add, # 加號的運算方法
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.floordiv}
def cal(tree):
    if type(tree) == int:
        return tree
    else:
        return ops[tree[0]](cal(tree[1]), cal(tree[2]))
print(cal(tree_f))
# 上面是二元樹  如括號有多個運算元  就要用多元樹  用到兩部分間接遞迴
tree_a = ['-', 6, 2]
tree_b = ['/', 10, 2]
tree_c = ['+', 3, tree_a, tree_b]
tree_d = ['-', 5, 2, 1]
tree_e = ['*', tree_d, tree_c]
import operator
ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.floordiv}
def cal_tree(tree):
    if type(tree) == int:
        return tree
    else:
        return cal_forest(tree[1:], tree[0])
def cal_forest(forest, op):
    if len(forest) == 2:
        return ops[op](cal_tree(forest[0]), cal_tree(forest[1]))
    else:
        hsr = cal_forest(forest[:-1], op)
        return ops[op](hsr, cal_tree(forest[-1]))
print(cal_tree(tree_e))
# 用遞迴寫迭代  
def my_sum(li):
    if li == []:
        return 0
    else:
        return li[0] + my_sum(li[1:])
def gcd_r(a,b):
    if a%b == 0:
        return b
    else:
        return gcd_r(a%b)

# 遞迴深度
# 每增加一層  就會多一層命名空間  
import sys
sys.getrecursionlimit() # 1000 cpu mem 有限  預設最多 1000


# 湊硬幣 用遞迴解  數字大的時候  容易超過最大深度
# Problem 31: Coin sums
# https://projecteuler.net/problem=31

# dynamic programming
def coin_sum(total, coins):
    ways = [1] + ([0] * total)
    for coin in coins:
        for i in range(coin, total+1):
            ways[i] += ways[i - coin]
    return ways[total]
    
def coin_sum_r(total, coins):
    if len(coins) == 1:
        return 1
    elif total < coins[-1]:
        return coin_sum_r(total, coins[:-1])
    else:
        return (coin_sum_r(total-coins[-1], coins) + 
                coin_sum_r(total, coins[:-1]))

# coins_a = (1, 5, 10, 25)   
# print(coin_sum(100, coins_a))   # 242

# coins_b = (1, 5, 10, 25, 50, 100)  
# print(coin_sum(100000, coins_b))   # 13398445413854501

coins_england = (1, 2, 5, 10, 20, 50, 100, 200)
# print(coin_sum(100, coins_england))   # 73682
# print(coin_sum(600, coins_england))   # 73682
# print(coin_sum_r(600, coins_england))   # 73682

coins_x = (1, 2)
for i in range(1, 12+1):
    print(coin_sum(i, coins_x)) 

# 改成 dp 就可以便迭代  迴圈  p365
def coin_sum(total, coins):
    ways = [1] + ([0] * total)
    for coin in coins:
        for i in range(coin, total + 1):
            ways[i] += ways[i - coin]
    return ways[total]

# 尾呼叫 Tail Call 
def fact_r(n):
    if n == 1 or n==0:
        return 1;
    else:
        return n * fact_r(n - 1) # 這種寫法 這邊要等待 fact_r 遞迴的最終結果才能計算

def fact_r_tail(n, result = 1):
    if n == 1 or n==0:
        return result;
    else:
        return fact_r_tail(n-1, n*result) # 其實等同這樣的的寫法  每次都直接知道結果
        # 所以其實可以不用累積一直每層遞迴都開記憶體  當下這層就知道結果  只需一層
        # 程式語言  如果有時做尾呼叫最佳化  tail call optimization  會視為特殊狀況 
        # 不會產生一堆遞迴  和命名空間執行資訊 遞迴深度問題

# decorator 裝飾器  本身也是可被呼叫物件  裝飾另一個韓式或類別定義 ch12

# @decorator
# def f(...)
# 等同# 
# def f(...)
# decorator(f)
def dec_memo(func):  # 370 特徵  傳入函式  回傳函式  中間對傳入的韓式呼叫額外處理
    cache = func.cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@dec_memo
def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)

def fib_r2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r2(n-1) + fib_r2(n-2)

def dec_time(func):
    def wrapper(*args, **kwargs):
        import time
        t_start = time.clock()   
        res = func(*args, **kwargs)
        t_end = time.clock()  
        print(func.__name__, t_end-t_start)
        return res
    return wrapper
@dec_time
def foo1():
    for i in range(6000):
        fib_r(i)
@dec_time
def foo2():
    for i in range(33):
        fib_r2(i)
        
foo1()
foo2()

# 368 
def dec_natural(func): # 是自然數才執行  有點像是 mvc 的前端檢查屬性標籤
    def wrapper(n):
        if type(n) == int and n >= 0:
            return func(n)
        else:
            raise TypeError('Argument is not a natural number')
    return wrapper

@dec_natural
def fact_i(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
print(fact_i(3))

# 369  time 模組 clock()  unix 回傳 int秒  windows float秒
# 另有計算函式執行時間  兩次呼叫的差值
# perf_counter 睡覺也算  process_time  真正執行時間 沒有算睡眠







# 369  厲害 外掛計算效能時間
def dec_time(func):
    def wrapper(*args, **kwargs):
        import time
        t_start = time.clock()
        res = func(*args, **kwargs)
        t_end = time.clock()
        print(func.__name__, t_end-t_start)
        return res
    return wrapper

def fact_i(n):
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

@dec_time
def foo(n):
    for i in range(n):
        fact_i(i)
foo(1000)





# 371 
import pickle
def dec_memo_limit(func, limit=None):
    if isinstance(func, int):
        def wrapper(f):
            return dec_memo_limit(f, func)
        return wrapper

    d = {}
    li = []
    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, kwargs))
        try:
            li.append(li.pop(li.index(key)))
        except ValueError:
            d[key] = func(*args, **kwargs)
            li.append(key)
            if limit is not None and len(li) > limit:
                del d[li.pop(0)]
        return d[key]

    wrapper._memoize_dict = d
    wrapper._memoize_list = li
    wrapper._memoize_limit = limit
    wrapper._memoize_origfunc = func
    wrapper.__name__ = func.__name__
    return wrapper

@dec_memo_limit(200)
def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)
print(fib_r._memoize_limit)

@dec_memo_limit(100)
def fib_r2(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r2(n-1) + fib_r2(n-2)
print(fib_r2._memoize_limit)

def dec_time(func):
    def wrapper(*args, **kwargs):
        import time
        t_start = time.clock()   
        res = func(*args, **kwargs)
        t_end = time.clock()  
        print(func.__name__, t_end-t_start)
        return res
    return wrapper
@dec_time
def foo1():
    for i in range(1000):
        fib_r(i)
@dec_time
def foo2():
    for i in range(1000):
        fib_r2(i)

foo1()
foo2()

import functools
@functools.lru_cache(maxsize=100)
def fib_r3(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r3(n-1) + fib_r3(n-2)

@dec_time
def foo3():
    for i in range(1000):
        fib_r3(i)
foo3()

# @functools.lru_cache(maxsize=300)
# def bar(li):
    # return sum(li)

# print(bar([1,2,3]))
# print(bar([22,22,22]))

@dec_memo_limit
def fib_r4(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r4(n-1) + fib_r4(n-2)
print(fib_r4)


#  367  CPython 無 tail call optim  了解 so4j14uv4,ur6kd3u3y4ur3,uv3
def fact_i(n):
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result
####
def fact_r(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_r(n-1)
####
def fact_r_tail(n, result=1):
    if n == 1 or n == 0:
        return result
    else:
        return fact_r_tail(n-1, n*result)
####

import sys

class TailRecurseException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if (f.f_back and f.f_back.f_back and
             f.f_back.f_back.f_code == f.f_code):
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    return func

# @tail_call_optimized
# def fact_tco(n, result=1):
    # if n == 1 or n == 0:
        # return result
    # else:
        # return fact_tco(n-1, n*result)
def fact_tco(n, result=1):
    if n == 1 or n == 0:
        return result
    else:
        return fact_tco(n-1, n*result)

fact_tco = tail_call_optimized(fact_tco)

for i in range(2, 50):
    x = fact_i(i)
    y = fact_r(i)
    z = fact_r_tail(i)
    w = fact_tco(i)
    if x == y == z == w:
        pass
    else:
        print('error')

# print(fact_i(980))
sys.setrecursionlimit(2000)
print(fact_r_tail(1000))
sys.setrecursionlimit(100)
print(fact_tco(1000))
for i in range(1000, 1050, 3):
    x = fact_i(i)
    w = fact_tco(i)
    if x == w:
        pass
    else:
        print('error')



