
#Python 内置的一种数据类型是列表：list.
#list是一种有序的集合，可以随时添加和删除其中的元素
#用[]构造通常会赋值给一个变量
#list是数学意义上的有序集合，也就是说，list中的元素是按照顺序排列的。
#由于Python是动态语言，所以list中包含的元素并不要求都必须是同一种数据类型，我们完全可以在list中包含各种数据


classmates=['Bob','Lucy','Tom']
print(classmates)
n=[90,190,87,33]
print(n)

#访问list 可以通过索引  从0开始
print(n[3])
#倒序
print(n[-1])#倒数第一个
#添加
#append() 添加到末尾   insert(index,'')通过索引添加到任意位置
n.append('Nana')
n.insert(0,334)
print(n)

#添加一个集合
#extend()

# n.extend([3,33])

#删除
#pop()默认从最后一个开始删除  还可以接受一个索引参数，删除第几个
n.pop(2)
#替换  通过索引赋值，相当于替换掉原来的元素

# 在列表中查找列表


my_list=['Michael','Terry',[1989,'what']]

for i in my_list:
    if isinstance(i,list):
        for j in i:
            print(j)
    else:
        print(i)

# isinstance  检查某个特定标识符是否包含某个特定类型的数据




#tuple
#tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了。
t=('Lucy','Pop','Bobo')

#创建tuple和创建list唯一不同之处是用( )替代了[ ]。
#现在，这个 t 就不能改变了，tuple没有 append()方法，也没有insert()和pop()方法。所以，新同学没法直接往 tuple 中添加，老同学想退出 tuple 也不行。

#访问tuple里元素跟list一样 可以去索引去访问 但是不能赋值

print(t)

#创建单个tuple 需要加一个逗号“ ， ”，以示这是一个tuple
tt=(2,)
#如若，会被当做运算

#"可变的"tuple
#tuple的不变是指指向不变，如果指向了a  就不能指向b 了，所谓可变的tuple如
T=(2,3,[4,5]);
l=T[2];
l[1]=22;
print(T)
#结果为(2,3,[22,5])
#这里变的只是l


# 列表操作包含以下函数:
# 1、cmp(list1, list2)：比较两个列表的元素
# 2、len(list)：列表元素个数
# 3、max(list)：返回列表元素最大值
# 4、min(list)：返回列表元素最小值
# 5、list(seq)：将元组转换为列表
# 列表操作包含以下方法:
# 1、list.append(obj)：在列表末尾添加新的对象
# 2、list.count(obj)：统计某个元素在列表中出现的次数
# 3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
# 5、list.insert(index, obj)：将对象插入列表
# 6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7、list.remove(obj)：移除列表中某个值的第一个匹配项
# 8、list.reverse()：反向列表中元素
# 9、list.sort([func])：对原列表进行排序



#
