
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

# dict 符合 抽象型別 MutableMapping

#182
Sized __len__ Container __contains  Iterable __iter__
Set MappingView Mapping Iterator
KeysView ItemsView ValuesView Mapping  __getitem__ keys values items get Iterator __next__
                    MutableMapping __setitem__ __delitem__ pop popitem clear update set defaultdict

#Set  len in  it = iter(set)  next(it)   [e for e in set if type(e) is int]

