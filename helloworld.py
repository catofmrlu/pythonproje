# coding = utf-8

# 语法练习
print("hello world");

print(12 + 31);

a= 12;
b= 23;

# python句尾不用分号
print(a + b)

print("我是鲁新新")


counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print (counter)
print (miles)
print(name)

# 多变量赋值
a = b = c = 12
a, b, c = 121, 23,45

print(a, b, c)

# 字符串练习
s = "string is good"

# 包含左边界，不包含右边界，即strin
str = s[0 : 5]

# 结果是strin
print(str)

print(s * 2 + "\n" + str)
# “*”为重复操作符

#固定间隔截取字符

# 每隔两个字符截取一个字符
str1 = s[0 : 10 : 2]
print(str1)

# 列表
# 可以包含不同数据类型
pylist = [12, "sjas", '12', 858]
jqList = pylist[0 : 3]
print(jqList * 2 )

# 元组
# 远足不能二次赋值
str2 = (123, "wdw", 'dadaa', 232)
print(str2)

# 字典
str4 = {'ss' : 'ddd', 'aa' : 'xxxx', 'fff' : 'jjjjj'}

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
    print("ssss:",letter)


fruits = ['banana', 'apple',  'mango']
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
fopen = open('1.txt', 'w')
print('sssssss文件名：', fopen.name)

# 写入
fopen.write('sssssss')

# 读取文件
fopen.read()

fopen.close()

# 查询是否已关闭输入流
print(fopen.closed)

















