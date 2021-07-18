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
tup = (1 ,2, 'a', [4,5])  # 語法同 list   [ 換成 (
# 內容不可變  不會變   取用 tup[i]
#單元素要加 ,
tup = ('test',)   #沒加會被當成 str
#可簡寫為  
tup = 'a' , 'b', 'c'

d = 17/3 # 2.x:5 3.x 5.66667    2.x > 17.0/3 = 5.6667
d = 17//3 # 地板除法  5    -17//3 = -5.666 > -6
d = 2 **5 # 2^5   但 ^ 程式符號是 xor
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

0 < 1 and 1<2 # && || !  在 python 用字 and or not   &&的效果叫 short circuit

#所有物件都可用於邏輯運算  None 0 '' 空list/tuple  為 False  其他 True
#'0' (0,) 為 True    None 是特別的物件  型別是 NoneType  代表 無  未得到有效值

# x<y and y<=z  可寫為 x<y<=z

# python 可分號結尾  同一行多分號可分句
1+2;3+4;5+6;

a=b=c=3
a=4; c=5;

a,b,c = 0,1,2 # tuple 
a,b = b,a # 交換

x= [0,1]; i=0
i, x[i] = 1,2
x # 得到 0,2

x,y,z = 'abc' # x,y,z = 'a','b','c'

#3.x 星號  可容納不定長度定長度

x= [1,2,3,4,5]
a, *b, c = x # b會是 [2,3,4]   
# *_  底線也是變數名稱  還有一些有趣規則見 p41

# if elif else  都要加 :
#  縮排要完全符合  可四空(建議)  兩空 或 Tab
a, b, c = 3, 5, 7
x = None

if a < b:
    if b < c:
        x = c
    else:
        x = b
else:
    if a < c:
        x = c
    else:
        x = a

x
print(x)

# pass  補句法沒動作的地方
if b < c:
	x = c
else:
	pass


scores = [60, 73, 81, 95, 34]
n = 5
i = 0
total = 0
while i < 5:
    total += scores[i]
    i += 1
avg = total / n
print('total ' + str(total))
print('average ' + str(avg))
 

scores = [60, 73, 81, 95, 34]
n = 0
total = 0
for x in scores:
    n += 1
    total += x

avg = total / n

print('total ' + str(total))
print('average ' + str(avg))
 
names_scores = (('Amy', 82, 90), ('John', 33, 64), ('Zoe', 91, 94))
highs = []
for x, y, z in names_scores:
    if y >= 90 and z >= 90:
        highs += [x, y, z]

print(highs)
 
colors = ['red', 'green', 'blue']
animals = ['cat', 'dog', 'horse', 'sheep']
results = []
for x in colors:
    for y in animals:
        results += [x + ' ' + y]

print(results)
 
scores = (98, 78, 64, 55, 61, 82)
lowerThan60 = False
for x in scores:
    if x < 60:
        lowerThan60 = True
        break  # continue
print(lowerThan60)

#p51
# assert 用在除錯  del 刪除名稱及物件的綁定關係
# return 值 或 None  yield
# raise 引發異常  global 宣告全域範圍
# 2.x exec 動態執行 python 語句   3.x nonlocal 宣告名稱在函式外
# try    with  把一組程式句包起來  由文脈管理器負責進入語離開的狀況
# def  函式  class


def my_sum(numbers, initial=0):
    total = initial
    for x in numbers:
        total += x
    return total

scores0 = [60, 73, 81, 95, 34]
scores1 = [10, 20, 30, 40, 50, 60]
scores2 = [0, 0, 0]
print(str(scores0) + ' total is ' + str(my_sum(scores0)))
print(str(scores1) + ' total is ' + str(my_sum(scores1)))

def total_avg(scores, initial=0):
    n = 0
    total = initial
    for x in scores:
        total += x
        n += 1
    return (total, total/n) # 可以回傳複雜類型
	
# 如果沒有 return  回傳 None

# 一旦沒有任何名稱指向某物件 就會被 GC    del 可以手動刪除 名稱 和指向物件的綁定
# 刪除後無法再使用

#  名稱 (變數) 的可視範圍 scope  global local 概念同 C#
# 比較特別  方法內部如果名稱和全域同   預設是會變成一個 local  如果想要操控外部全域的銅名稱 用global 宣告  global a; a= 100 global 找不到 會找 local 

a = []
len(a) # length
sum(a)
sum(a, 1000) # 1000 + sum(a)
max(a), min(a)  # 附錄A有完整內建函式列表
range(3) # [123]
range(2,4) # 234
range(1,10,2) # 1 3 5 7 9

li = [30,41,52]
for i in range(len(i)):
  li[i] += 100

# abs() pow() round()  divmod() all() any() id() type() callable()
# 2.x 有分 type class  3.x  全部都 class  
# function 也 class 且是可呼叫的  所以 callable(f) 是 true

# 基礎型別都有建構式
int(4.5) # 4
float(-4.5) # -4.5
a = list((1,2)) # list(tuple)也行   有複製的效果
tuple([1,2])# 同上

#bool(a) 得知 T F

#str(a)  有點類似 print 會得到的字串  repr()  很類似 但可當成程式碼給 interpreter 執行

# 2.x  print (0,1,2) 是述句  不是函式 用法奇特  p60

# 3.x  print 功能很多  可加 sep 分隔符號 end 結尾字串
#讀 inpout
# a = input('Your Name: ')
# 輸入 Ken  會得到  Your Name: Ken

#python 也有 eval()
