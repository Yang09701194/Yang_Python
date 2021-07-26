
# >>> type(len)
# <class 'builtin_function_or_method'>
# >>> def foo():pass
# >>> type(foo)
# <class 'function'>
# callable(foo) # true
# callable(int) # true  建構式也是 可被呼叫者

# 方法呼叫的 () 直譯器會轉為 __call__
from _typeshed import NoneType, OpenTextModeReading


def square(x,y): return x**2 + y**2
def square(x,y=2): return x**2 + y**2

a=3
def test(x=a):print(x)
test()
a=13
test() # x 只賦值一次 還是 3

#但 x = [] 是可變物件  就會跟著變
#解法是None  沒有指定參數的時候
def foo(x, y=None):
    if y is None: # 不能 if y:  因 False 空串列 也是 False
        y = []
    y.append(x)
    print(y)
foo(1)
foo(2)
foo(3, [90,91])

# 無名函式
sq = lambda x : x**2 # sq 是 function
(lambda : print('Hello'))() # 立刻執行
(lambda x, y: x if x > y else y)(3, 4)

#lambda x: return x;  err return 是 述句 不是運算式 運算式只能有一個

# lambda 好用之一 是可以傳給 sport
li = [('apple', 25), ('orange', 10), ('fig', 12), ('apricot', 20)]
def by_name(item):
    return item[0]
def by_name_len(item):
    return len(item[0])
def by_value(item):
    return item[1]
print(sorted(li, key=by_name))
print(sorted(li, key=by_name_len))
print(sorted(li, key=by_value))
####  ####
#[('apple', 25), ('apricot', 20), ('fig', 12), ('orange', 10)]
#[('fig', 12), ('apple', 25), ('orange', 10), ('apricot', 20)]
#[('orange', 10), ('fig', 12), ('apricot', 20), ('apple', 25)]
print(sorted(li, key=lambda item: item[0]))
print(sorted(li, key=lambda item: len(item[0])))
print(sorted(li, key=lambda item: item[1]))

# 函式的參數  傳入後使用 要小心原地修改  list.append(3) 就是

# 參數  有加 * 則額外的參數 都會放進這個 tuple
# 參數  有加 ** 則額外的參數 都會放進這個 dict   3.x 版不用最後一個
# 只有 * 沒有寫參數名稱  沒效果

def f(**d): print(d)
# f(1,2,3)  err 不能接位置參數  223
f(k1='a', k2='b')
# {'k1': 'a', 'k2': 'b'}

#  *t **e  可以混用

# 上面是形式參數 加上*   實際呼叫時 *加在 iter 會解開變成一串參數  而不是單個list
# ** 可以解開 dict 的值變成一串參數

# 開頭就是 * 表示後面我有參數都要用  關鍵字指定參數的方式 f(*, red, green, blue)
# 這種形式  可以接受 **dict的語法 key=value 展開

# 可視範圍 scope 分為 builtin global local  詳解 231
# 名稱第一次被指派的地方  名稱就在那個 scope
y = 999
def f(x):
    print(y) # 會錯  因為 y 被視為 local y 還沒賦值  如果 global y 會取全域
    y = x + 10

# scope 的概念  可以推廣到  直譯器 環境  多個命名空間  237
# LEGB (Local Enclosing Global Builtin)


def fact_i(n):  # 迭代形式
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
####
def fact_r(n): # 遞迴形式
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_r(n-1)

def gcd_i(a, b):
    while b:
        a, b = b, a%b
    return a
####
def gcd_r(a, b):
    if b == 0:
        return a
    else:
        return gcd_r(b, a%b)


# 257  回傳函式的函式  高階函式  higher-order-function
# 263  延遲綁定  C# javascrip 都有遇過  就是 for i 1~n 加入函式跟i有關
# 最後調用  所有的函式都用 n
def make_multipliers():
    result = []
    for i in range(3):
        m = lambda x: i*x
        result.append(m)
    return result
for m in make_multipliers():
    print(m(5))   # 3 個 10

#改寫
#m = lambda x, y=i: i*x  就可以印出 0 5 10

