# 序列概览
"""
1,Python 中有6种内建的序列。其中列表和元组是最常见的类型。
其他包括字符串、Unicode 字符串、buffer 对象和 xrange 对象。
2,列表和元组的主要区别是列表可以修改，而元组不能，如果要根据要求来添加元素，
这时候列表适用性会更好，但是当序列不能修改的时候，使用元组则更合适，使用元组与 Python 的运作方式相关。
3,在 Python 中几乎所有的情况下列表都可以替代元组，但是特殊情况不能
（当使用元组作为字典的不可修改的键时，此时键不能修改，所以不能使用列表）
"""

# 1   列表
Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# 2   元组 不可修改
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')

#   定义一个学生序列
stuInfo = ['zhangsan', 'lisi', 'wangwu', 18, 20]
stuName = ['zhangsan', 'lisi', 'wangwu']
stuAge = [18, 20, 16]
# 同时序列中还可以包含序列
database = [stuName, stuAge]
print(database)  # database[['zhangsan', 'lisi', 'wangwu'], [18, 20, 16]]

"""
==注意：== Python 还有一种名为容器（container）的数据结构，容器可以包含其他任意对象，
容器主要包括序列和映射（例如：字典）两类。序列的每个元素都有自己的编号，而映射每个元素则
有一个叫做“键”的名字。集合是另一种容器
"""

# 通用序列操作
"""
Python 中所有序列类型都可以进行一些特定的操作，这些操作包括：索引、分片、相加、相乘以及
检查某个元素是否属于序列的成员–>成员资格检测 除此之外，Python 还有计算序列长度，找出最大和最小元素的内建函数。
"""
# 1,索引
"""
序列中所有元素都有编号，这些编号是从 0 开始，依次递增，访问这些元素通过下标即可访问，而这个编号就是索引，
"""
print(" database[0]:", database[0])
print(" database[1]:", database[1])

# 字符串序列的索引,当使用负数索引时，Python会从右边到左进行所有，-1是从序列的最后一个元素开始，
str = 'hello'
print("str[0]:", str[0])
print("str[1]:", str[1])
#  从最后一个元素开始
print("str[-1]:", str[-1])
#  从最后二个元素开始
print("str[-2]:", str[-2])

#  2,分片
"""
1,同样的和索引类似，分片是通过冒号操作来访问一定范围内的元素，
分片操作的的实现需要提供两个索引作为边界，是一个左闭右开的区间，也就是第 1 个索引包含在分片内，而第2个索引不包含在这个分片内
"""
# 构建一个序列tag，里面包含一个元素
tag = ['https://www.cnblogs.com/yangyuqig/p/10101663.html']

# 拿到这个元素后通过分片取出一个范围的值
print("tag[0][0:24]:", tag[0][0:24])

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 表示从第四个到最后一个元素
print("num[3:10]:", num[3:10])

# 分片方式
"""
1,分片快捷操作 num[0:3]
2,分片步长操作
2.1 分片操作可以给元素设置步长，在开始和结束的时候指定相应步长获取元素，
2.2 另外需要注意的是负数步长是从元素尾部到前遍历整个序列，所以负数的分片开始索引一定要大于结束索引
   当开始索引和结束索引是负数时开始所以必须小于结束索引：
2.3 对于一个正数步长，Python会从序列的头部开始向右提取元素，直达最后一个元素，而对于负数步长，则是从序列的尾部开始向左提取元素，直达提取到第一个
"""
# 提取前6个元素，步长为2
print("num[0:6:2]:", num[0:6:2])
print("num[7:-1]:", num[7:-1])
print("num[-9:-1]:", num[-9:-1])
# 提取从后往前的8个元素，步长为2
print("num[:2:-2]:", num[:2:-2])

#  3.序列相加
"""
注意：只有相同类型的序列才能进行连接操作
"""
print('hello' + ' world !')
print([1, 2, 3] + ['zhangsan', 'lisi', 'wangwu'])

#  4.序列相乘
"""
一个数字 x 乘以一个序列会产生一个新的序列,原来的序列会被重置成x次
"""
print(['hello' + ' world !'] * 3)

#  5.成员资格
"""
检查一个元素是否在一个序列中使用运算符 in 进行检查， in 运算符返回检查某个条件的布尔值，若为真返回 true,否则返回 false，
"""
print('h' in 'hello')
print('x' in 'hello')

#  6.序列长度、最大值和最小值
"""
序列长度、最大值和最小值使用内建函数 len、max、min 进行检测，len 返回序列中所包含的元素数量，max 和 min 分别返回序列中最大值和最小值的元素
"""
print("len([11,34,23]):", len([11, 34, 23]))
print("max([11,34,23]):", max([11, 34, 23]))
print("min([11,34,23]):", min([11, 34, 23]))
