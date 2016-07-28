#Python的循环有两种，
#一种是for...in循环，依次把list或tuple中的每个元素迭代出来
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。

sl=[1,2,3,4]
for num in sl:
    print(num)

#计算 总和

sum=0
for n in [1,2,3,4,5,6,7,8,9]:
    sum=sum+n
print(sum)

#range(n)可以生成一个从0开始小于n的整数序列，再通过list()函数可以转换为list
l=range(10)
al=list(l)
print(al)
sum=0
for n in range(101):
    sum=sum+n
print(sum)


#while循环

ss=0;
n=9
while n>0:
    ss=ss+n
    n=n-1
print(ss)



#break退出循环
#continue继续循环
#