# nonlocal 多個閉包可以互相影響對方
def foo():
    n = 0;
    def bar(x):
        nonlocal n
        n += 1  # 影響之處
        return n * x
    li = [bar, bar, bar]
    return li
a,b,c = foo()

# 目前學的  還無法寫出一個可以在 for 等地方用的迭代器  例如自己寫 range
# 靠 def 還不夠 要 ch11 學繼承  自訂類別
# 但是 yield 可以快速建立 符合可迭代的物件
def f(end):
    start = 0
    while start < end:
        yield start
        start += 1
g = f(3)
type(g)
# <class 'generator'>
from collections.abc import *
issubclass(type(g), Iterable)
# True
next(g), next(g), next(g)
# (0, 1, 2)

# 碰到 yield 產生器的狀態會被凍結保存  記住 start end 等值 
# 然後把 yield 後的 start 交給呼叫方  
# 所以可以拿來實作 range

def range_g(start, end=None, inc=None):
    if end is None:
        end = start
        start = 0
    if inc is None:
        inc = 1
    while True:
        if inc > 0 and start >= end:
            break
        elif inc < 0 and start <= end:
            break
        yield start
        start += inc

def range2x(start, end=None, inc=None):
    if end is None:
        end = start
        start = 0
    if inc is None:
        inc = 1
    result = []
    while True:
        if inc > 0 and start >= end:
            break
        elif inc < 0 and start <= end:
            break
        result.append(start)
        start += inc
    return result

# not work
def range3x(start, end=None, inc=None):
    if end is None:
        end = start
        start = 0
    if inc is None:
        inc = 1
    s = [start]
    def sub():
        while s[0] < end:
            if inc > 0 and s[0] >= end:
                break
            elif inc < 0 and s[0] <= end:
                break
            s[0] += inc
            return (s[0] - inc)
    return sub

if __name__ == '__main__':
    tests = (0, 10, 30, -100, 1, 2)
    for a in tests:
        x0 = list(range(a))
        x1 = range2x(a)
        x2 = list(range_g(a))
        if x0 != x1 or x0 != x2:
            print('error')
    tests = ((0, 10), (10, 30), (-100, 20), (1, 2))
    for a,b in tests:
        x0 = list(range(a, b))
        x1 = range2x(a, b)
        x2 = list(range_g(a, b))
        if x0 != x1 or x0 != x2:
            print('error')
    tests = ((0, 10, 1), (10, 30, 2), (-10, -20, -1), (0, -31, -3))
    for a,b,c in tests:
        x0 = list(range(a, b, c))
        x1 = range2x(a, b, c)
        x2 = list(range_g(a, b, c))
        if x0 != x1 or x0 != x2:
            print('error %s %s' % (x0, x1))
    # xx = range3x(10, -3, -1)
    # for i in range(20):
        # print(xx())

# 產生器運運式
(i**2 for i in range(3)) # 可以再加 if 過濾條件  

sum((i**2 for i in range(3)))
sum(i**2 for i in range(3))
sum([i**2 for i in range(3)])

# yield 一個特性  就是不用預先取得全部   可以用到的時候才取
# 就像看影片  不適全部載入記憶體  可能會爆  而是觀看到的地方才下載
# 八個皇后  一開始寫的是取全部  也可以改成 yield 版本
# 另一個特性  式可以做到無窮  而只用少量記憶體

def int_from(n, increment=1):
    while True:
        yield n
        n += increment
y = int_from(5,2)
next(y)

# 271 yield from 
def sub_fg(n):
    i = 1 if n >0 else -1
    inc = i
    while i  != n:
        yield i
        i += inc
def fg(n):
    yield from sub_fg(n)
    yield from sub_fg(-n)
print(list(fg(5))) # 1 2 3 4 -1 -2 -3- 4

# 產生器協定  呼叫方可以用 send 傳參數 成為 yield 的結果   相當於影響 yield 的結果  或順序
# 還支援 在最近的 yield 引發異常 throw   close() 引發特別異常  GeneratorExit()
def gf():
    n = 0
    while True:
        from_send = yield n
        n +=1 if from_send is None else from_send
g = gf()
print(next(g))
print(g.send(3)) # 3
print(g.send(5)) # 8

