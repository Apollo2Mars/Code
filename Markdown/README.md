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



### 括号

| 功能           | 语法                                         | 显示         |
| -------------- | -------------------------------------------- | ------------ |
| 圆括号，小括号 | \left( \frac{a}{b} \right)                   | (ab)(ab)     |
| 方括号，中括号 | \left[ \frac{a}{b} \right]                   | [ab][ab]     |
| 花括号，大括号 | \left\{ \frac{a}{b} \right\}                 | {ab}{ab}     |
| 尖括号         | \left \langle \frac{a}{b} \right \rangle     | ⟨ab⟩⟨ab⟩     |
| 单竖线，绝对值 | \left \| \frac{a}{b} \right\|                | 丨abab丨     |
| 双竖线，范式   | \left \| \frac{a}{b} \right \|               | ‖‖ab‖‖‖ab‖   |
| 取整函数       | \left \lfloor \frac{a}{b} \right \rfloor     | ⌊ab⌋⌊ab⌋     |
| 取顶函数       | \left \lceil \frac{c}{d} \right \rceil       | ⌈cd⌉⌈cd⌉     |
| 斜线与反斜线   | \left / \frac{a}{b} \right \backslash        | /ab\/ab\     |
| 上下箭头       | \left \uparrow \frac{a}{b} \right \downarrow | ↑⏐⏐ab⏐↓⏐↑ab↓ |
| 混合括号1      | \left [ 0,1 \right )                         | [0,1)[0,1)   |
| 混合括号2      | \left \langle \psi \right\|                  | ⟨ψ‖⟨ψ‖       |
| 单左括号       | \left \{ \frac{a}{b} \right .                | {ab{ab       |
| 单右括号       | \left . \frac{a}{b} \right \}                | ab}          |

### 希腊字母

| 希腊字母(小写) | 输入                  | 希腊字母(大写) | 输入     |
| -------------- | --------------------- | -------------- | -------- |
| α              | \alpha                | Α              | A        |
| β              | \beta                 | Β              | B        |
| γ              | \gamma                | Γ              | \Gamma   |
| δ              | \delta                | Δ              | \Delta   |
| ε或ϵ           | \epsilon或\varepsilon | Ε              | E        |
| ζ              | \zeta                 | Ζ              | Z        |
| η              | \eta                  | Η              | H        |
| θ或ϑ           | \theta或\vartheta     | Θ              | \Theta   |
| ι              | \iota                 | Ι              | I        |
| κ              | \kappa                | Κ              | K        |
| λ              | \lambda               | Λ              | \Lambda  |
| μ              | \mu                   | Μ              | M        |
| ν              | \nu                   | Ν              | N        |
| ξ              | \xi                   | Ξ              | \Xi      |
| ο              | o                     | Ο              | O        |
| π或ϖ           | \pi或\varpi           | Π              | \Pi      |
| ρ或ϱ           | \rho或\varrho         | Ρ              | P        |
| σ或ς           | \sigma或\varsigma     | Σ              | \Sigma   |
| τ              | \tau                  | Τ              | T        |
| υ              | \upsilon              | Υ              | \Upsilon |
| φ或φ           | \phi或\varphi         | Φ              | \Phi     |
| χ              | \chi                  | Χ              | X        |
| ψ              | \psi                  | Ψ              | \Psi     |
| ω              | \omega                | Ω              | \Omega   |



### 数学运算符

| 数学字符 | 输入            | 数学字符 | 输入           |
| -------- | --------------- | -------- | -------------- |
| ±        | \pm             | ×        | \times         |
| ÷        | \div            | \|       | \mid           |
| ∤∤       | \nmid           | ⋅        | \cdot          |
| ∘        | \circ           | ∗        | \ast           |
| ⨀        | \bigodot        | ⨂        | \bigotimes     |
| ⨁        | \bigoplus       | ≤        | \leq           |
| ≥        | \geq            | ≠        | \neq           |
| ≈        | \approx         | ≡        | \equiv         |
| ∑        | \sum            | ∏        | \prod          |
| ∐        | \coprod         | ∅        | \emptyset      |
| ∈        | \in             | ∉        | \notin         |
| ⊂        | \subset         | ⊃        | \supset        |
| ⊆        | \subseteq       | ⊇        | \supseteq      |
| ⋂        | \bigcap         | ⋃        | \bigcup        |
| ⋁        | \bigvee         | ⋀        | \bigwedge      |
| ⨄        | \biguplus       | ⨆        | \bigsqcup      |
| log      | \log            | lg       | \lg            |
| ln       | \ln             | ⊥        | \bot           |
| ∠        | \angle          | 30^∘     | 30 ^ \circ     |
| sin      | \sin            | cos      | \cos           |
| tan      | \tan            | cot      | \cot           |
| ′        | \prime          | ∫        | \int           |
| ∬        | \iint           | ∭        | \iiint         |
| ⨌        | \iiiint         | ∮        | \oint          |
| lim      | \lim            | ∞        | \infty         |
| ∇        | \nabla          | ∵        | \because       |
| ∴        | \therefore      | ∀        | \forall        |
| ∃        | \exists         | ≠        | \not=          |
| ≯        | \not>           | ⊄        | \not\subset    |
| ŷ        | \hat{y}         | yˇ       | \check{y}      |
| y˘       | \breve{y}       | sec      | \sec           |
| ↑        | \uparrow        | ↓        | \downarrow     |
| ⇑        | \Uparrow        | ⇓        | \Downarrow     |
| →        | \rightarrow     | ←        | \leftarrow     |
| ⇒        | \Rightarrow     | ⇐        | \Leftarrow     |
| ⟶        | \longrightarrow | ⟵        | \longleftarrow |
| ⟹        | \Longrightarrow | ⟸        | \Longleftarrow |
|          | \quad           | #        | #              |
|          |                 |          |                |
|          |                 |          |                |



## 连线符号

$\overline{a+b+c+d}$

$\underline{a+b+c+d}$

$\overbrace{a+\underbrace{b+c}*{1.0}+d}^{2.0}$

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
https://www.rdtoc.com/tutorial/markdown-latex-tutorial.html

[多行公式] https://www.cnblogs.com/nowgood/p/Latexstart.html
