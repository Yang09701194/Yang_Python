print('Hello Python')

a=3.75
a #  在互動模式會印出值  檔案執行不會
print(a)

s = 'hello'

ls = ['ab', 2, 'ef']  # list 是  array list 的概念  可以裝不同型別
print(ls[1])

height = 2
weight = 3
ls2 = [height, weight]
print(ls2[1])
ls2[1] = 5
print(weight) # 還是 3
print(ls2[1]) # 5

b=3
a=b
a=2 # b 不會變  因為 immutable 

# list 的話  就是參考的概念  同 C#  shared reference

#tuple  
tup = (1 ,2, 'a')  # 語法同 list   [ 換成 (
# 內容不可變  不會變   取用 tup[i]
#單元素要加 ,
tup = ('test',)   #沒加會被當成 str
#可簡寫為  
tup = 'a' , 'b', 'c'

d = 17/3 # 2.x:5 3.x 5.66667    2.x > 17.0/3 = 5.6667
d = 17//3 # 地板除法  5    -17//3 = -5.666 > -6
d = 2 **5 # 2^5
17 % -3 // -1 # > x% y = x - (x//y)*y

2 ** 3 ** 2 # 順序例外 先 3 ** 2  再 2 ** 3

'a' + 'b' # ab
'a' * 4 # aaaa

[0, 1, 2] + [2, 3, 4] # add range   tuple 也行
[0, 1, 2] * 3 #[012012012]

# list 的相等是 所有元素相等  C# 是 ref 
lia = [0,1,2]
lib = [0,1,2]
a == b

#list contains  是 in

c = 2
c in lia
c not in lia

d = 'abc'
e = 'abcde'
d in e

# is  判斷是不是指向同一個物件(值  python 裡基礎型別值都被稱為物件)
a = 3
b = 4
c = 1 + 2
c is a # True

ls = [0,1]
ls1 = ls
ls2 = [0,1]
ls2 is ls # False
ls1 is ls # True

0 < 1 and 1<2 # & | !  在 python 用字 and or not 




