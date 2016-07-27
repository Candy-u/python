#
#
# 数据类型
# 整数、浮点数、字符串、布尔值、空
# 字符串是以单引号'或双引号"括起来的任意文本

print(1.22+1.3)
print('abc')#表示一个字符  abc
print("abc")#表示 a  b  c三个字符
print("i am \"ok\"")#\转义
#如果字符串内部有很多换行,用'''...'''的格式表示多行内容

print('''line1
line2
line3
line4''')

#布尔值 True、False 必须大写
#布尔值可以用and、or和not运算
print(2>3)

age=11
if(age<=18):
    print('students')
else:
    print('teacher')

#空值   用none表示，none不能为0，因为0有意义，而none无意义



#变量
#不仅可以是数字 还可以是任意数据类型。
# 变量在程序中就是用一个变量名表示，变量名必有是大小写英文、数字和_的组合，且不能数字开。


a='abc'
b=a
a='xyz'
print(b)




#在Python中，有两种除法，一种除法是/： 一种是//
#/结果是浮点数，不管是否整除
#// 其结果是整数，不管是否整除，即使除不尽，只取结果的整数部分


print(9/3)
print(9//4)
print(10%3)#求余数
