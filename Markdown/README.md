# Markdown

## 目录

用 `[TOC]`来生成目录

[TOC]

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

+ Pass



## 代码块

代码块语法遵循标准markdown代码，例如：
``` python
print([i for i in range(101)])
```



## 数学公式

+ 使用MathJax渲染*LaTex* 数学公式，详见[math.stackexchange.com][1].
  - 行内公式，数学公式为：$\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$。
  - 块级公式
     $$	x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

+ 符号
  + 上标 $x^2$
  + 整体 $Z^{ab}$
  + 分号 $\frac{x}{y}$
  + 开方 $\sqrt[n]{x}$
  + 省略号 $\ldots$ $\cdots$
  + 矢量 $\vec{a}$
  + 积分  $\int_0^2 x^2 {\rm d}x$
  + 极限 $\lim\limits_{n \rightarrow +\infty} \frac{1}{n(n+1)}$
  + 累加 $\sum_{i=0}^n \frac{1}{i^2}$
  + 累乘 $\prod_{i=0}^{n} \frac{1}{i^2}$


## 希腊字母

$\alpha, \beta, \gamma, \Gamma, \delta, \Delta, \epsilon, \varepsilon, \zeta, \eta, \theta, \Theta , \vartheta, \iota, \kappa, \lambda, \Lambda, \mu, \nu, \xi, \Xi, \pi, \Pi, \varpi, \rho, \varrho, \sigma, \Sigma, \varsigma, \tau, \upsilon, \Upsilon, \phi, \Phi, \varphi, \chi, \psi, \Psi, \omega, \Omega$

## 关系运算符

$\pm \times \div \mid
 \nmid
 \cdot
 \circ
 \ast
 \bigodot
 \bigotimes
 \bigoplus
 \leq
 \geq
 \neq
 \approx
 \equiv
 \sum
 \prod
 \coprod$

## 集合运算符

 $\emptyset
\in
\notin
\subset
\supset
\subseteq
\supseteq
\bigcap
\bigcup
\bigvee
\bigwedge
\biguplus
\bigsqcup$

## 对数运算符

$\log, \lg, \ln$

## 三角运算符

$\bot, \angle, 30^\circ, \sin, \cos, \tan, \cot, \sec, \csc$

## 微积分运算符

$\prime, \int, \iint, \iiint, \iiiint, \oint, \lim, \infty, \nabla$

## 逻辑运算符号

 $\because, \therefore, \forall, \exists, \not=, \not-, \not>, \not\subset$

## 戴帽符号

$\hat{u}, \check{u}, \breve{u}$

## 连线符号

$\overline{a+b+c+d}$

$\underline{a+b+c+d}​$

$\overbrace{a+\underbrace{b+c}*{1.0}+d}^{2.0}$

## 箭头符号

$\uparrow
 \downarrow
 \Uparrow
 \Downarrow
 \rightarrow
 \leftarrow
 \Rightarrow
 \Leftarrow
 \longrightarrow
 \longleftarrow
 \Longrightarrow
 \Longleftarrow​$

## 图表

+ UML图:
	+ 可以渲染序列图
+ 流程图
- 关于 **序列图** 语法，参考 [这儿][4]
- 关于 **流程图** 语法，参考 [这儿][5]

## Reference

http://math.stackexchange.com/

https://github.com/jmcmanus/pagedown-extra "Pagedown Extra"

http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference

http://bramp.github.io/js-sequence-diagrams/

http://adrai.github.io/flowchart.js/

https://github.com/benweet/stackedit

https://linux.cn/article-7623-1.html


