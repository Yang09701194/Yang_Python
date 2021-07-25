
# dict
# >>> d= {'name':'Test', 'age': 27}
# >>> d['name']
# 'Test'
# >>> d['name'] = 'T5'
# >>> d
# {'name': 'T5', 'age': 27}
# >>> d['t3']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 't3'

# 值 可以是任何型別  list dict ...
# 鍵 限制不可變物件 str int tuple
d = {'321': (5, 6, 7), (6, 7, 8): '456'}

d = dict(name= (5, 6, 7), id= '456')
keys = [2,3,4]
values = ['kk','nn','cc']
d2 = dict(zip(keys, values))
d3 = dict(d, name=(6,5,4)) # 以 d 為基礎  再修改 name
d4 = dict(zip(range(100, 100+3), ('t1', 't2', 't3')))

len(d)
del d['name'] # remove
d.get('name') # 無 key 回傳 None
d.get('name', 'default') # 無 key 回傳 default
d.setdefault('job') # 無 key 指派 None  有 key 回傳 val
d.setdefault('job', 't2') # 加入 key val

for key in d:
    print(key)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():   #都無固定順序  不同版本 python 電腦 可能都不同  
    print(k, v)   

#set  類  HashSet   裝不可變物件 str tuple str
x = {1,2,3,4,5}
x1 = set([1, (2,3,4), 'test'])
set(range(1, 5+1))

# {} 是空字典   集合不具順序性  不能用 index  x[0]  error
len(x)
1 in x; x.add(5)  
x.remove(7)  # 若不存在會 error
x.discard(7)  # 可以不存在
x & x1 # intersection 交集
# | union 聯集  - difference 差集  ^ symmetric difference 對應差集

x = set([1,1,2,2,3,3])
x == {1,2,3} # true

# 說鍵是 不可變物件  還不夠準確   更準確是 可雜湊者 Hashable   是抽象型別
# 不可變物件都有繼承  都可以取得獨一無二的雜湊值  有內建 hash 函式
# Hash 把資料用某種函式規則  計算出可代表物件的數位指紋
# 但資料無窮  所以可能會有  衝突

from collections import defaultdict
from collections.abc import *
issubclass(int, Hashable)
hash('1'), hash('abc')

#不可變物件  存活期間 內容不變 > hash 不變 > 可做為 key  字典其實是計算物件的 雜湊值  去找出對應的 value
# set 也是存雜湊值  檢查存在 也是用 hasH   
# 不同平台 python ver 的 hash 演算法可能不同

# dict 符合 抽象型別 MutableMapping  #182
# set 符合 抽象型別 Set 定義的介面

#182
# Sized __len__ Container __contains  Iterable __iter__
# Set MappingView Mapping Iterator
# KeysView ItemsView ValuesView Mapping  __getitem__ keys values items get Iterator __next__
#                     MutableMapping __setitem__ __delitem__ pop popitem clear update set defaultdict

#set  len in  it = iter(set)  next(it)   [e for e in set if type(e) is int]
#  191 discard 不存在沒問題  add  remove 不存在 err   pop(e) 空集合err   
# copy 淺複製  clear    a<=b  是否  issubset   >= issuperset
#  > 真超集合 superset  < 真子集 proper set
# isdisjoint 交集為空  union |  聯集   & instersection 交集  - difference 差集
# ^ symmetric_difference 對稱差集  |= update 聯集動作  &= instersection_update
# -= difference_update  ^= symme...
# 上面 x= 是原地修改  不會產生新集合物件   

#dict len in d['key']  d[]=   pop(key) # 移除 並回傳原值 不存在會err 
# pop('key', 'returnDefaultVal')   popitem() 任意 pop   copy() 淺複製
# clear()


#184  dict keys 唯一 所以設計為 Set   values 繼承 Iterable Container 非 Set
#keys values  鍵/值的順序是對應的  所以依序印出會對應

# >>> dict.fromkeys(['a', 'b', 'c'])
# {'a': None, 'b': None, 'c': None}
# >>> dict.fromkeys(['a', 'b', 'c'], 1)
# {'a': 1, 'b': 1, 'c': 1}
d = {'a': 55, 'b': 59, 'c': 65}
{k: v for k, v in d.items() if v < 60}
# {'a': 55, 'b': 59}
li = ['a', 'b', 'c']
{a:i for i,a in enumerate(li, start=101)}
# if else 多個相等值  可以改成 dict 省程式碼  函式也可
def f0(): pass
def f1(): pass
def f2(): pass
d = {'orange': f0, 'banana': f1, 'grape': f2}
x = 'orange'
if x in d:
    d[x]()

