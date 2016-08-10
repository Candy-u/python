
import os

# print(os.getcwd())   #当前项目目录

os.chdir('../HeadFirstPython/chapter2') #切换目录

# print(os.getcwd())

data=open('sketch.txt')

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


for each_line in data:
    if not each_line.find(':')==-1:
        (role,line_spoken)=each_line.split(':',1)#额外的参数 控制split如何分解
        print(role,end='')
        print('  said:',end='')
        print(line_spoken,end='')

data.close()



#
