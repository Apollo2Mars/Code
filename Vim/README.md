[TOC]



# Basic Operation of Vim

## 全选

- 全选（高亮显示）：按esc后，然后ggvG或者ggVG
  全部复制：按esc后，然后ggyG
  全部删除：按esc后，然后dG
  解析：
  gg：是让光标移到首行，在vim才有效，vi中无效 
  v ： 是进入Visual(可视）模式 
  G ：光标移到最后一行 
  选中内容以后就可以其他的操作了，比如： 
  d  删除选中内容 
  y  复制选中内容到0号寄存器 
  "+y  复制选中内容到＋寄存器，也就是系统的剪贴板，供其他程序用 

## 复制

yy     复制一行，此命令前可跟数字，标识复制多行，如6yy，表示从当前行开始复制6行
yw     复制一个字
y$     复制到行末

\+y  复制到+寄存器



## 移动

1、左移h、右移l、下移j、上移k
2、向下翻页ctrl + f，向上翻页ctrl + b
3、向下翻半页ctrl + d，向上翻半页ctrl + u
4、移动到行尾$，移动到行首0（数字），移动到行首第一个字符处^
5、移动光标到下一个句子 ），移动光标到上一个句子（
6、移动到段首{，移动到段尾}
7、移动到下一个词w，移动到上一个词b
8、移动到文档开始gg，移动到文档结束G
9、移动到匹配的{}.().[]处%
10、跳到第n行 ngg 或 nG 或 :n
11、移动光标到屏幕顶端H，移动到屏幕中间M，移动到底部L
12、读取当前字符，并移动到本屏幕内下一次出现的地方 *
13、读取当前字符，并移动到本屏幕内上一次出现的地方 #



- h Move left
- j Move down
- k Move up
- l Move right
- w Move to next word
- W Move to next blank delimited word
- b Move to the beginning of the word
- B Move to the beginning of blank delimted word
- e Move to the end of the word
- E Move to the end of Blank delimited word
- ( Move a sentence back
- ) Move a sentence forward
- { Move a paragraph back
- } Move a paragraph forward
- 0 Move to the begining of the line
- $ Move to the end of the line
- 1G Move to the first line of the file
- G Move to the last line of the file
- nG Move to nth line of the file
- :n Move to nth line of the file
- fc Move forward to c
- Fc Move back to c
- H Move to top of screen
- M Move to middle of screen
- L Move to botton of screen
- % Move to associated ( ), { }, [ ]

## 查找替换
1、光标向后查找关键字 #或者g#
2、光标向前查找关键字 *或者g*
3、当前行查找字符 fx, Fx, tx, Tx
4、基本替换 :s/s1/s2 （将下一个s1替换为s2）
5、全部替换 :%s/s1/s2
6、只替换当前行 :s/s1/s2/g
7、替换某些行 :n1,n2 s/s1/s2/g
8、搜索模式为 /string，搜索下一处为n，搜索上一处为N
9、制定书签 mx, 但是看不到书签标记，而且只能用小写字母
10、移动到某标签处 `x，1旁边的键
11、移动到上次编辑文件的位置 `.
PS：.代表一个任意字符 *代表一个或多个字符的重复

## 编辑操作
1、光标后插入a, 行尾插入A
2、后插一行插入o，前插一行插入O
3、删除字符插入s， 删除正行插入S
4、光标前插入i，行首插入I
5、删除一行dd，删除后进入插入模式cc或者S
6、删除一个单词dw，删除一个单词进入插入模式cw
7、删除一个字符x或者dl，删除一个字符进入插入模式s或者cl
8、粘贴p，交换两个字符xp，交换两行ddp
9、复制y，复制一行yy
10、撤销u，重做ctrl + r，重复.
11、智能提示 ctrl + n 或者 ctrl + p
12、删除motion跨过的字符，删除并进入插入模式 c{motion}
13、删除到下一个字符跨过的字符，删除并进入插入模式，不包括x字符 ctx
14、删除当前字符到下一个字符处的所有字符，并进入插入模式，包括x字符，cfx
15、删除motion跨过的字符，删除但不进入插入模式 d{motion}
16、删除motion跨过的字符，删除但不进入插入模式，不包括x字符 dtx
17、删除当前字符到下一个字符处的所有字符，包括x字符 dfx
18、如果只是复制的情况时，将12-17条中的c或d改为y
19、删除到行尾可以使用D或C
20、拷贝当前行 yy或者Y
21、删除当前字符 x
22、粘贴 p
23、可以使用多重剪切板，查看状态使用:reg，使用剪切板使用”，例如复制到w寄存器，”wyy，或者使用可视模式v”wy
24、重复执行上一个作用使用.
25、使用数字可以跨过n个区域，如y3x，会拷贝光标到第三个x之间的区域，3j向下移动3行
26、在编写代码的时候可以使用]p粘贴，这样可以自动进行代码缩进
27、 >> 缩进所有选择的代码
28、 << 反缩进所有选择的代码
29、gd 移动到光标所处的函数或变量的定义处
30、K 在man里搜索光标所在的词
31、合并两行 J
32、若不想保存文件，而重新打开 :e!
33、若想打开新文件 :e filename，然后使用ctrl + ^进行文件切换



