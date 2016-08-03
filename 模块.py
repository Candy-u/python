

#使用模块

#简单地说，模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码。一个模块只会被导入一次
#Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
#我们以内建的sys模块为例，编写一个hello的模块：(我们也可以自定义一个模块去导入)


import sys  #导入模块
#sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
def test():
    args=sys.argv
    if len(args)==1:
        print('hello world!')
    elif len(args)==2:
        print('hello,%s' % args[1])
    else:
        print('too many arguments!')

test()


#作用域















#
