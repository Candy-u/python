# import time
#
# #函数调用的时间  performance
#
# def performance(f):
#     def fn(*args,**kw):
#         t1=time.time()
#         r=f(*args,**kw)
#         t2=time.time()
#         print('call %s() in %fs' % (f.__name__,t2-t1))
#         return r
#     return fn
#
#
# @performance
# def factorial(n):
#     # print(n)
#     x=0
#     while x < n:
#         x = x+1
#     print(x,n)
# print(factorial(10000))



from functools import reduce
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))


#3.x  reduce 的用法

# from functools import reduce
#
# def myadd(x,y):
#     return x+y
# sum=reduce(myadd,[1,2,3,4,5,6,7])
# print(sum)















#
