```
# lineSeg = line.split('/[\w]+')
lineSeg = re.split('/\w+', line)
```
python 字符串处理
http://www.cnblogs.com/huangcong/archive/2011/08/29/2158268.html


## encode decode
```
http://www.cnblogs.com/DxSoft/archive/2010/05/21/1741043.html
python的str，unicode对象的encode和decode方法（转）
python的str，unicode对象的encode和decode方法 
python中的str对象其实就是"8-bit string" ，字节字符串，本质上类似java中的byte[]。 
而python中的unicode对象应该才是等同于java中的String对象，或本质上是java的char[]。 

对于
Python代码 
1. s="你好"    
2. u=u"你好"   
    s="你好" 
    u=u"你好" 
\1. s.decode方法和u.encode方法是最常用的， 
简单说来就是，python内部表示字符串用unicode（其实python内部的表示和真实的unicode是有点差别的，对我们几乎透明，可不考虑），和人交互的时候用str对象。 
s.decode -------->将s解码成unicode，参数指定的是s本来的编码方式。这个和unicode(s,encodename)是一样的。 
u.encode -------->将unicode编码成str对象，参数指定使用的编码方式。 
助记：decode to unicode from parameter 
encode to parameter from unicode 
只有decode方法和unicode构造函数可以得到unicode对象。 
上述最常见的用途是比如这样的场景，我们在python源文件中指定使用编码cp936， 
# coding=cp936或#-- coding:cp936 --或#coding:cp936的方式（不写默认是ascii编码） 
这样在源文件中的str对象就是cp936编码的，我们要把这个字符串传给一个需要保存成其他编码的地方（比如xml的utf-8,excel需要的utf-16） 
通常这么写： 
strobj.decode("cp936").encode("utf-16") 
You typically encode a unicode string whenever you need to use it for IO, for instance transfer it over the network, or save it to a disk file. 
To convert a string of bytes to a unicode string is known as decoding. Use unicode('...', encoding) or '...'.decode(encoding). 
You typically decode a string of bytes whenever you receive string data from the network or from a disk file. 
1. 第一条已经写了不少，因为是最常用到的，基本不用怎么解释。我重点想说的是这第二条。 
   似乎有了unicode对象的encode方法和str的decode方法就足够了。奇怪的是，unicode也有decode，而str也有 
   encode，到底这两个是干什么的。 
   用处1 
   str本身已经是编码过的了，如果再encode很难想到有什么用（通常会出错的） 
   先解释下这个 
   str.encode(e) is the same as unicode(str).encode(e). 
   This is useful since code that expects Unicode strings should also work when it is passed 
   ASCII-encoded 8-bit strings(from Guido van Rossum) 
   python之父的这段话大概意思是说encode方法本来是被unicode调的，但如果不小心被作为str对象的方法调，并且这个str对象正好 
   是ascii编码的（ascii这一段和unicode是一样的），也应该让他成功。这就是str.encode方法的一个用处（我觉得这个基本等于没用） 
   类似地，把光用ascii组成的unicode再decode一回是一样的道理，因为好像几乎任何编码里ascii都原样没变。因此这样的操作等于没做。 
   u"abc".decode("gb2312")和u"abc"是相等的。 
   用处2 
   非字符的编码集non-character-encoding-codecs，这些只在python中定义，离开python就没意义（这个来自python的官方文档） 
   并且也不是人类用的语言，呵呵。 
   比如

Python代码 

1. '\n'.encode('hex')=='0a'    
2. u'\n'.encode('hex')=='0a'  
3. '0a'.decode('hex')=='\n'  
4. u'0a'.decode('hex')=='\n'  

    '\n'.encode('hex')=='0a' 
    u'\n'.encode('hex')=='0a'
    '0a'.decode('hex')=='\n'
    u'0a'.decode('hex')=='\n'

可见名为hex的编码可以讲字符表示（当然了，必须是ascii内的）和十六进制表示之间转换 
另外还有很多好玩的，比如：base64通俗的讲是号称防君子不防小人的给邮件的编码，gzip大概是指压缩吧（这是我猜的），rot13回转13等，不知者google之 
关于这些，官方有个详细的表格，在http://docs.python.org/library/codecs.html中的Standard Encodings一节中，前一个表格是基于字符的编码，第二个表格 
就是这里的非字符的编码。关于这些特殊编码，官方一句说明： 
For the codecs listed below, the result in the “encoding” direction is always a byte string. 
The result of the “decoding” direction is listed as operand type in the table. 
encode的结果一定是一个byte的str，而decode的结果在表中operand一列。 
参考 
Converting Between Unicode and Plain Strings 在Unicode和普通字符串之间转换 
http://wiki.woodpecker.org.cn/moin/PyCkBk-3-18 
what’s the difference between encode/decode? (python 2.x) 
http://stackoverflow.com/questions/447107/whats-the-difference-between-encode-decode-python-2-x 
http://docs.python.org/library/codecs.html 
编码声明的作用 
请参考http://www.python.org/dev/peps/pep-0263/ 
声明源文件中将出现非ascii编码； 
在高级的IDE中，IDE会将你的文件格式保存成你指定编码格式。 
决定源码中类似于u'哈'这类声明的将'哈'解码成unicode所用的编码格式，也是一个比较容易让人迷惑的地方。 
（java不需要声明的原因在于：java中默认是本地编码而py中默认是ascii，搞得python更易出错， 
并且，java编译的时候还有个指定编码的参数encoding） 
文件的编码格式决定了在该源文件中声明的字符串的编码格式，例如：

Python代码 
1. str = '哈哈'    
2. print repr(str)   
    str = '哈哈' 
    print repr(str) 
a.如果文件格式为utf-8，则str的值为：'\xe5\x93\x88\xe5\x93\x88'（哈哈的utf-8编码） 
b.如果文件格式为gbk，则str的值为：'\xb9\xfe\xb9\xfe'（哈哈的gbk编码） 
我的理解：文件编码格式保存后没有地方指明，只有靠聪明或笨的编辑器，编译器去猜。而声名就更精确一些。 
让两者一致了总不会错。 
其实好多其他语言或应用中也是类似的decode和encode概念，比如在java中String的涉及的编码转换及jdk中的工具native2ascii， 
好像javascript也有这个，记不清楚了。
```
