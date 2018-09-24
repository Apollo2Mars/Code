# Python 面向对象

## 类的标识符
+ 以下划线开头的标识符是有特殊意义的
+ 以单下划线开头 \_foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入
+ 以双下划线开头的 \_\_foo 代表类的私有成员
+ 以双下划线开头和结尾的 \_\_foo \_\_  代表 Python 里特殊方法专用的标识，如\_\_init()\_\_ 代表类的构造函数

## 类相关
+ type() and instance()
	+ type()不会认为子类是一种父类类型
	+ isinstance()会认为子类是一种父类类型

+ 类的定义
	+ 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
	+ 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
	+ 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
	+ 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
	+ 实例变量：定义在方法中的变量，只作用于当前实例的类。
	+ 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
	+ 实例化：创建一个类的实例，类的具体对象。
	+ 方法：类中定义的函数。
	+ 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法

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
        <statement-N>
    ```
    + 需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法
	+ BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。
	+ 除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
    ```
    class DerivedClassName(modname.BaseClassName):
    ```

+ 多继承
	+ 格式
    ```
    class DerivedClassName(Base1, Base2, Base3):
        <statement-1>
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
		+ __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问
	+ 类的方法
		+ 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例
		+ self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self
	+ 类的私有方法
		+ __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用, 不能在类地外部调用
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