# 字串格式化 某鍵 用 (名稱)
data = {'name': 'Amy', 'score': 83, 'age': 33}
'%(name)s is %(age)d years old, score is %(score)d' % data
# 'Amy is 33 years old, score is 83'
'{name:s} is {age:d} years old, score is {score:d}'.format(name='Amy', score=83, age=33)
'{name:s} is {age:d} years old, score is {score:d}'.format(**data)
# ** 是展開

# 195   unique 用 set 很快
def unique(iterable):
    return set(iterable)

# dict  get 不存在 key 會 err 所以常先用 in 判斷  或 setdefault 
# 另有  defaultdict  可以給預設值  不存在key會自動建立 
# 參數是可建立預設值的函式 (或任何可呼叫者) 
d=defaultdict(int)
d['a'] # 0 

# 有順序的 dict
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
# {'name': 'Amy', 'score': 83, 'age': 33, 'a': 1, 'b': 2, 'c': 3}
# >>> d['b'] = 99   # a 順序保持
# >>> d
# {'name': 'Amy', 'score': 83, 'age': 33, 'a': 1, 'b': 99, 'c': 3}
# >>> del d['a']  
# >>> d['a'] = 1   # a重加到尾
# >>> d
# {'name': 'Amy', 'score': 83, 'age': 33, 'b': 99, 'c': 3, 'a': 1}
d.pop() # 預設 True  從尾端拿出 
d.pop(False) # 首拿
d.update([('c', 3)], d=4, e=5)  # 用update 多個參數  就不保證順序維持

#不可變集合  不能 add clear &= 等改變動作  取用同一般 set
frozenset([1,2,3])

# python 會把名稱  存在命名空間裡  實際上就是 存在字典
a=1
b=2
c=3
def foo(x,y):
    a = 'aaa'
    b = 'bbb'
    print(locals())
print(globals())
print('*' * 10)
foo(1,2)
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'key': 204, 'd': {'name': 'Amy', 'score': 83, 'age': 33, 'b': 99, 'c': 3, 'a': 1}, 'x': {1, 2, 3}, 'data': {'name': 'Amy', 'score': 83, 'age': 33}, 'a': 1, 'b': 2, 'c': 3, 'foo': <function foo at 0x00000227BD6FB168>}
# **********
# {'x': 1, 'y': 2, 'a': 'aaa', 'b': 'bbb'}

# 不可變 = 可雜湊  唯一例外是 ch11 自訂類別  可以定義 可辨的型別 又可雜湊  
# 但拿來當dict key 不是好主意？

# 189
d = {'Amy': 45, 'Bob': 50, 'Cathy': 62, 'David': 45,
     'Eason': 63, 'Fred': 78, 'George': 72, 'Helen': 82,
     'Ivan': 100, 'Jason': 98, 'Kevin': 0, 'Laura': 100}

d2 = {v:k for k,v in d.items()}

d3 = {}
for k, v in d.items():
    r = v // 10
    if r not in d3:
        d3[r] = []
        # 改成 defaultdict(list)  就可以省上面兩句
    d3[r].append(k)
print(d3)

#### output: ####
# {0: ['Kevin'], 4: ['David', 'Amy'], 5: ['Bob'], 6: ['Cathy', 'Eason'], 
# 7: ['Fred', 'George'], 8: ['Helen'], 9: ['Jason'], 10: ['Ivan', 'Laura']}

d = {'Amy': (45, 60, 33), 'Bob': (50, 62, 78), 
     'Cathy': (62, 98, 87), 'David': (45, 22, 12),
     'Eason': (63, 55, 71), 'Fred': (78, 79, 32)}

for k in sorted(d.keys()):
    print(k, d[k])

def foo(item):
    return item[1][2] # 根據英文成績排序
for item in sorted(d. items(), key=foo):
    print(item)

def bar(item): # 根據總分排序
    return sum(item[1])
for item in sorted(d.items(), key=bar):
    print(item)


#### generate a set containing prime numbers from 2 to n ####
def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes

#### this is not a good algorithm to check prime numbers ####
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#### powerset, all subsets of a set ####
def powerset(s):
    li = list(s)
    ps = set()
    for n in range(0, 2**len(s)):
        sub = set()
        x = n
        for i in range(len(s)):
            if x & 0x1:
                sub.add(li[i])
            x >>= 1  # 標準 LC 風格考題
        ps.add(frozenset(sub))
    return ps

