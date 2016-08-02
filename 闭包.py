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
#         # print('call' + f._name_ +'()')
#         return f(x)
#     return fn

# g1=new_fn(f1)
# f1=new_fn(f1)
# print(f1(5))


#简化版
def new_fn(f):
    def fn(x):
        # print('call' + f._name_ +'()')
        return f(x)
    return fn

@new_fn
def f1(x):
    return x*2

print(f1(5))

















#
