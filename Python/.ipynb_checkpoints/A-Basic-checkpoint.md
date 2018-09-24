# Python
## Reference
+ http://javayhu.me/python/
+ http://www.runoob.com/python/python-tutorial.html

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
	+ 以下划线开头的标识符是有特殊意义的
	+ 以单下划线开头 \_foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入
	+ 以双下划线开头的 \_\_foo 代表类的私有成员
	+ 以双下划线开头和结尾的 \_\_foo \_\_  代表 Python 里特殊方法专用的标识，如\_\_init()\_\_ 代表类的构造函数
+ 保留字
	+ 下面的列表显示了在Python中的保留字
	+ 这些保留字不能用作常数或变数，或任何其他标识符名称
	+ 所有 Python 的关键字只包含小写字母
| 		 | 		  |		|
|--------|--------| --- |
|and	| exec	| not |
|assert	| finally	|or |
|break |	for	| pass|
|class	| from	| print|
|continue	| global	| raise|
|def	|if	| return|
|del |	import	| try|
|elif	| in |	while|
|else	|is |	with|
|except|	lambda |	yield|

+ 引号
- Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
- 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

```{.python .input}
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
```

+ 注释
	+ 单行 #
	+ 多行 ``` 和 “”“
+ 行与缩进
+ 多行语句
	+ 使用反斜杠(\\)来实现多行语句
	+ 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\\)
+ 同一行显示多条语句
	+ Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
	```
    import sys; x = 'runoob'; sys.stdout.write(x + '\n')
    ```
+ 用户交互
	+ 下面的程序执行后就会等待用户输入，按回车键后就会退出：
	```
    input("\n\n按下 enter 键后退出。")
    ```
    ```
    >>> input("type your input : ")
    type your input : hello world
    'hello world'
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

## Next to do
+ reorganize this blog according to http://javayhu.me/python/
