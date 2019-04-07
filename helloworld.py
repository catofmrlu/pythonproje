# coding = utf-8

import os
import TestPy
import re
import threading
import _thread


# 语法练习
print("hello world");

print(12 + 31);

a = 12;
b = 23;

# python句尾不用分号
print(a + b)

print("我是鲁新新")

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)

# 多变量赋值
a = b = c = 12
a, b, c = 121, 23, 45

print(a, b, c)

# 字符串练习
s = "string is good"

# 包含左边界，不包含右边界，即strin
str = s[0: 5]

# 结果是strin
print(str)

print(s * 2 + "\n" + str)
# “*”为重复操作符

# 固定间隔截取字符

# 每隔两个字符截取一个字符
str1 = s[0: 10: 2]
print(str1)

# 列表
# 可以包含不同数据类型
pylist = [12, "sjas", '12', 858]
jqList = pylist[0: 3]
print(jqList * 2)

# 元组
# 远足不能二次赋值
str2 = (123, "wdw", 'dadaa', 232)
print(str2)

# 字典
str4 = {'ss': 'ddd', 'aa': 'xxxx', 'fff': 'jjjjj'}

# 赋值或改变值
str4['ss'] = 'cvbn'
print(str4)
print(str4['ss'])
# 打印键
print(str4.keys())
# 打印值
print(str4.values())

if 12 and 12:
    print("ssssssssssssssssssssssssssssdddddssss")
else:
    print("ddddddddddddddddddddddddccccccccc")
aaa = 12
while aaa > 0:
    aaa += -1
    print(aaa)
    print("ssssssss:", aaa)

# for循环练习
for letter in "sssdddsss":
    print("ssss:", letter)

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])

# 函数练习
var11 = min(12, 23, 5, 7)
print('大龙奈斯:', var11)

print('My name is %s and weight is %d kg!' % ('Zara', 21))

hi = ''' hi   
there
 wdjwkd
   dksckskcs
    cmdscks
毛孔 从'''
print(hi)

# 输出练习
# strings = input('请输入：\n')
# print('cscscscssc%s, %s, %d' %(strings, 'sssdddd', 123423))
# print('cscscscssc:', strings)


# 文件读取练习
fopen = open('23333.txt', 'w+')
print('sssssss文件名：', fopen.name)

# 写入
fopen.write('12ss4sss')

# 读取文件
# strr = fopen.read()
# print('dddd', strr)

location = fopen.tell()
print(location)

# 对文件内指针进行位移
fopen.seek(4)
location = fopen.tell()
print(location)

strr = fopen.read(2)
print('dddd', strr)

fopen.close()

# 查询是否已关闭输入流
print(fopen.closed)

# 重命名文件
os.rename('23333.txt', '23333.txt')

# 删除文件
os.remove('23333.txt')

# os.mkdir('luxinxin')

os.chdir('luxinxin')

# 显示当前目录
print(os.getcwd())

# 绝对值
print(abs(-23))

# newPys = TestPy()
# newPys.pri('djkssssssdfdfsg未出厂')

# 正则表达式
subStr = re.sub('s?', 'd', 'huhuewdusddjwsshuhddncuhs')
print(subStr)

a = re.match('s', 'hcshckskksaknjnakc')
print(a)

b = re.search('s', 'naskjcaknasnsmklcaklnasc')
print(b)

pattern = re.compile(r'\d+')
result = pattern.findall('bhcbakbcb94ckjsdckj2004'
                         'ndckjs04u94343nkjs')
print('\n', result, '\n')

j = 0
for i in result:
    print('j = ', j, '------i = ', i)
    j += 1

def testThread(i):
    print('我是线程1', i)
try:
    # 线程练习
    _thread.start_new_thread(testThread, ('thread1'))
except:
    print('出现异常！')






