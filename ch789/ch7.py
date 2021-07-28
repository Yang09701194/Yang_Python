
# 一個  ASCII  字元  佔多少位元組  字元集  編碼方式  編碼系統
fin = open('test.txt')
print(fin.readline())
for line in  fin:
    print(line)  # 預設印完會空一行  可以改 print(line, end = '')
fin.close()

fin = open('test.txt', 'r') # r 讀取 w 寫 a 附加  x 寫 檔案不存在建立新的 已存在err
# t 文字模式 預設  b 二進位模式 r+ 更新 可讀寫 檔案已存在 從頭開始讀寫
# w+ 更新 可讀寫 開新檔案 或覆蓋舊檔(原檔案內容消失) 從頭開始讀寫
# a+ 更新 可讀寫 開新檔案 或從檔案結尾讀寫

# 複製檔案
fin = open('test.txt')
fout = open('testw.txt', 'w')
for line in  fin:
    print(line) 
    fout.write(line)
fin.close()
fout.close()

# 檔案的 readlines() 可以讀取每一行並放在 ls  但是會一次載入全部檔案內容  
# 才迭代  效率低

fin = open('test.txt', 'rb') # 二進位模式
data = fin.read(5)           # 讀 5 byte
print(data, type(data))
fin.close()

# 只有一個  str  型別  統合 八字元字串 Unicode 字串  
# 位元組由 bytes 型別負責   bytearray 是 bytes 可變版
# 285
# >>> import sys
# >>> sys.stdin.read()
# 123
# ^Z
# '123\n'
# >>> sys.stdout.write('hello')
# hello5
# >>>
#287  3.x 的 io.open 功能比 2.x 更強大    file-like stream
from io import open
# 文脈管理協定  context management protocal
# 資源開啟  忘記關閉 資源沒有釋放的問題  可透過 protocal  建立的物件
# with 標示 進入點  離開with後  物件會自動被關閉     根本就是 using  = =
with open('test.txt', 'r') as fin:
    for line in fin:
        print(line, end = '')

'\x00\x01\x02' # '\x00\x01\x02'
'\x61\x62\x63' # abc   ASCII 編碼底下 a = 97  十六進位 x61
ord('a'), ord('\x01') # (97, 1)
b'abc' # b 表型別 bytes
# Unicode 字串 開頭 u
u'abc\u4f60\u6211\u4ed6'  #'abc你我他'
import sys
sys.stdin.encoding
sys.stdout.encoding
'cp950'  # 相當 cmd 的 chcp  Active code page: 950
u'abc你我他' + 'abc'  # 'abc你我他abc'
# pyhton 取得資料時  都是先轉成 unicode 再轉成輸出的編碼

# 291
# >>> data = '我'
# >>> u = data.decode('big5')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'str' object has no attribute 'decode'
#
#You are trying to decode an object that is already decoded. You have a str, there is no need to decode from UTF-8 anymore.
# https://stackoverflow.com/questions/28583565/str-object-has-no-attribute-decode-python-3-error

# 292 列出很多編碼系統清單  同一份位元組 不同編碼系統會解出不同的字
chr(97) # 'a'
s = 'abc'
b = 'abc'.encode('utf_8')
len(s), len(b)  # 3,3 書 3,6
# python 3.x 所有字串都是 unicode 不用加上 u

# 要保證對應  檔案編碼  1 在檔案開頭加上檔案編碼  2 open 指定編碼
# -*- coding: utf-8 -*-
# 你好
from __future__ import print_function
from io import open

print('你好Python')
with open('ch07_print_self_utf8.py', encoding='utf8') as fin:
    for line in fin:
        print(line, end='')
print('再見Python')

# 298 open 有八個參數
#file mode
#  buffering  0 關密緩衝 只能用於 1 行緩衝 文字模式  > 1 指定大小 預設 -1 系統決定
# encoding errors  預設None 會 strict  發生錯誤 引發 ValueError  ignore 忽略 可能會遺失資料
# replace 替換成其他字元 如 ?
# newline  不同系統   新行字元不同 Win \r\n UNIX \n Max \r
# pyhton 預設 \n  也可指定 '' \r \r\n   寫入模式轉為 os.linesep
# closefd opener
import os
os.linesep

