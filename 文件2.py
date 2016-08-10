
import os

# print(os.getcwd())   #当前项目目录

os.chdir('../HeadFirstPython/chapter2') #切换目录

# print(os.getcwd())

# data=open('sketch.txt')

# print(data.readline(),end='')
# print(data.readline(),end='')

#以上读取文件前两行数据


# data.close()#关闭


#根据需求抽取数据中各个部分    split()

# for each_line in data:
#     (role,line_spoken)=each_line.split(':',1)#额外的参数 控制split如何分解
#     print(role,end='')
#     print('  said:',end='')
#     print(line_spoken,end='')
#
# data.close()
#上述方法解决了数据中有：的报错
#

#split()方法返回一个字符串列表，会赋值给一个目标标识符 这里根据数据来看 role==Man line_spoken='is this the right..'

# for each_line in data:
#     if not each_line.find(':')==-1:
#         (role,line_spoken)=each_line.split(':',1)#额外的参数 控制split如何分解
#         print(role,end='')
#         print('  said:',end='')
#         print(line_spoken,end='')

# data.close()
#上述方法解决了数据中有一行不是：格式的数据
#find()方法如果找不到就会返回-1,所以取相反值，如果不是：格式的数据跳过

#这里只是有两个小问题，如果是大量的数据，不乏会有很多问题，这种排除法，显然是不可行的。





#处理异常

#python 的异常处理机制允许错误出现，但监视它的发生，然后给你一个机会来恢复，在正常的控制流期间，Python尝试运行你的代码，如果没有任何问题，代码会继续正常执行。在异常控制流期间，Python先尝试运行你的代码，如果发现有问题，就会执行恢复代码，然后继续正常执行你的代码。


#try / except 机制

'''
    try:
        你的代码(可能导致一个运行时错误)
    except:
        错误恢复代码
'''


'''for each_line in data:
    try:
        (role,line_spoken)=each_line.split(':',1)
        print(role,end='')
        print('  said:',end='')
        print(line_spoken,end='')
    except:
        pass#如果出一个运行时错误，会执行这个代码


'''




#处理缺少的文件

#如果文件被删除了或者不存在，这两个解决问题的程序都会崩溃
#第一种方法  ：增加代码检查
'''if os.path.exists('sketch.txt'):
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print('  said:',end='')
            print(line_spoken,end='')
        except:
            pass
else:
    print('The data file is missing!')

'''

#第二种方法：  再做一层异常处理

try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            print(role,end='')
            print('  said:',end='')
            print(line_spoken,end='')
        except:
            pass
except:
    print('The data file is missing!')



#特定指定异常

#如果你的异常处理代码设计为处理一种特定类型的错误，一定要在except代码行上指定错误类型，这样一来，就可以把一般化的异常处理代码转变为具有特定性。


# except ValueError
# except IOError

'''
open() 打开一个磁盘文件

readline()读取一行数据

seek() 可以将文件退回到起始位置

close() 关闭文件

split() 将一个字体串分为一个子串列表

数据不符合期望的格式时会出现ValueError

数据无法正常访问时会出现IOError

find() 在一个字符串中查找特定的字串

not 关键字将一个条件取反

help()  bif 允许你在IDLE shell中访问Python的文档

try/except 语句提供了一个异常机制，从而保护可能导致运行时错误的某些代码行。

pass 空语句

'''
#
