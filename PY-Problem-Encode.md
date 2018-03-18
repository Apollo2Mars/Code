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