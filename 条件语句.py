
#if条件语句写法如下
age=8
if age<=18:
    print('student')
else:
    print('teacher')
#需要注意的是当一个判断语句没结束时，要加冒号" : "
#多重复杂的如
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
#简写
a=22
if a:
    print(a)
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

# 练习
#
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = float(input('请输入身高：'))
weight = float(input('请输入体重：'))
bmi=weight/(height*height)

if bmi<18.5:
    print('过轻')
elif bmi>=18.5 and bmi<25:
    print('正常')
elif bmi>=25 and bmi<28:
    print('过重')
elif bmi>=28 and bmi<32:
    print('肥胖')
elif bmi>=32:
    print('严重肥胖')


#需要注意的是 input返回的值是字符串类型，需要转换成数据类型  int()整数   float()浮点数



#
