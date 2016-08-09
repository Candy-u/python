
# IO编程

#IO在计算机中指Input/Output，也就是输入和输出。

#最简单的输出就是print了

#读取键盘输入

# Python提供了内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
# input


#input函数
# 从标准输入读取一个行，并返回一个字符串

# str=input("请输入。。。")
# print("你输入的内容："+str)



# 打开和关闭文件
#open() 打开

# the_file=open('test.txt')
# print(the_file.name)  #文件名
# print(the_file.closed)  #文件是否关闭
# print(the_file.mode)  #文件访问模式，默认为R（只读模式）


#close()

# the_file.close()



#os模块    (操作文件和目录)
#引入模块
import os

print(os.name)   # 操作系统类型

#查看当前目录的绝对目录
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/mygit/python','testdir')

#然后创建一个目录
# os.mkdir('/mygit/python/testdir')

#删掉目录
# os.rmdir('/mygit/python/testdir')



#StringIO和BytesIO

#StringIO
#很多时候，数据读写不一定是文件，也可以在内存中读写。
#StringIO顾名思义就是在内存中读写str。

from io import StringIO

f=StringIO()
print(f.write('hello'))  #5
f.write(',')
f.write('world !')

print(f.getvalue())

#getvalue()方法用于获得写入后的str。
#
