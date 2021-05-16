#推导式 comprehensions（又称解析式），是 python 的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列。

#todo 列表推导式
# 语法：变量是在表达式中的额
# 变量名 = [表达式 for 变量 in 列表 for 变量 in  xxx]
# 变量名 = [表达式 for 变量 in 列表 if 条件]


#快速创建一个包含元素1-10的列表

list1 = [i for i in range(1, 11)]
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [2*i for i in range(1, 11)]
print(list2) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#快速创建一个包含1-10之间所有偶数的列表
list1 = [i for i in range(1, 11) if i % 2 == 0]
print(list1) #[2, 4, 6, 8, 10]

#现在有一列表 lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ，求出 1/4/7 和 1/5/9元素，思考如何取出
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst1 = [lst[i][0] for i in range(len(lst))]
print(lst1) #[1, 4, 7]
lst2 = [lst[i][i] for i in range(len(lst))]
print(lst2) #[1, 5, 9]

