

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






















#
