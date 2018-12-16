1.python List交集、并集、差集

1). 获取两个list 的交集
\#方法一:

a=[2,3,4,5]

b=[2,5,8]

tmp = [val for val in a if val in b]

print tmp

\#[2, 5]

\#方法二

print list(set(a).intersection(set(b)))


2). 获取两个list 的并集
print list(set(a).union(set(b)))


3). 获取两个 list 的差集
print list(set(b).difference(set(a))) # b中有而a中没有的

 

2.python Set交集、并集、差集

s = set([3,5,9,10,20,40])      #创建一个数值集合 

t = set([3,5,9,1,7,29,81])      #创建一个数值集合 

a = t | s          # t 和 s的并集 ,等价于t.union(s)

b = t & s          # t 和 s的交集 ,等价于t.intersection(s) 

c = t - s          # 求差集（项在t中，但不在s中）  ,等价于t.difference(s) 

d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）,等价于t.symmetric_difference(s)