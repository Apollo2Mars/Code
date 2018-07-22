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