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