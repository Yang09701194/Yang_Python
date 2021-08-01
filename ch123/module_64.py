
# 書是建議  模組名稱都小寫  沒有特別原因

from mymath import * # 可以把 mymath 裡面的名稱  提升到目前檔案的 global 
import mymath as m #   m 是代名

import keyword  
# keyword keyword.kwlist  keyword.iskeyword  
__builtins__  # 是預設匯入的模組    dir(__builtins__)
import math # math.pi  math.e  math.factorial  math.log10   math.log  math.sqrt  math.sin

import random 

random.seed() # 初始化  以系統時間作為亂數種子  可以指定數字 會變成固定的亂數種子   會得相同亂數
random.random() # 0-1 亂數
random.randint(1,7) # 1-6 亂數
random.uniform(0.1,0.5) # 1-6 亂數

random.choice([0,1,2])
random.shuffle([0,1,2])

# random 是  虛擬亂數  假亂數  pseudo random  還是有順序規則  不可用於加密安全

# 2.x  要使用 3.x  用  from __future__ import 模組名稱
# __future__ 要放在第一行   只對目前程式有作用  匯入其他含有 __future__ 的模組檔 沒有作用  還是要寫 p67

# 現成的模組有  字串 資結 檔案 資料儲存  加解密 系統資續  網站服務存取
# PyPI 可查詢




