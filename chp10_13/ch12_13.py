
# 457   基本參數檢查
from os import stat, truncate
from typing import ValuesView


def fact(n):    
    if type(n) is not int or n < 0:
        return None # 特殊值表錯誤
    result = 1
    for i in range(n):
        result *= i
    return result

i = 1
while i != 0:
    s = input('input n: ')
    f = fact(int(s))
    if f is not None:
        print('%s = %d' % (s, f))
    else:
        print('n must be non-negative')

# Exception 異常  的寫法
def fact(n):    
    if type(n) is not int:
        raise TypeError
    if n < 0:
        raise ValueError('Argument must be non-negative')
    result = 1
    for i in range(n):
        result *= i
    return result

while i !=0:
    try:
        s = input('input n: ')
        f = fact(int(s))
    except TypeError:
        print(f'{s} is not an interger') 
        # f-string 這本書寫的時候應該還沒出來
        # 跟C# $"{arg}" 一樣
        # https://github.com/microsoft/pylance-release/issues/200
        break
    except ValueError:
        print('%s is not a number ot is less than 0' % s) 
        break
    print('%s = %d' % (s,f))

# /0 ZeroDivisionError   dic KeyError Unicode  UnicodeDecodeError
# Error 架構
# BaseException
#     SystemExit
#     KeyboardInterrupt
#     GeneratorExit
#     Exception
#         StopIteration
#         ArithmeticError
#             FloatingPointError
#             OverflowError
#             ZeroDivisionError
#         AssertionError
#         BufferError
#         EOFError
#         LookupError
#             IndexError
#             KeyError
#         NameError
#             UnboundLocalError
#         OSError
#             BlockingIOError
#             ConnectionError
#                 ConnectionAbortedError
#                 ConnectionRefusedError
#                 ConnectionResetError
#             FileExistsError
#             FileNotFoundError
#             InterruptedError
#         SyntaxError
#         IndentationError
#             TabError
#         TypeError
#         ValueError
#         UnicodeError
#             UnicodeDecodeError
#             UnicodeEncodeError
#         Warning
#            DeprecationWarning
#            PendingDeprecationWarning
#            FutureWarning
#            BytesWarning


# try:
# excpet ExName:
# excpet ExName as name:
# excpet (Ex1, Ex2 ...) as name:
# else:  # 沒異常繼續執行  可有可無
# finally # 同C#   except finally 至少一個

# raise 產生錯誤
# 464
def fact(n):
    if type(n) is not int:
        raise TypeError('Argument must be type int')
    if n < 0:
        raise ValueError('Argument must be non-negative')
    result = 1
    for i in range(1, n+1): 
        result *= i
    return result

while True:
    try:
        s = input('input n: ')     # 2.x版改用raw_input
        f = fact(int(s))
    except TypeError as e: # as 完可以 str 印出訊息
        print('Error: ' + str(e))
        break
    except ValueError as e:
        print('%s can not be less than 0' % s)
        break
    print('%s! = %d' % (s, f))
# 如果只 except 沒有加 ex 會抓到所有的型別  連 ctrl+c 都會抓到 導致無法跳出程式
# 所以至少還是加 except Exception










# 466 不用 with 直接開 + except 
from io import open

try:
    fin = open('test.txt', 'r', encoding='utf-8')
    try:
        for line in fin:
            print(line)
    except UnicodeError as e:
        print('Error while reading file: ' + str(e))
    except Exception as e:
        print('Error while reading file: ' + str(e))
    finally:
        fin.close()
except Exception as e:
    print('Error while opening file: ' + str(e))


# excpet as name  注意不要撞名 3.x 離開 excoet 會刪除 name
# 要在外圍使用 ex 可以另加一個變數賦值
# exc = None
# ... except IndexError as e:
#       exc = e
#       print(exc)
# print(exc)

# try finally 都有 return 時  用 finally 的

e = ImportError('err msg', name='name msg', path='path msg')
e.name
e.path

# excpet Exception:
#   print('err')
#   raise  # 再丟

def get(li, n):
    try:
        li[n]
    except IndexError as e:
        s = 'index %d, len of list is %d' % (n, len(li))
        raise IndexError(s) from e
li = [0, 1, 2]
get(li, 99)
# Traceback (most recent call last):
#   File "<stdin>", line 3, in get
# IndexError: list index out of range
# The above exception was the direct cause of the following exception:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 6, in get
# IndexError: index 99, len of list is 3

# assert 可以搭配 單元測試  assert 不符合  也會raise AssertionError
# assert 運算式一
# assert 運算式一  運算式二
# 相當於
e =3
if __debug__:  # debug 是內建常數  一般 True  但執行時加上參數 -O  效能最佳化
    if not e == 2: raise AssertionError
if __debug__:
    if not e == 2: raise AssertionError(e == 5)

#例如
def fact(n):
    assert type(n) is int
    assert n > 0
    pass

#自訂ex
class MyExcpetion(Exception):
    def __init__(self, msg, status):
        #Exception.__init__(*args)
        super().__init__(self, msg, status)
        self.msg = msg
        self.status = status


# \ 可以斷行接續
if 1 == 0 and 2 == 3\
    and 4 ==5:
    pass
# 三重引號可跨行  有自動加換行符號
s = '''123
345
456'''
s = """123
456"""
s = ("123"  # 視為同行
"456")

