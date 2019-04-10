# coding = utf-8

import os
import TestPy
import re
import threading
import _thread
import xml.sax
import json

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


class TestHandler(xml.sax.ContentHandler):
    def __init__(self):

        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attr):
        self.CurrentData = tag
        if tag == 'movie':
            print('-------电影----------')
            title = attr['title']
            print('电影名：', title)

    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

        # 读取字符时调用

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content



if (__name__ == "__main__"):
    try:
        # 创建一个 XMLReader
        parser = xml.sax.make_parser()
        # 关闭命名空间
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        # 重写 ContextHandler
        Handler = TestHandler()
        parser.setContentHandler(Handler)

        parser.parse("movies.xml")
    except IOError:
        print('解析xml出现IO异常！')
    except:
        print('其他异常！')
    else:
        print('解析成功！')


# 解析json,json对象与python的字典相互转换

# 封装json
jsonTest = {'name': 'luxinxin',
            'age': 25,
            'university': 'JJU'}
json_test = json.dumps(jsonTest)
print('-----', jsonTest)
print('---json--zd:', json_test)

# 转换json为字典数据
json_data = json.loads(json_test)

print('---json:age:', json_data['age'])
print('---json:name:', json_data['name'])
print('---json:university:', json_data['university'])

# 处理json文件
# json_file = json.dump('test.json', 'r')
# with open('test.json', 'r') as f:
#     data = json.load(f)
#
# print(data)

with open('data2.json', 'w') as f:
    json.dump(json_data, f)

with open('data2.json', 'r') as f:
    data = json.load(f)

print(data)


