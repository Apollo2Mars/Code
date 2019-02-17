## Operator
+ 算术运算符

    + % 取余数
+ 比较运算符

  + <> 是否不相等
+ 赋值运算符
	+ python2 中可用， python3中不可用
	+ +=
	+ -=

+ 逻辑运算符
	+ and
	+ or
	+ not

+ 成员运算符
	+ in
	+ not in

+ 身份运算符
  + is
  	+ is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
  + is not
  	+ is not 是判断两个标识符是不是引用自不同对象
  + demo
        ```
        a = [1, 2, 3]
        b = a
        b is a
        # True
        b == a
        #True
        b = a[:]
        b is a
        #False
        b == a
        True
  ```
  
  ```
