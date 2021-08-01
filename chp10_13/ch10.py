

# Module 390
# mymath 範例可以見 ch123
# 每個檔案都是模組  主程式是整個程式的進入點  稱主模組檔  就是命令 python 檔名.py 的檔案
# 每個模組都有 __name__ 代表名稱  主模組值是 '__main__'
# 直譯器會記錄已 import 的模組  多次import不會重複載
# import 時  直譯器會先到  module search path 找  在sys.path  安裝路徑
import sys
from types import resolve_bases
sys.path
# 裡面的 '' 就是主程式的路徑
# python 的模組不一定是 py    cpython 很多是 c 寫的  不同 os 上有不同格式
# win dll linux .so jvm .java 
# import 時不加副檔名   主要是直譯器能吃得了就行
# 402 search path 順序   當前目錄  環境變數 PYTHONPATH  標準程式庫目錄
# .pth檔  第三方程式庫目錄 site packages  同名模組先找到的先用
# .pth檔可以有多支  win 在 c:\python34 or \sitepackages  
# linux 在 /usr/lib/python37/site-packages
# /usr/lib/site-python

# 模組命名  因有些 os 不區分大小寫  建議都小寫  兩字可直接合  多字可底線分

# 為加速執行  會先編譯模組為位元組碼  產生在 __pycache__
#   下次編譯時  如果原始檔比位元組新 才回重編
# 在區域 import  只有區域能用

import random as r 
from random import randint #直接使用 randint 不用 random.randint
from random import randint as ri
from random import *  # 匯入多個可能名稱混淆

# 寫模組時  名稱錢加上底線 就不會被 import
# 或者 可以把要被引用者 import  的名稱具體指定在  __all__ = ['a','b'] 
dir(sys) # 列出所有 import 的名稱
# 已載入的模組
sys.modules
# 執行時重新 import  用 reload  以 random ex
# >>> random
# <module 'random' from 'C:\\Users\\\\Python\\Python37\\lib\\random.py'>
# >>> random.__file__
# 'C:\\Users\\Python\\Python37\\lib\\random.py'
from importlib import reload
reload(random)
# reload 後  random.xxx 都會是更新後的值
# 但是如果是指定名稱  import  的語法   from random import randint
# 要再重新執行 import 才會更新  401

# 有子模組的模組  稱為套件 package
# pyhton 裡所有東西都是物件 module 也是  套件的型別也是module

# package_example.py        主程式檔
# package_example/          套件
#   __init__.py 
#   info.py
#   gui/                    子套件
#       __init__.py 
#       menu.py             子套件的子模組
#       canvas.py
#       foo.py
#       bar.py
#   formats/                子套件
#       __init__.py 
#       jpg.py
#       png.py
#   tools/                  子套件
#       rotate.py
#       bar.py

# 匯入子套件  就依序用  import 套件.子套件.模組名  也可 as
# 從套件 import * 不會匯入子模組  只有 __init__.py 定義的名稱
# 可以在 __init__.py  裡 __all__ 手動加入所有子模組名稱 = ['menu', 'canvas', ...]
#  __init__.py 會在子模組載物前執行  可以加入初始化動作
# 例如在 tools\__init__.py  寫 from package_example.tools.bar import *  
# 則在 import tools 時  會一併匯入 bar
# 可簡寫為  from .bar import *  .是同套件尋找  要再上一層  用 ..bar 
# ..gui.foo

# 如果有一個模組越寫越大  想拆分 可以分成多個小檔案  轉為套件  就變成一個
# 最後再 __init__.py  加上 from .子檔1 import *;  from .子檔2 import *... 
# 3.3 加入命名空間套件  還可以把子模組檔  分散到不同目錄
# path1/            # 在 serach path 
#   mymodule/
#       sub1.py
# path1/            # 在 search path 另一個目錄
#   mymodule/
#       sub2.py
# 以上沒有  __init__.py  直譯器會全部搜尋  然後合併
# 主程式檔可以  import mymodule.sub1  import mymodule.sub2

# 安裝第三方模組
# 2000 Diutils    2003 PyPI (Python Packages Index) 
# SetupTools  Egg  EasyInstall  2008 pip  virtualenv

# Debian/Ubuntu Linux apt-get install 模組名   
# Fedora RedHat yum install 模組名

# pip install random==1.2.3
#                   >=
# pip install random.whl
# pip install --upgrade random
# pip uninstall random
# pip list
# pip list--outdated
# pip show random
# pip search "..."
# pip install --user random



