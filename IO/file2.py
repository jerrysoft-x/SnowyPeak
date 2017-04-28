import os
# 查看当前目录的绝对路径：
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：
p = os.path.join(r'C:\Users\JJLI\Documents\GitHub\SnowyPeak\IO','testdir')
print(p)
# 然后创建一个目录
# os.mkdir(p)
# 删掉一个目录
os.rmdir(p)