# docstring 會存在屬性 __doc__
# 在定義物件時 在內部放字串
#例如放在檔案最上方
"""123
456"""
class Foo:
    """This is a 
test"""
    pass
foo = Foo()
print(foo.__doc__)

# 執行 python 的參數放在 argv  [0] 是檔名  參數跟在後
import sys
print(sys.argv)

# 
import sys

def main(infile, outfile):
    print(infile, outfile)

def proc_argv(argv):
    infile, outfile = None, None
    infile = argv[0]
    try:
        outfile = argv[1]
    except Exception:
        outfile = infile + '.out'
        print("Warning: output filename defaults to " + outfile)
    return infile, outfile

if __name__ == '__main__':
    try:
        inf, outf = proc_argv(sys.argv[1:])
    except Exception:
        print("At least specify input filename")
        sys.exit()
    main(inf, outf)

# 如果參數更複雜  -i filename1 -o filename2  就用專門的模組

# getopt
from getopt import getopt
args = ['-a', '-b', '-c', 'cv', '-d', 'dv', 'x', 'y']
getopt(args, 'abc:d:') # 表示 b 跟 c 後面有帶參數
# ([('-a', ''), ('-b', ''), ('-c', 'cv'), ('-d', 'dv')], ['x', 'y'])
pairs, rest = getopt(args, 'abc:d:') # 表示 b 跟 c 後面有帶參數
# >>> pairs
# [('-a', ''), ('-b', ''), ('-c', 'cv'), ('-d', 'dv')]

args = \
['--file=foo.txt', '--verbose', '--output-file', 'out.txt', '-a', '-b', 'bv', 'x']
pairs, rest = getopt(args, 'ab:', ['file=', 'verbose', 'output-file=' ]) # 表示 b 跟 c 後面有帶參數
# >>> pairs
# [('--file', 'foo.txt'), ('--verbose', ''), ('--output-file', 'out.txt'), ('-a', ''), ('-b', 'bv')]

# 486  更強的工具   定義怎麼解析傳入的參數
import argparse

parser = argparse.ArgumentParser(description='Count lines in text files')

parser.add_argument(dest='path', metavar='path')

parser.add_argument('-e', dest='extensions', action='append',
                    metavar='extension', required=True,
                    help='filename extensions to process')
                    
parser.add_argument('-b', dest='blankline', action='store_true',
                    help='blank line')
                    
parser.add_argument('-r', dest='recur', action='store_true',
                    help='recursively into subdirectories')
                    
parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')
                    
parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='fast',
                    help='processing speed')

args = parser.parse_args()

print('path', args.path)
print('extensions', args.extensions)
print('blankline', args.blankline)
print('recur', args.recur)
print('outfile', args.outfile)
print('speed', args.speed)


# 執行 cmd
import os
os.system('dir')

# 執行外部程式  subprocess   491
# call checkcall check_output
from subprocess import call, check_call, check_output
from subprocess import CalledProcessError
call(['netstat', '-a'])
call('ls - l')
call('ls - l', shell=True)
try:
    check_call('exit 1', shell=True)
except CalledProcessError as e:
    out_b = e.output
    rcode = e.returncode

# check_ouptput 可得指令輸出 預設二進位
out_b = check_output(["echo", "Hello World!"])
# universal_newlines=True 是文字模式
out_t = check_output(["echo", "Hello World!"], universal_newlines=True)
import locale
locale.getpreferredencoding(False) #編解碼
print(out_b.decode('utf-8'))

# 上面的函式會使用較低階的 Popen 來完成   Popen 可以做更進階的
# 如果需製作互動式的主控台程式  可以用  pexpect

# 一般是先寫好成是在執行   執行時動態產生code  或使用者輸入 code 執行
# 是 eval exec  
# eval('程式碼', global 命名空間, local 命名空間)
eval('3 + 5')
gd = {'a':3, 'b':4, 'c':5}
eval('a - b + c', gd) # 4 
ld = {'a':13, 'b':14, 'c':15}
x = eval('a - b + c', gd, ld)  # 14

# eval 運算式  述句或多行  exec 
from io import open
gd = {'c': 10}
with open('a.py', 'r') as fin:
    exec(fin.read(), gd)
    print(gd['a'])
    print(gd['b'])

# pyhton 有直譯器全局鎖  Global Interpreter Lock  執行緒適合用於 IO bound
# 不適合 cpu bound
# python 很早以前就支援 concurrency Thread Process

# 電影院  10個售票員 賣 100張票  用 10 Thread 模擬  亂數模擬賣票所需時間

# 模組清單
# 檔案操作 用 os os.path shutil sys
# xml html  htmllib xml.dom xml.sax  BeautifulSoup
# regular expr   re
# nlp  nltk Natural Language Toolkit
# 微控制器開發板  Arduino  單板電腦 Raspberry Pi  Beagle Bone
# 開發板與外界溝通 : 藍芽 Wifi 紅外線 SPI I2C USB   序列埠 pySerial
# FTP ftplib   TELNET telnetlib  HTTP httplib urllib2 requests
# 網路爬蟲 Scrapy
# 網站 Django Flask   TurboGears Pylons web2Py Pyjamas Zope2 Plone
# game pygame   Minecraft Pyglet
# 多重觸控介面  Kivy
# 資料分析  pandas  數值運算  NumPy  科學數學演算法  SciPy  
# IPython 互動式運算介面  比 CPython 好用

# Lua 遊戲引擎
# 