# 可迭代者  本身不是迭代器  重新取 iter 可以取到從頭開始的 
ls = [1, 2, 3]
g = iter(ls)
h = iter(ls)
next(g); next(g); next(g); # 1 2 3
next(h) # 1
y = iter(g)
next(y)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
y = iter(h)
next(y) # 2
x = z = e = y # 淺複製 其實都是指向同個物件 

# 內建  object 建構式  可建立一個獨一無二的參數值
_default_value_ = object()
def foo(x, y, z = _default_value_):
    if z is _default_value_ : pass





# 250

from itertools import permutations
p = permutations

def perm(iterable, r=None):
    items = tuple(iterable)
    r = len(items) if r is None else r
    answers = []
    def sub(items, k, p):
        if k == 0:
            answers.append(p)
        else:
            # for i in range(k): # wrong
            for i in range(len(items)):
                # sub(list_del(items, i), k-1, p+(items[i],))
                sub(items[:i] + items[i+1:], k-1, p+(items[i],))
    sub(items, r, ())
    return answers

if __name__ == '__main__':
    tests = (list(range(3)), ['a','b','c','d'], list(range(100, 106)))
    for t in tests:
        pa = list(p(t))
        pb = perm(t)
        if set(pa) == set(pb):
            print('yes')
        else:
            print('no')
    for t in tests:
        for r in range(1, len(t)):
            pa = list(p(t, r))
            pb = perm(t, r)
            if set(pa) == set(pb):
                print('yes')
            else:
                print('no')



def powerset(s):
    li = list(s)
    ps = set()
    for n in range(0, 2**len(s)):
        sub = set()
        x = n
        for i in range(len(s)):
            if x & 0x1:
                sub.add(li[i])
            x >>= 1
        ps.add(frozenset(sub))
    return ps
####

def powerset_r(iterable):
    def set_add(ps, item):
        if len(ps) == 0:
            return []
        else:
            return [ps[0] + [item]] + set_add(ps[1:], item)
    def sub(s):
        if len(s) == 1:
            return [s, []]
        else:
            ps = sub(s[1:])
            return ps + set_add(ps, s[0])
    return sub(list(iterable))

test = [1,2,3,4]
print(powerset(test))
print(sorted(powerset_r(test), key=lambda x: len(x)))


def fib_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_r(n-1) + fib_r(n-2)
####
def fib_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
####
memo = {0: 0, 1: 1}
def fib_m(n):
    if n not in memo:
        memo[n] = fib_m(n-1) + fib_m(n-2)
    return memo[n]

for x in range(20):
    fr = fib_r(x)
    fi = fib_i(x)
    fm = fib_m(x)
    if fr != fi or fi != fm:
        print('error: fib(%d) %d %d %d' % (x, fr, fi, fm))



def hanoi(n):
    steps = []
    def sub(n, pfrom, pto, pbuf):
        if n == 1:
            steps.append((pfrom, pto))
        else:
            sub(n-1, pfrom, pbuf, pto)
            steps.append((pfrom, pto))
            sub(n-1, pbuf, pto, pfrom)
    sub(n, 'A', 'C', 'B')
    return steps

steps = hanoi(3)
print(steps)

def simulate_hanoi(n, pfrom, pto, pbuf, steps):
    pillars = {pfrom: list(range(n)), pto: [], pbuf: []}
    for s in steps:
        disk = pillars[s[0]].pop()
        pillars[s[1]].append(disk)
    print(pillars[pfrom])
    print(pillars[pto])
    print(pillars[pbuf])
    if (pillars[pfrom] == [] and
        pillars[pbuf] == [] and
        pillars[pto] == list(range(n))):
        return True
    else:
        return False

print(simulate_hanoi(3, 'A', 'C', 'B', steps))



def queen(n):
    answers = []

    def is_safe(ans, col):
        for i, c in enumerate(ans):
            if len(ans)-i == abs(c-col):
                return False
        return True

    def sub(ans, n):
        if len(ans) == n:
            answers.append(ans)
        else:
            for col in range(n):
                if col not in ans and is_safe(ans, col):
                    sub(ans + (col,), n)

    sub((), n)
    return answers


