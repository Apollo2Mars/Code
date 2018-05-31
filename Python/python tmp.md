## Reference websites:
+ http://blog.csdn.net/yzl11/article/details/53792416

## __XX

"""
  Class Secretive:
    def __inaccessible(self):
      print "Bet you can't see me..."
    def accessible(self):
      print "The secret message is:"
      self.__inaccessible(self)
"""

## __XX__
+ “__xx__”经常是操作符或本地函数调用的magic methods。在上面的例子中，提供了一种重写类的操作符的功能。
+ 在特殊的情况下，它只是python调用的hook。例如，__init__()函数是当对象被创建初始化时调用的;__new__()是用来创建实例。

-----------------------------
# Variable Parameter
+ 默认参数

```
def test_defargs(one, two = 2):
   print 'Required argument: ', one
   print 'Optional argument: ', two

test_defargs(1)
# result:
# Required argument: 1
# Optional argument: 2

test_defargs(1, 3)
# result:
# Required argument: 1
# Optional argument: 3
```

+  $*args 和 **Kwargs$
	+  $*args$ 使用方法
		+ 包含一个必须的参数

		```
        def test_args(first, *args):
   		print 'Required argument: ', first
   		for v in args:
     		 print 'Optional argument: ', v

		test_args(1, 2, 3, 4)
		# result:
		# Required argument: 1
		# Optional argument:  2
		# Optional argument:  3
		# Optional argument:  4
        ```
	+  $**kwargs$ 使用方法
		+ 同时包含一个必须的参数和*args列表

        ```
        def test_kwargs(first, *args, **kwargs):
   			print 'Required argument: ', first
   		for v in args:
      		print 'Optional argument (*args): ', v
   		for k, v in kwargs.items():
      		print 'Optional argument %s (*kwargs): %s' % (k, v)

		test_kwargs(1, 2, 3, 4, k1=5, k2=6)
		# results:
		# Required argument:  1
		# Optional argument (*args):  2
		# Optional argument (*args):  3
		# Optional argument (*args):  4
		# Optional argument k2 (*kwargs): 6
		# Optional argument k1 (*kwargs): 5
        ```
-----------------------------------------------------------------------
load和loads都是实现“反序列化”，区别在于（以Python为例）：

1.loads针对内存对象，即将Python内置数据序列化为字串

如使用json.dumps序列化的对象d_json=json.dumps({'a':1, 'b':2})，在这里d_json是一个字串'{"b": 2, "a": 1}'

d=json.loads(d_json)  #{ b": 2, "a": 1}，使用load重新反序列化为dict

2.load针对文件句柄

如本地有一个json文件a.json则可以d=json.load(open('a.json'))

相应的，dump就是将内置类型序列化为json对象后写入文件

JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。它基于 ECMAScript (w3c制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

----------------------------------------------------------------------
## Python super __init

## python类中super()和__init__()的区别
+ http://python.jobbole.com/86993/

--------------------------------------------------------------------
+ python中文编码问题的解决办法
https://yq.aliyun.com/articles/53575

+ 查看python的默认编码
```
    import sys
	print sys.getdefaultencoding()
```

+ 更改python默认编码
```
    import sys
	reload(sys)   #必须要reload
	sys.setdefaultencoding('utf-8')

+ 原文件编码声明
```
	#放在原文件第一行
	#coding=utf-8
```

+ UnicodeDecodeError解决办法
	+ 通常情况使用前面的两种方法，基本不会有什么问题。但是最近还是碰到编码的问题。
	+ 在往一个函数传递字符串时出现的错误：
		```
        exceptions.UnicodeDecodeError: ‘utf8’ codec can’t decode byte 0xce in position 0: invalid continuation byte
		```
	+ 解决办法：
		+ 对字符串进行unicode化,忽略错误，代码如下：
		```
		unicode( rst , errors='ignore')
        ```
		```
        with open(csv_file_name, 'r', encoding='utf-8', errors='ignore') as csv:
        ```
----------------------------------------------------------------------
+ before    
    + code
    ```
      parser = argparse.ArgumentParser()
      parser.add_argument('data_dir', type=str, help='Path to SQuAD data directory', default='../data/SQuAD')
      parser.add_argument('out_dir', type=str, help='Path to output file dir', default='../data/SQuAD')
      parser.add_argument('--split', type=str, help='Filename for train/dev split',
                          default='dev-v1.1')
      parser.add_argument('--workers', type=int, default=None)
      parser.add_argument('--tokenizer', type=str, default='corenlp')
    ```
  + error
    ```
      usage: SQuAD_json2python.py [-h] [--split SPLIT] [--workers WORKERS]
                            [--tokenizer TOKENIZER]
                            data_dir out_dir
      SQuAD_json2python.py: error: the following arguments are required: data_dir, out_dir
    ```
+ after
    + code
    ```
      parser = argparse.ArgumentParser()
      parser.add_argument('--data_dir', type=str, help='Path to SQuAD data directory', default='../data/SQuAD')
      parser.add_argument('--out_dir', type=str, help='Path to output file dir', default='../data/SQuAD')
      parser.add_argument('--split', type=str, help='Filename for train/dev split',
                          default='dev-v1.1')
      parser.add_argument('--workers', type=int, default=None)
      parser.add_argument('--tokenizer', type=str, default='corenlp')
    ```
  + result
    ```
      Loading dataset ../data/SQuAD/dev-v1.1.json
      Will write to file ../data/SQuAD/dev-v1.1-processed-corenlp.txt
    ```
+ parser.register()
	+ http://blog.csdn.net/a1964543590/article/details/69791760

    ```
    parser = argparse.ArgumentParser()#创建一个命令解析器的句柄
	#注册一个命令解析器参数类型,其中lambda v: v.lower()=="true"
	#是代表一个匿名函数的实现，主要判断获取到的参数v转换成小写后是否等于true
	parser.register("type", "bool", lambda v: v.lower() == "true")
	#这个接口主要是添加命令解析器命令。其中下面使用的type就是上面注册的类型(注意:bool 是带双引号的)
	parser.add_argument(
  	"--debug",
  	type="bool",
  	nargs="?",
  	const=True,
  	default=False,
  help="Use debugger to track down bad values during training")
    ```
---------------------------------------------------------------------------------------
## import 与 from import 的区别
  两个import语义有差异import datetime
  print(datetime.datetime.now())
  是引入整个datetime包from datetime import datetime
  print(datetime.now())
  是只引入datetime包里的datetime类所以import之后前者是datetime这个包可见 后者是datetime.datetime这个类可见


## 如何在某.py文件中调用其他.py内的函数
+ 假设名为A.py的文件需要调用B.py文件内的C(x,y)函数
+ 假如在同一目录下,则只需
	```
    import B
    if __name__ == "__main__":
        B.C(x,y)
	```

+ 若只需调用单个函数，也可以
	```
    from B import C
    if __name__ == "__main__":
        C(x,y)
	```

+ 若A.py和B.py位于不同的目录下，可以用以下方法 (假设B.py位于D盘的根目录下)
+ 引用所在路径
	```
    import sys
    sys.path.append('D:/')
    import B
    if __name__=="__main__":
        print B.pr(x,y)
	```
+ 使用imp
    ```
    import imp
    B=imp.load_source('B','D:/B.py')
    import B
    if __name__=="__main__":
        print B.pr(x,y)
    ```