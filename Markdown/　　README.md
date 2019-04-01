# Markdown

## Reference
+ 数学公式：
	+ https://blog.csdn.net/xingxinmanong/article/details/78528791

## 快捷键

 - 加粗    `Ctrl + B`
 - 斜体    `Ctrl + I`
 - 引用    `Ctrl + Q`
 - 插入链接    `Ctrl + L`
 - 插入代码    `Ctrl + K`
 - 插入图片    `Ctrl + G`
 - 提升标题    `Ctrl + H`
 - 有序列表    `Ctrl + O`
 - 无序列表    `Ctrl + U`
 - 横线    `Ctrl + R`
 - 撤销    `Ctrl + Z`
 - 重做    `Ctrl + Y`


## 表格

**Markdown　Extra**　表格语法：

项目     | 价格
-------- | ---
Computer | $1600
Phone    | $12
Pipe     | $1

可以使用冒号来定义对齐方式：

| 项目      |    价格 | 数量  |
| :-------- | --------:| :--: |
| Computer  | 1600 元 |  5   |
| Phone     |   12 元 |  12  |
| Pipe      |    1 元 | 234  |

## 列表



## 代码块
代码块语法遵循标准markdown代码，例如：
``` python
@requires_authorization
def somefunc(param1='', param2=0):
    '''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1) or None
class SomeClass:
    pass
>>> message = '''interpreter
... prompt'''
```

### 脚注


## 目录
用 `[TOC]`来生成目录：

[TOC]

## 数学公式
+ 使用MathJax渲染*LaTex* 数学公式，详见[math.stackexchange.com][1].
	- 行内公式，数学公式为：$\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$。
	- 块级公式
			$$	x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
	- 更多LaTex语法请参考 [这儿][3].
		​	
			$ \uparraw$
		​	$\uparrow \downarrow \leftarrow \rightarrow \Uparrow \Downarrow \Leftarrow \Rightarrow \longleftarrow \longrightarrow \Longleftarrow \Longrightarrow $$
+ 符号
	+ 箭头
	

## 图表
+ UML图:
	+ 可以渲染序列图
+ 流程图
- 关于 **序列图** 语法，参考 [这儿][4]
- 关于 **流程图** 语法，参考 [这儿][5]

---------
[1]: http://math.stackexchange.com/
[2]: https://github.com/jmcmanus/pagedown-extra "Pagedown Extra"
[3]: http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
[4]: http://bramp.github.io/js-sequence-diagrams/
[5]: http://adrai.github.io/flowchart.js/
[6]: https://github.com/benweet/stackedit