# io 檔案物件  支援介面
# close flush 寫出緩衝區  closed readable writable  read(n=-1)
# readlall write(bytes) seekable tell seek(offset, whence SEEK_SET/CUR/END
# truncate(sixe=None)  encoding errors newlines read readline readlines 
# write writelines

# print 
with open('test.txt', 'w', encoding='utf8') as fout:
    print('Hello Python', file=fout)
    print([0,1,2], file=fout)
    print({'a':1, 'b':2}, file=fout)

# 可指定 sys.stdout = fout  就變成print 會輸出到 fout 用完可還原 搜尋 redirect

import codecs #  有各種編碼相關函式
codecs.lookup('utf8')
codecs.getencoder('utf8')
codecs.getdecoder('utf8')
s=codecs.decode(b'\xBB\xBB', 'big5')
print(s) # 遙
codecs.encode(s, 'big5') # b'\xBB\xBB' 
enc = codecs.getencoder('urf-16be') # 書找的到 執行 err
enc = codecs.getdecoder('urf-16be') # 同上
# s = dec(b'\x90\x90')  #書有 執行 err   enc 

#　檔案　轉換編碼 也簡單  open fin r 用一種編碼 　open fout w 用另一種 
# 再逐行寫入就可以了

# csv 有專用模組處理 312
# json 有專用模組處理 313

# 316 二進位讀寫
data = bytearray(range(10))
#bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t')
# jpeg zip wav 都有模組可以處理

# 十六進位編輯器  可以觀看  編輯  檔案裡的每個位元組
# google Hex Editor

# 介紹 C 的 struct 儲存成位元組二進位 
# pyhton 也有 struct 可以用 pack unpack 轉乘 轉回  二進位 319
# picle 也可以  Pikler dump Unpikler laod
import pickle

# codec coder-decoder  編解碼器  322
# 編碼概念
# character 定義轉換到的數字 character code 
# 組合成 character set 或 code page (簡寫 CP)
#  定義 character scheme 轉成 bytes
# 再解碼 轉回字元  再搭配 font 描繪顯示

# BOM Byte Order Mark 333



# -*- coding: utf-8 -*-
from io import open

# 計算文字檔有幾行
def line_count(filepath, enc='utf8'):
    count = 0
    with open(filepath, mode='r', encoding=enc) as fin:
        for line in fin:
            count += 1
    return count

# 計算文字檔有幾行，另一種作法
def line_count_2(filepath, enc='utf8'):
    return sum(1 for line in open(filepath, mode='r', encoding=enc))

# 為文字檔加上行號，參數：輸入檔路徑、輸出檔路徑、編碼
def line_number(fin_path, fout_path, enc='utf8'):
    lc = line_count(fin_path)      # 知道行數才能對齊
    lcw = len(str(lc))             # 該佔幾格
    with open(fin_path, mode='r', encoding=enc) as fin:
        with open(fout_path, mode='w', encoding=enc) as fout:
            for i, line in enumerate(fin):
                fout.write(u'{:0{width}d} {}'.format(i+1, line, width=lcw))


# -*- coding: utf-8 -*-
from io import open
import os
import os.path

# 計算文字檔有幾行
def line_count(filepath, enc='utf8'):
    count = 0
    with open(filepath, mode='r', encoding=enc) as fin:
        for line in fin:
            if line.strip():       # 空白行不算
                count += 1
    return count
# 判斷文字編碼系統，從檔案開頭的前幾個位元組
def what_encoding_by_head(filepath):
    enc = None
    with open(filepath, 'rb') as fin:
        data = fin.read(3)
        if len(data) == 3:       # Windows會在UTF-8檔案開頭加上BOM
            if data[0] == 0xEF and data[1] == 0xBB and data[2] == 0xBF:
                enc = 'utf8'
        if len(data) >= 2:       # UTF-16 BE與LE
            if data[0] == 0xFE and data[1] == 0xFF:
                enc = 'UTF-16BE'
            elif data[0] == 0xFF and data[1] == 0xFE:
                enc = 'UTF-16LE'
    return enc
