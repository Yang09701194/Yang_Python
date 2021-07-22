
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
for k, v in d.items():
    print(k, v)





