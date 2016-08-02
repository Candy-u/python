

#函数

#定义一个函数 代码块以 def 关键词开头，后接函数标识符名称和圆括号()。return [表达式] 结束函数


# def functionname(parameters):
#     return [expression]
#默认情况下，参数值和参数名称是按函数声明中定义的的顺序匹配起来的。


def printme(str):
    print(str)
    return

printme('调用函数')
printme('再次调用函数')

#pass 占位符  写个pass可以让程序走起来，不至于报错


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-4))


# def power(x):
#     return x*x
#
# print(power(35))

#x的N次方

def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power(3,4))



#匿名函数
#python 使用 lambda 来创建匿名函数

sum=lambda a1,a2:a1+a2

print(sum(10,10))


#lambda只是一个表达式,不是一个代码块，


# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。



#高阶函数

#能接收函数作参数的函数就是高阶函数


def add(x,y,f):
    return f(x)+f(y)

print(add(3,-4,abs))




#python 内置的高阶函数 map()  reduce()  filter() sorted()


#python 内置函数详解


#http://www.cnblogs.com/wang-yc/p/5635765.html






#