# 判斷文字編碼系統，從第一行或第二行，若含有'coding'字樣的話
def what_encoding_by_mark(filepath):
    enc = 'ascii'            # 預設為ASCII
    mark = 'coding'          # 編碼標記字樣
    def extract_enc(line):
        chars = ' :=-*'      # 編碼標記字樣周圍無用的字元
        return line.strip().lstrip(chars).rstrip(chars)
    with open(filepath, mode='r', encoding=enc, errors='ignore') as fin:
        for i in range(2):         # 只讀兩行
            line = fin.readline()
            idx = line.find(mark)  # 若含有編碼標記字樣
            if idx != -1:
                enc = extract_enc(line[idx+len(mark):])
                break
    return enc
# 判斷文字編碼系統
def what_encoding(filepath):
    return what_encoding_by_head(filepath) or what_encoding_by_mark(filepath)

lc_total = 0         # 總行數
file_count = 0       # 被計算行數的檔案個數
for p in os.listdir('.'):      # 2.x版應使用u'.'
    if os.path.isfile(p) and p[-3:] == '.py':
        try:
            enc = what_encoding(p)
            lc = line_count(p, enc)
            lc_total += lc
            file_count += 1
            print(p, enc, lc)
        except:
            print(p, "can't count lines")

print('%d .py files totally have %d lines ' % (file_count, lc_total))
# -*- coding: utf-8 -*-
from io import open
import string

# 回傳轉換表，shift是偏移量，可正可負，encrypt代表要加密還是解密
def caesar_table(shift, encrypt=True):
    lowers = string.ascii_lowercase    # 小寫英文字母
    uppers = string.ascii_uppercase    # 大寫英文字母
    lowers_new = lowers[shift:] + lowers[:shift]
    uppers_new = uppers[shift:] + uppers[:shift]
    # 若是2.x版，請把str.maketrans改成string.maketrans
    # maketrans的功能是製作轉換表，供str.translate使用
    if encrypt:
        return str.maketrans(lowers+uppers, lowers_new+uppers_new)
    else:
        return str.maketrans(lowers_new+uppers_new, lowers+uppers)
# 凱撒密碼，shift是偏移量，encrypt代表要加密還是解密
def caesar(file_in, file_out, shift, encrypt=True):
    table = caesar_table(shift, encrypt)
    with open(file_in, mode='r', encoding='ascii') as fin:
        with open(file_out, mode='w', encoding='ascii') as fout:
            for line in fin:
                # 呼叫translate，傳入轉換表
                fout.write(line.translate(table))
                
caesar('test.txt', 'encrypt.txt', 3, True)
caesar('encrypt.txt', 'decrypt.txt', 3, False)


#redirect
# -*- coding: utf-8 -*-
from __future__ import print_function
from io import open
import sys

with open('test.txt', 'w', encoding='utf-8') as fout:
    stdout_backup = sys.stdout
    sys.stdout = fout
    print(u'Hello Python')
    sys.stdout = stdout_backup

# -*- coding: utf-8 -*-
# Python 3.x
import csv

with open('csv.txt', 'r', encoding='utf-8') as fin:
    with open('csv_out.txt', 'w', encoding='utf-8') as fout:
        csvreader = csv.reader(fin, delimiter=',')
        csvwriter = csv.writer(fout, delimiter=' ')
        header = next(csvreader)
        csvwriter.writerow(header)
        for row in csvreader:
            row[0] = row[0].replace('/', '-')
            row[-1] += '%'
            print(','.join(row))
            csvwriter.writerow(row)


# -*- coding: utf-8 -*-
from __future__ import print_function
from io import open
import json

with open('json.txt', 'r', encoding='ascii') as fin:
    data = json.loads(fin.read())
    print(data['menu']['hello'])
    print(data['menu']['flag'])
    print(data['menu']['count'])
    with open('json_out1.txt', 'w', encoding='ascii') as fout:
        fout.write(json.dumps(data, separators=(',', ':')))
    with open('json_out2.txt', 'w', encoding='ascii') as fout:
        fout.write(json.dumps(data, sort_keys=True, 
                 indent=4, separators=(',', ':')))



