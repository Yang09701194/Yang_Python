

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
