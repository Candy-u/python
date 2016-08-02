#
#闭包的作用
#封装
#代码复用




#内层函数引用了外层函数的变量,然后返回内层函数的情况，称为闭包（Closure）。


def count():
    for i in range(1,4):
        def f():
            return i*i
    return f()

f2=count()


# print(f2)




#装饰器   decorator
#Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
#可以极大的简化代码，避免函数编写重复性代码

#打印日志   @log
#检测性能   @performance
#数据库事务 @transactiob
#UEL路由    @post('/register')

# def f1(x):
#     return x*2
#
# def new_fn(f):
#     def fn(x):
#         # print('call' + f.__name__ +'()')
#         return f(x)
#     return fn

# g1=new_fn(f1)
# f1=new_fn(f1)
# print(f1(5))


#简化版
def new_fn(f):
    def fn(x):
        # print('call' + f.__name__ +'()')
        print(f.__name__)
        return f(x)
    return fn

@new_fn
def f1(x):
    return x*2
# print(f1(5))


#无参数decorator

def log(f):
    def fn(x):
        print('call  ' + f.__name__ +'()...')
        return f(x)
    return fn

# @log
# def factorial(n):
#     return n*n+1
#
# print(factorial(10))

#报错
# @log
# def add(x,y):
#     return x+y
# print(add(1,2))

#正确写法

def log(f):
    def fn(*args,**kw):
        print('call  ' + f.__name__ +'()...')
        return f(*args,**kw)
    return fn

@log
def add(x,y):
    return x+y
print(add(1,2))


#这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前


import time

t=time.time()
print(t)

#