## 多行注释/多行缩进

- 首先按esc进入命令行模式下，按下Ctrl + v，进入列（也叫区块）模式
- 在行首使用上下键选择需要注释的多行
- 按下键盘（大写）“I”键，进入插入模式
- 然后输入注释符（“//”、“#”等)
- 最后按下“Esc”键。 注：在按下esc键后，会稍等一会才会出现注释，不要着急~~时间很短的 

## 删除多行注释

- 首先按esc进入命令行模式下，按下Ctrl + v, 进入列模式
- 选定要取消注释的多行
- 按下“x”或者“d”. 注意：如果是“//”注释，那需要执行两次该操作，如果是“#”注释，一次即可

## 多行删除

- 首先在命令模式下，输入“：set nu”显示行号； 2.通过行号确定你要删除的行； 3.命令输入“：32,65d”,回车键，32-65行就被删除了，很快捷吧



## 多行合并

- 按 ESC 进入 Normal 模式，移动游标定位到第 2 行的位置。
- 按 shift+j 就可以实现合并行的操作。

## vim 将文件所有行合并到一行

- 在 Normal Mode下执行
- ggvGJ
- gg 用于跳到行首
- v 转换成 visual 模式
- G 跳到最后一行

J 合并行



## 窗口操作
1、分隔一个窗口:split或者:vsplit
2、创建一个窗口:new或者:vnew
3、在新窗口打开文件:sf {filename}
4、关闭当前窗口:close
5、仅保留当前窗口:only
6、到左边窗口 ctrl + w, h
7、到右边窗口 ctrl + w, l
8、到上边窗口 ctrl + w, k
9、到下边窗口 ctrl + w, j
10、到顶部窗口 ctrl + w, t
11、到底部窗口 ctrl + w, b

## 宏操作
1、开始记录宏操作q[a-z]，按q结束，保存操作到寄存器[a-z]中
2、@[a-z]执行寄存器[a-z]中的操作
3、@@执行最近一次记录的宏操作

## 可视操作
1、进入块可视模式 ctrl + v
2、进入字符可视模式 v
3、进入行可视模式 V
4、删除选定的块 d
5、删除选定的块然后进入插入模式 c
6、在选中的块同是插入相同的字符 I<String>ESC

## 跳到声明
1、[[ 向前跳到顶格第一个{  
2、[] 向前跳到顶格第一个}
3、]] 向后跳到顶格的第一个{
4、]] 向后跳到顶格的第一个}
5、[{ 跳到本代码块的开头
6、]} 跳到本代码块的结尾

## 挂起操作
1、挂起Vim ctrl + z 或者 :suspend
2、查看任务 在shell中输入 jobs
3、恢复任务 fg [job number]（将后台程序放到前台）或者 bg [job number]（将前台程序放到后台）
4、执行shell命令 :!command
5、开启shell命令 :shell，退出该shell exit
6、保存vim状态 :mksession name.vim
7、恢复vim状态 :source name.vim
8、启动vim时恢复状态 vim -S name.vim

## 快捷键

![img](http://roclinux.cn/wp-content/uploads/2010/04/vi_tutorial.png)