# Python
## 1. Python Basic
+ version
    ```
    python -V
    ```
+ encoding
	+ 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串
	+ 当然你也可以为源码文件指定不同的编码：
    ```
    # -*- coding: cp-1252 -*-
    ```
+ 标识符
+ 保留字
+ 注释
	+ 单行 #
	+ 多行 ``` 和 “”“
+ 行与缩进
+ 多行语句
	+ 使用反斜杠(\)来实现多行语句
	+ 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
+ 同一行显示多条语句
	+ Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
	```
    import sys; x = 'runoob'; sys.stdout.write(x + '\n')
    ```

+ 用户交互
	```
    input("\n\n按下 enter 键后退出。")
    ```
+ Print 输出
	+ print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
	```
    x="a"
    y="b"
    # 换行输出
    print( x )
    print( y )

    print('---------')
    # 不换行输出
    print( x, end=" " )
    print( y, end=" " )
    print()
    ```
+ 命令行参数
	+ python -h 查看各参数帮助信息

## 2. Data Type
+ 创建
	+ Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
	+ 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型
    + 多个变量赋值
        + a = b = c = 1
        + a, b, c = 1, 2, "runoob"
+ 删除
	+ del var
	+ del var_a, var_b
+ Number
	+ int
	+ bool
	+ float
	+ complex(复数3.14j)
	+ 数据运算
		+ 2 / 4  # 除法，得到一个浮点数  == 》 0.5
		+ 2 // 4 # 除法，得到一个整数   == 》 0
		+ 17 % 3 # 取余 == 》 2
		+ 2 ** 5 # 乘方 == 》 32  **
		+ 在混合计算时，Python会把整型转换成为浮点数
	+ **Function**
		+ Math
			+ constant
				+ pi
				+ e
            + abs
            + ceil
            + cmp(x,y)
            	+ 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x < y) 替换
            + exp
            + fabs
            + floor
            + log
            + log10
            + max(...)
            + min(...)
            + (???) modf
                + 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
            + pow(x,y)
            + round(x[,n])
                + 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
            + sqrt
		+ random
			+ choice(seq)
				+ 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
			+ (???) randrange ([start,] stop [,step])
				+ 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1

			+ random()
				+ 随机生成下一个实数，它在[0,1)范围内。
			+ (???)seed()
				+ 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
			+ shuffle
				+ 	将序列的所有元素随机排序
			+ uniform
				+ 随机生成下一个实数，它在[x,y]范围内。
		+ Trigonometric
			+ acos
			+ asin
			+ atan
			+ atan2
			+ cos
			+ pypot(x,y)
				+ 返回欧几里德范数 sqrt(x*x + y*y)
			+ sin
			+ tan
			+ degrees
				+ 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
			+ radians
				+ 将角度转换为弧度

+ String 不可变 ”“ ‘’
	+ python中单引号和双引号使用完全相同
    + 使用三引号(单引号或双引号)可以指定一个多行字符串。
    + 转义符 '\'
    + 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
    + 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
    + 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
    + *Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。*
    + Python中的字符串不能改变
    + Python 没有单独的字符类型，一个字符就是长度为 1 的字符串
    + 字符串的截取的语法格式如下：变量[头下标:尾下标]
        ```
        # example 1
        word = '字符串'
        sentence = "这是一个句子。"
        paragraph = """这是一个段落，
        可以由多行组成"""
        # example 2
        str='Runoob'
        print(str)                 # 输出字符串
        print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
        print(str[0])              # 输出字符串第一个字符
        print(str[2:5])            # 输出从第三个开始到第五个的字符
        print(str[2:])             # 输出从第三个开始的后的所有字符
        print(str * 2)             # 输出字符串两次
        print(str + '你好')        # 连接字符串
        print('------------------------------')
        print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
        print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

        # output
        Runoob
        Runoo
        R
        noo
        noob
        RunoobRunoob
        Runoob你好
        ------------------------------
        hello
        runoob
        hello\nrunoob
        ```
	+ **Function**
		+ capitalize()
			+ 将字符串的第一个字符转换为大写
		+ center(width, fillchar)
			+ 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格
		+ count(str,beg=0,end=len(str1))
			+ 返回 str 在 str1 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
		+ bytes.decode(encoding="utf-8", errors="strict")
			+ python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回
		+ encode(encoding='UTF-8',errors='strict')
			+ 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
		+ endswith(suffix, beg=0, end=len(string))
			+ 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False
		+ expandtabs(tabsize=8)
			+ 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 
		+ find(str, beg=0 end=len(string))
			+ 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
		+ index(str, beg=0, end=len(string))
			+ 跟find()方法一样，只不过如果str不在字符串中会报一个异常
		+ isalnum()
			+ 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
		+ isalpha()
			+ 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
		+ isdigit()
			+ 如果字符串只包含数字则返回 True 否则返回 False
		+ islower()
			+ 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
		+ isnumeric()
			+ 如果字符串中只包含数字字符，则返回 True，否则返回 False
		+ isspace()
			+ 如果字符串是标题化的(见 title())则返回 True，否则返回 False
		+ (???)isupper()
			+ 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
		+ join
			+ 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
			+ (???)example
		+ len
		+ ljust(width[, fillchar])
			+ 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
		+ lower
		+ lstrip()
			+ 截掉字符串左边的空格或指定字符
		+ (???) maketrans()
			+ 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标
		+ max(str)
			+ 返回字符串 str 中最大的字母
		+ min(str)
			+ 返回字符串 str 中最小的字母
		+ replace(old, new [, max])
			+ 把 将字符串中的 old 替换成 new ,如果 max 指定，则替换不超过 max 次
		+ rfind
		+ rindex
		+ rjust
		+ rstrip
		+ split(str="", num=string.count(str))
			+ num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
			+ str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
			+ num -- 分割次数
			```
            str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
			print str.split( );
			print str.split(' ', 1 );
            # output
            ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
			['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
            ```
		+ (???)splitlines([keepends])
			+ 按照行('\r', '\r\n', '\n')分隔，返回一个包含各行作为元素的列表
			+ 如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
		+ startswith(str, beg=0,end=len(string))
			+ 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
		+ strip([chars])
		+ swapcase()
		+ title()
			+ 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
		+ (???)translate(table, deletechars="")	
			+ 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
		+ upper
		+ zfill (width)
			+ 返回长度为 width 的字符串，原字符串右对齐，前面填充0
		+ isdecimal()
			+ 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

+ List(可变) []
	+ 列表是写在方括号([])之间、用逗号分隔开的元素列表
	+ 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表
		+ 截取 ： 变量[头下标:尾下标]
		+ 索引值以 0 为开始值，-1 为从末尾的开始位置
	+ 加号（+）是列表连接运算符，星号（*）是重复操作
	```
    list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
    tinylist = [123, 'runoob']

    print (list)            # 输出完整列表
    print (list[0])         # 输出列表第一个元素
    print (list[1:3])       # 从第二个开始输出到第三个元素
    print (list[2:])        # 输出从第三个元素开始的所有元素
    print (tinylist * 2)    # 输出两次列表
    print (list + tinylist) # 连接列表
    #output
    ['abcd', 786, 2.23, 'runoob', 70.2]
    abcd
    [786, 2.23] # list[1], list[2]
    [2.23, 'runoob', 70.2] # list[2],...
    [123, 'runoob', 123, 'runoob']
    ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
    ```
    + 与Python字符串不一样的是，列表中的元素是可以改变的
    ```
    a = [1, 2, 3, 4, 5, 6]
    a[0] = 9
    a[2:5] = [13, 14, 15]
    a
    [9, 2, 13, 14, 15, 6]
    a[2:5] = []   # 将对应的元素值设置为 []
    a
    [9, 2, 6]
    ```
    + **Function**
    	+ len(list)
    	+ max(list)
    	+ min(list)
    	+ list(seq)
    		+ 将元组转化为列表
    	+ list.append(obj)
			+ 在列表末尾添加新的对象
		+ list.count(obj)
			+ 统计某个元素在列表中出现的次数
		+ list.extend(seq)
			+ 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
		+ list.index(obj)
			+ 从列表中找出某个值第一个匹配项的索引位置
		+ list.insert(index, obj)
			+ 将对象插入列表
		+ list.pop(obj=list[-1])
			+ 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
		+ list.remove(obj)
			+ 移除列表中某个值的第一个匹配项
		+ list.reverse()
			+ 反向列表中元素
		+ list.sort([func])
			+ 对原列表进行排序
		+ list.clear()
			+ 清空列表
		+ list.copy()
			+ 复制列表

+ Tuple (不可变/immutable)Set() {}
	+ 元组（tuple）与列表类似，不同之处在于元组的元素不能修改
	+ 可包含List等可变的对象
	```
    tup = (1, 2, 3, 4, 5, 6)
	print(tup[0])
    ```
    + 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则
    ```
    tup1 = ()    # 空元组
	tup2 = (20,) # 一个元素，需要在元素后添加逗号
    ```
    + **Function**
    	+ len(tuple)
    	+ min(tuple)
    	+ max(tuple)
    	+ tuple(seq)
    		+ 将列表转换为元组
    		```
            list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
			tuple1=tuple(list1)
			tuple1
			('Google', 'Taobao', 'Runoob', 'Baidu')
            ```
+ Sets
	+ 集合（set）是一个无序不重复元素的序列
	+ 基本功能是进行成员关系测试和删除重复元素
	+ 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
	```
    parame = {value01,value02,...}
	# 或者
	set(value)
    ```
    ```
    student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
    print(student)   # 输出集合，重复的元素被自动去掉
    # 成员测试
    if('Rose' in student) :
        print('Rose 在集合中')
    else :
        print('Rose 不在集合中')
    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(a - b)     # a和b的差集
    print(a | b)     # a和b的并集
    print(a & b)     # a和b的交集
    print(a ^ b)     # a和b中不同时存在的元素
    ```
+ Dictionary（可变/mutable） {}
	+ 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
	+ 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合
	+ 键(key)必须使用不可变类型
	+ 在同一个字典中，键(key)必须是唯一的
	```
    dict = {}
	dict['one'] = "1 - 菜鸟教程"
	dict[2]     = "2 - 菜鸟工具"

	tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

    print (dict['one'])       # 输出键为 'one' 的值
    print (dict[2])           # 输出键为 2 的值
    print (tinydict)          # 输出完整的字典
    print (tinydict.keys())   # 输出所有键
    print (tinydict.values()) # 输出所有值
    ```
    + **Function**
    	+ len(dict)
    	+ str(dict)
    	+ type(variable)
    	+ ---
    	+ radiansdict.clear()
			+ 删除字典内所有元素
		+ radiansdict.copy()
			+ 返回一个字典的浅复制
		+ (???)radiansdict.fromkeys()
			+ 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
		+ radiansdict.get(key, default=None)
			+ 返回指定键的值，如果值不在字典中返回default值
		+ key in dict
			+ 如果键在字典dict里返回true，否则返回false
		+ radiansdict.items()
			+ 以列表返回可遍历的(键, 值) 元组数组
			+ dict 转 list
		+ radiansdict.keys()
			+ 以列表返回一个字典所有的键
		+ radiansdict.setdefault(key, default=None)
			+ 和get()类似
			+ 但如果键不存在于字典中，将会添加键并将值设为default
		+ radiansdict.update(dict2)
			+ 把字典dict2的键/值对更新到dict里
		+ radiansdict.values()
			+ 以列表返回字典中的所有值
		+ pop(key[,default])
			+ 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
		+ popitem()
			随机返回并删除字典中的一对键和值(一般删除末尾对)。
+ 类型转换
    + int
    + float
    + complex
    + str
    + repr
        + 将对象 x 转换为表达式字符串
    + eval
        + 用来计算在字符串中的有效Python表达式,并返回一个对象
    + tuple(s)
        + 将序列s转化为一个元组
    + list(s)
        + 将序列s转化为一个列表
    + set(s)
        + 转化为可变集合
    + dict(d)
        + 创建字典
        + d必须是一个序列（key,value）元组
    + frozenset(s)
        + 转化为不可变集合
    + chr(x)
        + 将整数转化为字符
    + ord(x)
        + 将字符转化为它的整数值
    + hex(x)
        + 整数转为十六进制
    + oct(x)
        + 整数转化为八进制

## 3. Operator
+ 赋值运算符
+ 位运算符
	+ &
	+ |
	+ ^ 异或
	+ ～ 取反
	+ <<
	+ \>>

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
	+ is not

+ 优先级

## 4.Regular Expression
+ split
	```
	# lineSeg = line.split('/[\w]+')
	lineSeg = re.split('/\w+', line)
    ```

## 5.Loop
+ if
    ```
    if expression :
       suite
    elif expression :
       suite
    else :
       suite
    ```
+ while
    + 无限循环
    + while else
    ```
    count = 0
    while count < 5:
       print (count, " 小于 5")
       count = count + 1
    else:
       print (count, " 大于或等于 5")
    ```
+ for
+ range()
    ```
    for i in range(5):
        print(i)
    0
    1
    2
    3
    4
	```
+ break
    + break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
+ couninue
	+ continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
+ pass
	+ 占位

## 6.Iterator and Generator
+ Iterator
	+ 访问集合元素的一种方式
	+ 迭代器是一个可以记住遍历的位置的对象
	+ 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退
	+ 两个基本的方法：iter() 和 next()
	+ 字符串，列表或元组对象都可用于创建迭代器
	```
    # demo1
    list=[1,2,3,4]
	it = iter(list)    # 创建迭代器对象
	print (next(it))   # 输出迭代器的下一个元素
	# 1
	print (next(it))
	# 2
	# demo2
    list=[1,2,3,4]
	it = iter(list)    # 创建迭代器对象
	for x in it:
		print (x, end=" ")
    # demo3
    import sys         # 引入 sys 模块
	list=[1,2,3,4]
	it = iter(list)    # 创建迭代器对象
	while True:
    	try:
        	print (next(it))
    	except StopIteration:
        	sys.exit()
	```
+ Generation
	+ 使用了 yield 的函数被称为生成器（generator）
	+ 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
    + 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
    + 调用一个生成器函数，返回的是一个迭代器对象
    ```
    import sys
    def fibonacci(n): # 生成器函数 - 斐波那契
        a, b, counter = 0, 1, 0
        while True:
            if (counter > n):
                return
            yield a
            a, b = b, a + b
            counter += 1
    f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

    while True:
        try:
            print (next(f), end=" ")
        except StopIteration:
            sys.exit()
    ```

## 7.Function
+ 函数定义：
    + 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()
    + 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
    + 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    + 函数内容以冒号起始，并且缩进。
    + return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
+ 参数传递：
	+ 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
	```
    def ChangeInt( a ):
    a = 10
	b = 2
	ChangeInt(b)
	print( b ) # 结果是 2
    ```
	+ 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
	```
    def changeme( mylist ):
       "修改传入的列表"
       mylist.append([1,2,3,4]);
       print ("函数内取值: ", mylist)
       return

    mylist = [10,20,30];
    changeme( mylist );
    print ("函数外取值: ", mylist)
    # 结果
    函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
	函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
    ```
+ 参数
	+ 必须参数
	+ 关键字参数
		```
        def printinfo( name, age ):
           "打印任何传入的字符串"
           print ("名字: ", name);
           print ("年龄: ", age);
           return;
        #调用printinfo函数
        printinfo( age=50, name="runoob" );
        ```
	+ 默认参数
	+ 不定长参数
		```
        def printinfo( arg1, *vartuple ):
           "打印任何传入的参数"
           print ("输出: ")
           print (arg1)
           for var in vartuple:
              print (var)
           return;

        # 调用printinfo 函数
        printinfo( 10 );
        printinfo( 70, 60, 50 );
        ```
+ 匿名函数
	+ python 使用 lambda 来创建匿名函数。
	+ 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
	+ lambda 只是一个表达式，函数体比 def 简单很多。
	+ lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
	+ lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
	+ 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
	```
	sum = lambda arg1, arg2: arg1 + arg2;
	# 调用sum函数
	print ("相加后的值为 : ", sum( 10, 20 ))
	print ("相加后的值为 : ", sum( 20, 20 ))
    # output
    相加后的值为 :  30
	相加后的值为 :  40
    ```
+ 变量作用域
	+ 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
		+ L （Local） 局部作用域
        + E （Enclosing） 闭包函数外的函数中
        + G （Global） 全局作用域
        + B （Built-in） 内建作用域
     	+ 以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
	```
    x = int(2.9)  # 内建作用域
    g_count_ = 0  # 全局作用域
    def outer():
        o_count = 1  # 闭包函数外的函数中
        def inner():
            i_count = 2  # 局部作用域
    ```
	+ gobal
		+ 当内部作用域想修改外部作用域的变量时
		```
        num = 1
        def fun1():
            global num  # 需要使用 global 关键字声明
            print(num)
            num = 123
            print(num)
        fun1()
        # output
        1
		123
        ```
	+ nonlocal
		+ 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
		```
        def outer():
            num = 10
            def inner():
                nonlocal num   # nonlocal关键字声明
                num = 100
                print(num)
            inner()
            print(num)
        outer()
        # output
        100
		100
        ```
	+ error example
		```
        a = 10
        def test():
            a = a + 1
            print(a)
        test()
        # UnboundLocalError: local variable 'a' referenced before assignment
        # 错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改
        ```

## 8.OOP
+ type() and instance()
	+ type()不会认为子类是一种父类类型
	+ isinstance()会认为子类是一种父类类型

+ Define
	+ 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
	+ 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
	+ 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
	+ 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
	+ 实例变量：定义在方法中的变量，只作用于当前实例的类。
	+ 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
	+ 实例化：创建一个类的实例，类的具体对象。
	+ 方法：类中定义的函数。
	+ 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法

+ 类定义

+ 类对象
	+ 很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
	```
    class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
	x = Complex(3.0, -4.5)
	print(x.r, x.i)   # 输出结果：3.0 -4.5
    ```
+ (???)self代表类的实例，而非类
	+ self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的
+ 类的方法
	+ 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
+ 继承
	+ 形式
	```
    class DerivedClassName(BaseClassName1):
        <statement-1>
        .
        .
        .
        <statement-N>
    ```
    + 需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法
	+ （？？？）BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。
	+ （？？？）除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
	```
    class DerivedClassName(modname.BaseClassName):
    ```

+ 多继承
	+ 格式
	```
    class DerivedClassName(Base1, Base2, Base3):
        <statement-1>
        .
        .
        .
        <statement-N>
    ```
    + 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法
+ 方法重写
	```
    class Parent:        # 定义父类
       def myMethod(self):
          print ('调用父类方法')

        class Child(Parent): # 定义子类
           def myMethod(self):
              print ('调用子类方法')

        c = Child()          # 子类实例
        c.myMethod()         # 子类调用重写方法
        super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
	# output
    调用子类方法
	调用父类方法
    ```
    + super() 函数是用于调用父类(超类)的一个方法
+ 类属性与方法
	+ 类的私有属性
		+ __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs
	+ 类的方法
		+ 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
		+ self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self
	+ 类的私有方法
		+ __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_method
	+ 类的专有方法
		+ __init__ : 构造函数，在生成对象时调用
		+ __del__ : 析构函数，释放对象时使用
		+ __repr__ : 打印，转换
		+ __setitem__ : 按照索引赋值
		+ __getitem__: 按照索引获取值
		+ __len__: 获得长度
		+ __cmp__: 比较运算
        + __call__: 函数调用
        + __add__: 加运算
        + __sub__: 减运算
        + __mul__: 乘运算
        + __div__: 除运算
        + __mod__: 求余运算
        + __pow__: 乘方
	+ 运算符重载
		+ 例子
		```
        class Vector:
           def __init__(self, a, b):
              self.a = a
              self.b = b

           def __str__(self):
              return 'Vector (%d, %d)' % (self.a, self.b)

           def __add__(self,other):
              return Vector(self.a + other.a, self.b + other.b)

        v1 = Vector(2,10)
        v2 = Vector(5,-2)
        print (v1 + v2)
        # output
        Vector(7,8)
        ```
+ 高级编程
	+ ref : https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000
	+ __slot__
	+ @property
	+ 定制类
	+ 元类

## 9.Error and Exception
+ SyntaxError : 语法错误
+ Exception : 异常
	+ 异常处理
        ```
        try:
            f = open('myfile.txt')
            s = f.readline()
            i = int(s.strip())
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
        ```
        + try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行
        	+ 使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常
        ```
        for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()
        ```
	+ 抛出异常
		+ 抛出一个指定的异常
		```
        $ raise NameError('HiThere')
        # output
        Traceback (most recent call last):
        	File "<stdin>", line 1, in ?
        NameError: HiThere
        ```
        + raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
        ```
        $ try:
        raise NameError('HiThere')
    		except NameError:
        print('An exception flew by!')
        raise
        # output
        An exception flew by!
        Traceback (most recent call last):
        	File "<stdin>", line 2, in ?
        NameError: HiThere
        ```
	+ 自定义异常
	+ finally

## Magic Function
+ property
+ Iterator

## 10.Module
+ import 与 from...import
+ 将整个模块(somemodule)导入，格式为： import somemodule
+ 从某个模块中导入某个函数,格式为： from somemodule import somefunction
+ 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
+ 将某个模块中的全部函数导入，格式为： from somemodule import *
    ```
    import sys
    print('================Python import mode==========================');
    print ('命令行参数为:')
    for i in sys.argv:
        print (i)
    print ('\n python 路径为',sys.path)

    from sys import argv,path  #  导入特定的成员
    print('================python from import===================================')
    print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

    ```
+ import
	+ 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行
    + 搜索路径
        + 搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块
        + 搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改
        + 搜索路径被存储在sys模块中的path变量，做一个简单的实验，在交互式解释器中，输入以下代码
        ```
        import sys
		sys.path
		['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x8664-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']
        ```
        + sys.path 输出是一个列表，其中第一项是空串''，代表当前目录
        + 若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录
        + 当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉
        ```
        例子
        现在，在解释器的当前目录或者 sys.path 中的一个目录里面来创建一个fibo.py的文件，代码如下：
        # 斐波那契(fibonacci)数列模块
        def fib(n):    # 定义到 n 的斐波那契数列
            a, b = 0, 1
            while b < n:
                print(b, end=' ')
                a, b = b, a+b
            print()

        def fib2(n): # 返回到 n 的斐波那契数列
            result = []
            a, b = 0, 1
            while b < n:
                result.append(b)
                a, b = b, a+b
            return result
        然后进入Python解释器，使用下面的命令导入这个模块：

        $ import fibo
        这样做并没有把直接定义在fibo中的函数名称写入到当前符号表里，只是把模块fibo的名字写到了那里。

        可以使用模块名称来访问函数：

        $ fibo.fib(1000)
        1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
        $ fibo.fib2(100)
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        $ fibo.__name__
        'fibo'
        如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：

        $ fib = fibo.fib
        $ fib(500)
        1 1 2 3 5 8 13 21 34 55 89 144 233 377
        ```

+ from ... import
	+ 这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来
	```
    $ from fibo import fib, fib2
	$ fib(500)
	1 1 2 3 5 8 13 21 34 55 89 144 233 377
    ```
+ （？？？）深入模块

+ （？？？）__name__ 属性
	+ 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入
	+ 一个模块被另一个程序第一次引入时，其主程序将运行。
	+ 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行
	```
    # Filename: using_name.py
    if __name__ == '__main__':
       print('程序自身在运行')
    else:
       print('我来自另一模块')

    $ python using_name.py
     程序自身在运行

    $ import using_name
    我来自另一模块
    ```

+ dir（）
	+ 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回

+ 包
	+ 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"
	+ 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B
	+ 就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况
	+ 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
		+ （？？？）主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块
		+ 当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值
	+ 导入
		 + 注意当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量
		 + import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了
		 + 反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字
	```
    # demo 1
    import sound.effects.echo
    sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
	# demo 2
    from sound.effects import echo
    echo.echofilter(input, output, delay=0.7, atten=4)
    # demo 3
    from sound.effects.echo import echofilter
    echofilter(input, output, delay=0.7, atten=4)
    ```
    + 从一个包中导入

## 11.IO
+ 输出格式美化
	+ str()： 函数返回一个用户易读的表达形式。
	+ repr()： 产生一个解释器易读的表达形式
	+ 两种方式输出平方立方表（1到10）
		```
        # demo1
        for x in range(1, 11):
			print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
		# 注意前一行 'end' 的使用
		print(repr(x*x*x).rjust(4))
        # demo2
        for x in range(1, 11):
			print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
        ```
	+ str.format
		+ 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
		```
        print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
		# output
        菜鸟教程网址： "www.runoob.com!"
		```
		+ 在括号中的数字用于指向传入对象在 format() 中的位置
		```
        print('{0} 和 {1}'.format('Google', 'Runoob'))
		# output
        Google 和 Runoob
		print('{1} 和 {0}'.format('Google', 'Runoob'))
		# output
        Runoob 和 Google
        ```
        + 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
        ```
        print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
		# output
        菜鸟教程网址： www.runoob.com
        ```
        + 位置及关键字参数可以任意的结合
        ```
        print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob',
                                                       other='Taobao'))
		# output
        站点列表 Google, Runoob, 和 Taobao
        ```
        + (???) '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
     	+ 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位
     	```
        import math
		print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
		# output
        常量 PI 的值近似为 3.142
        ```
     	+ 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用

+ 旧式字符串格式化
	+ % 操作符也可以实现字符串格式化
	```
    import math
	print('常量 PI 的值近似为：%5.3f。' % math.pi)
	# output
    常量 PI 的值近似为：3.142。
    ```
+ 读取键盘输入
	```
    str = input("请输入：");
	print ("你输入的内容是: ", str)
    #output
    请输入：AAA
	你输入的内容是:  AAA
    ```
+ 读写文件
	+ open 返回一个file对象
	+ open(filename, mode)
		+ filename：filename 变量是一个包含了你要访问的文件名称的字符串值
		+ mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)
		| mode | description |
		|--------|--------|
        | r  | 以**只读**方式打开文件。文件的指针将会放在文件的**开头**。这是默认模式 |
        | rb | 以二进制格式打开一个文件用于只读 |
        | r+ | 打开一个文件用于读写。文件指针将会放在文件的开头 |
        | rb+ | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头 |
        | w | 打开一个文件只用于**写入**。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件 |
        | wb | 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件 |
        | w+ | 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件 |
        | wb+ | 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件 |
        | a	 | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入 |
		| ab | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入 |
		| a+ | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写 |
		| ab+ | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写 |

		![](http://www.runoob.com/wp-content/uploads/2013/11/2112205-861c05b2bdbc9c28.png)
		+ Diff
		| 模式 | r | r+ | w | w+ | a | a+ |
        |-----|---|----|---|----|----|---|
		| 读	 | + | +  |    | +	|   | + |
        | 写	 |   | +  | +  | +	| + | + |
		| 创建 |   |    | + | +  | +  | + |
        | 覆盖 |   |    | + | +  |    |   |
        | 指针在开始 | + | +  | + | +  |   |  |
        | 指针在结束 |  |   |  |   | +  | +  |

+ 文件对象的方法
	+ f.read()
		+ 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回
		+ size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回
	+ f.readline()
		+ f.readline() 会从文件中读取单独的一行。换行符为 '\n'。
		+ f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
	+ f.readlines()
		+ f.readlines() 将返回该文件中包含的所有行
		+ 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割
		```
        f = open("/tmp/foo.txt", "r")
		str = f.readlines()
		print(str)
		# 关闭打开的文件
		f.close()
        ```
	+ f.write
		+ f.write(string) 将 string 写入到文件中, 然后返回写入的字符数
		+ 如果要写入一些不是字符串的东西, 那么将需要先进行转换
	+ f.tell()
		+ 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
	+ f.seek()
		+ 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
		+ from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
			+ seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
			+ seek(x,1) ： 表示从当前位置往后移动x个字符
			+ seek(-x,2)：表示从文件的结尾往前移动x个字符
	+ f.close()
+ pickle模块
	+ 实现了基本的数据序列和反序列化
	+ 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
	+ 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
	+ 基本接口
		+ pickle.dump(obj, file, [,protocol])
		+ x = pickle.load(file)
## 12.File
+ file.close()
	+ 关闭文件。关闭后文件不能再进行读写操作
+ file.flush()
	+ 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入
+ file.fileno()
	+ 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上
+ file.isatty()
	+ 如果文件连接到一个终端设备返回 True，否则返回 False
+ file.next()
	+ 返回文件下一行
+ file.read([size])
	+ 从文件读取指定的字节数，如果未给定或为负则读取所有
+ file.readline([size])
	+ 读取整行，包括 "\n" 字符
+ file.readlines([sizeint])
	+ 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
+ file.seek(offset[, whence])
	+ 设置文件当前位置
+ file.tell()
	+ 返回文件当前位置
+ file.truncate([size])
	+ 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小
+ file.write(str)
	+ 将字符串写入文件，没有返回值
+ file.writelines(sequence)
	+ 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符

## 13. OS
+ os 模块提供了非常丰富的方法用来处理文件和目录
+ os.access(path, mode)
	+ 检验权限模式
+ os.chdir(path)
	+ 改变当前工作目录
+ os.chflags(path, flags)
	+ 设置路径的标记为数字标记。
+ os.chmod(path, mode)
	+ 更改权限
+ os.chown(path, uid, gid)
	+ 更改文件所有者
+ os.chroot(path)
	+ 改变当前进程的根目录
+ os.close(fd)
	+ 关闭文件描述符 fd
+ os.closerange(fd_low, fd_high)
	+ 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
+ os.dup(fd)
	+ 复制文件描述符 fd
+ os.dup2(fd, fd2)
	+ 将一个文件描述符 fd 复制到另一个 fd2
+ os.fchdir(fd)
	+ 通过文件描述符改变当前工作目录
+ os.fchmod(fd, mode)
	+ 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
+ os.fchown(fd, uid, gid)
	+ 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
+ os.fdatasync(fd)
	+ 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
+ os.fdopen(fd[, mode[, bufsize]])
	+ 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
+ os.fpathconf(fd, name)
	+ 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
+ os.fstat(fd)
	+ 返回文件描述符fd的状态，像stat()。
+ os.fstatvfs(fd)
	+ 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
+ os.fsync(fd)
	+ 强制将文件描述符为fd的文件写入硬盘。
+ os.ftruncate(fd, length)
	+ 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
+ os.getcwd()
	+ 返回当前工作目录
+ os.getcwdu()
	+ 返回一个当前工作目录的Unicode对象
+ os.isatty(fd)
	+ 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
+ os.lchflags(path, flags)
	+ 设置路径的标记为数字标记，类似 chflags()，但是没有软链接
+ os.lchmod(path, mode)
	+ 修改连接文件权限
+ os.lchown(path, uid, gid)
	+ 更改文件所有者，类似 chown，但是不追踪链接。
+ os.link(src, dst)
	+ 创建硬链接，名为参数 dst，指向参数 src
+ os.listdir(path)
	+ 返回path指定的文件夹包含的文件或文件夹的名字的列表。
+ os.lseek(fd, pos, how)
	+ 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END_或者2则从文件尾部开始. 在unix，Windows中有效
+ os.lstat(path)
	+ 像stat(),但是没有软链接
+ os.major(device)
	+ 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
+ os.makedev(major, minor)
	+ 以major和minor设备号组成一个原始设备号
+ os.makedirs(path[, mode])
	+ 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
+ os.minor(device)
	+ 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
+ os.mkdir(path[, mode])
	+ 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
+ os.mkfifo(path[, mode])
	+ 创建命名管道，mode 为数字，默认为 0666 (八进制)
+ os.mknod(filename[, mode=0600, device])
	+ 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
+ os.open(file, flags[, mode])
	+ 打开一个文件，并且设置需要的打开选项，mode参数是可选的
+ os.openpty()
	+ 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
+ os.pathconf(path, name)
	+ 返回相关文件的系统配置信息。
+ os.pipe()
	+ 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
+ os.popen(command[, mode[, bufsize]])
	+ 从一个 command 打开一个管道
+ os.read(fd, n)
	+ 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
+ os.readlink(path)
	+ 返回软链接所指向的文件
+ os.remove(path)
	+ 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
+ os.removedirs(path)
	+ 递归删除目录。
+ os.rename(src, dst)
	+ 重命名文件或目录，从 src 到 dst
+ os.renames(old, new)
	+ 递归地对目录进行更名，也可以对文件进行更名。
+ os.rmdir(path)
	+ 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
+ os.stat(path)
	+ 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
+ os.stat_float_times([newvalue])
	+ 决定stat_result_是否以float对象显示时间戳
+ os.statvfs(path)
	+ 获取指定路径的文件系统统计信息
+ os.symlink(src, dst)
	+ 创建一个软链接
+ os.tcgetpgrp(fd)
	+ 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
+ os.tcsetpgrp(fd, pg)
	+ 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
+ os.tempnam([dir[, prefix]])
	+ Python3 中已删除。返回唯一的路径名用于创建临时文件。
+ os.tmpfile()
	+ Python3 中已删除。返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
+ os.tmpnam()
	+ Python3 中已删除。为创建一个临时文件返回一个唯一的路径
+ os.ttyname(fd)
	+ 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
+ os.unlink(path)
	+ 删除文件路径
+ os.utime(path, times)
	+ 返回指定的path文件的访问和修改的时间。
+ os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
	+ 输出在文件夹中的文件名通过在树中游走，向上或者向下。
+ os.write(fd, str)
	+ 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度