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

