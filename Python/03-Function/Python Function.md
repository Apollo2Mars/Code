# Python Function
## Reference
+ 函数定义
	+ 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()
	+ 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
	+ 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
	+ 函数内容以冒号起始，并且缩进。
	+ return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None
+ 参数传递
	+ 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身

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

	+ 缺省参数
		+ pass 
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

        输出:
        10
        输出:
        70
        60
	50
        ```
+ return
	+ 不带参数值的return语句返回None

+ 匿名函数 (def 的简化版)
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

+ 变量作用域(???)
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
	+ global
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