# Raymond Hettingers
# http://code.activestate.com/recipes/576647/
from itertools import permutations

def queen(n):
    answers = []
    cols = range(n)
    for ans in permutations(cols):
        if (n ==
            len(set([ans[i]+i for i in cols])) ==
            len(set([ans[i]-i for i in cols]))):
            answers.append(ans)
    return answers

# Steve Howell
# http://wiki.python.org/moin/SimplePrograms

def queen(n):
    answers = [()]

    def under_attack(col, ans):
        return (col in ans or
               any([abs(col - x) == len(ans)-i
                   for i,x in enumerate(ans)]))

    for row in range(n):
        answers = [ans + (col,)
                    for ans in answers
                    for col in range(n)
                    if not under_attack(col, ans)]
    return answers




def sum_number(start, end):
    result = 0
    while start <= end:
        result += start
        start += 1
    return result

def sum_square(start, end):
    result = 0
    while start <= end:
        result += start**2
        start += 1
    return result

# pi/8
def sum_pi(start, end):
    result = 0
    while start <= end:
        result += 1.0 / (start * (start+2))
        start += 4
    return result

def sum_hf(item, start, next, end):
    result = 0
    while start <= end:
        result += item(start)
        start = next(start)
    return result


def sum_number_r(start, end):
    if start > end:
        return 0
    else:
        return start + sum_number_r(start+1, end)
def sum_square_r(start, end):
    if start > end:
        return 0
    else:
        return start**2 + sum_square_r(start+1, end)
def sum_pi_r(start, end):
    if start > end:
        return 0
    else:
        return (1.0 / (start * (start+2))) + sum_pi_r(start+4, end)

def sum_hf_r(item, start, next, end):
    if start > end:
        return 0
    else:
        return item(start) + sum_hf_r(item, next(start), next, end)

if __name__ == '__main__':
    tests = [(0, 10), (100, 200), (2000, 2500)]
    for t in tests:
        fa = sum(range(t[0], t[1]+1))
        fb = sum_number(t[0], t[1])
        fc = sum_hf(lambda x: x, t[0], lambda i: i+1, t[1])
        fd = sum_number_r(t[0], t[1])
        fe = sum_hf_r(lambda x: x, t[0], lambda i: i+1, t[1])
        if fa == fb == fc == fd == fe:
            print('pass')
    for t in tests:
        fa = sum([x**2 for x in range(t[0], t[1]+1)])
        fb = sum_square(t[0], t[1])
        fc = sum_hf(lambda x: x**2, t[0], lambda i: i+1, t[1])
        fd = sum_square_r(t[0], t[1])
        fe = sum_hf_r(lambda x: x**2, t[0], lambda i: i+1, t[1])
        if fa == fb == fc == fd == fe:
            print('pass')
    for end in range(200, 205):
        print(sum_pi(1, end) * 8)
        print(sum_pi_r(1, end) * 8)
        print(sum_hf(lambda x: 1.0 / (x * (x+2)), 1, lambda i: i+4, end) * 8)
        print(sum_hf_r(lambda x: 1.0 / (x * (x+2)), 1, lambda i: i+4, end) * 8)
        print('---')




# not work
# def counter(n):
    # def bar(x):
        # n += x
        # return n
    # return bar

def counter(n):
    def bar(x):
        nonlocal n
        n += x
        return n
    return bar

c0 = counter(0)
c100 = counter(100)
print(c0(1))
print(c100(10))
print(c0(1))
print(c0(3))
print(c100(20))



# Raymond Hettingers
# http://code.activestate.com/recipes/576647/
from itertools import permutations

def queen_gf(n):
    cols = range(n)
    for ans in permutations(cols):
        if (n == len(set(ans[i]+i for i in cols)) ==
                len(set(ans[i]-i for i in cols))):
            yield ans



def fib_gf():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
fib_g = fib_gf()

def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo: 
            memo[n] = sub(n-1) + sub(n-2) 
        return memo[n]
    return sub
fib_m = fib_memo()

for x in range(40):
    fg = next(fib_g)
    fm = fib_m(x)
    if fg != fm:
        print('error: fib(%d) %d %d' % (x, fg, fm))

