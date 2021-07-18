

#  .pyc  是位元組 byte code 檔  蘇然理論上直譯器 會一行行的執行  
# 但實際上彙編把原始碼編譯成位元組檔 提升執行速度
# 有可能放在原始碼資料夾  或  __pycahce__
# .pyo 開啟效能最佳化   編譯的 byte code


# 標示程式檔的 編碼
# -*- coding: utf-8 -*-
# ascii latin-1 iso-8895-1 big5
# 要搭配 編輯器存檔時  也要選擇正確的編碼
 

# Linux MacOS Cygwin 可以用 #! 放程式第一行  os可知用哪個程式執行
# #!/usr/bin/env python   
# 然後更改檔案屬性加上可執行  就可當一般指令執行  不用加 "pyhton 檔名"
# chmod +x hello.py

# a=b=c =[1,2]
# b = b+[3,4] # b 會變成新的 ls
# c += [3,4] # 還是 c 叫原地修改
# a is c T  a is b F

# 為什麼  用 名稱+物件  不用變數的概念  dynamic typing p73
# 3.x 才可以用 unicode  中日文字命名
# exec 可以執行程式碼
# None 是 型別 NoneType 的惟一值


# for 可以搭配 else  如果  for 裡面沒有 break 完整執行完  就會執行 else
names_scores = (('Amy', 82, 90), ('John', 33, 64), ('Zoe', 91, 94))
b = False
for x, y, z in names_scores:
    if y >= 90 and z >= 90:
        b = True
        break
else:
    b = False


# ch3 82

# 2.x 的整數 是 int 超過自動轉 long  印出時尾巴會加上 L
# 3.x 只有 int 變無窮精確度  只要記憶體購 都能表示

# 二進位  16進位  8 進位
# 0b1100100, 0x64, 0O144
# (100, 100, 100)

# bin(100), hex(100), oct(100)
# (0b1100100, 0x64, 0O144)
# int(0b1100100) # 100
# int('99', 10) # 10進位    各種測試 p84

# 福點數  除小數點表示  也可科學記號
3e2 # 3 * 10^2
# float()  和 int() 類似

float('nan')  # 非數字
float('inf') # 正無限大
float('-inf') # 負無限大

# round()  不是真的 四捨五入  浮點數如果有小誤差   
# round(2.675, 2)  因為二進位無法準確表示 變 2.674... 所以扁 2.67 
# 遇到中間  2.x 是 away from zero    round(2.5) round(-2.5) > 3 -3
# 3.x是 to even 靠向偶數  round(2.5) round(-2.5) > 2 -2

# math.trunc 跟 // 正數效果相同   負數  -17//3 是 -6  math.trunc(-17/3) = -5

#  ? :  
#  x if y > 0 else z 
#  y > 0 ? x : z
#  語法糖 (syntactic sugar)
#  (y > 0 and x) or z

#  li.append(3)  > li + 3
# tuple 是不可變物件  不能附加元素  但是兩 tuple 可相加

# p93 複數 complex
# 型別 complex   由實部  虛部  real part + imaginary part  皆為 浮點數  虛部加上 j
z = (3.1+4.5j)
complex(3 + 2j) 
z.real # 實部
z.imag # 虛部  是數字  不帶 j 
z.conjugate() # 共軛複數

import cmath
import fractions # 有 complex 型別的相關函式  如直角坐標系(笛卡兒座標系) 和 極坐標系 的轉換
x = 4+5j; y = 6+7j;
abs(x) # 絕對值 模
cmath.phase(x) # 幅角 弧度
ct = cmath.polar() # 有模與幅角的 tuple
cmath.rect(ct[0], ct[1])
cmath.sqrt(-1)
#exp log log10 acos asin acosh asinh

# 數字 + 字串  不會自動轉換
# 每個物件都有 .__str__() 方法   print() 時就會調用
# __repr__ 差別在回傳的字串可以當程式碼  餵給直譯器   可以執行

# p97  Decimal  這邊是真的十進位  float 會友精確度的差異  不完全等於真的值
# 跟金錢貨幣 相關的銀行財務部門 適合用  
import decimal
a = decimal(0.1)  # 因為傳入 float  所以建立起來還是 float 不准
b = decimal('0.1') # 用字串表示  就會是真的 '0.1'  計算就會維持正確的 有效數字
b = a * a + a
# decimal 也提供 sqrt  explog10  四捨五入用  quantize
# decimal 還有算術環境 可以設定精確度 捨入規則 指數限制
decimal.getcontext()
#Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1,
#  clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
# 這些都可以屬性設定

# p100 分數 Fraction 有理數
from fractions import *
a = Fraction(1,3) # 1/3
#用法詳見 100
a.limit_denominator(100)  #  限定分母最大值  預設六位數  100 可限制到兩位數
# F(...).limit_denominator() # 找出無窮小樹的 近似分數


# pyhton 用 二補述表示法   11111 是 -1 單個 0  二進位相關概念  p103

# 位元運算子  ~ : not   << >>  &  ^ : xor  | 

# +=  >>>>   <<= >>=  &= 

