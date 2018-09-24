# Module
## import
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

+ import一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行

## 搜索路径
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
+ **当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉**


## 深入模块