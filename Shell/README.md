[TOC]

# Basic Operation of Linux

## apt

+ apt repository 添加/删除
    + 固定
    ```
    sudo add-apt-repository 'deb http://typora.io linux/'添加typora的远程仓库
    sudo apt-get update更新
    sudo apt-get install typora 安装
    ```
    + PPA
        + Ubuntu里，PPA代表一种非稳定版本到发布，喜欢尝试鲜到人一般会加入很多PPA源
            + https://blog.csdn.net/li_hai/article/details/8189290
    ```
    sudo add-apt-repository ppa:webupd8team/atom
    sudo apt-get update
    sudo apt-get install atom 
    ```



## LD_LIBRARY_PATH

+ https://blog.csdn.net/fengxinze/article/details/6940241



## Cat and Echo

- cat
  - 基本功能
    - 一次显示整个文件。$cat filename
    - 从键盘创建一个文件。$ cat > filename  
      - 只能创建新文件,不能编辑已有文件.
    - 将几个文件合并为一个文件： $cat file1 file2 > file
  - 参数：
    - -n 或 --number 由 1 开始对所有输出的行数编号
    - -b 或 --number-nonblank 和 -n 相似，只不过对于空白行不编号
    - -s 或 --squeeze-blank 当遇到有连续两行以上的空白行，就代换为一行的空白行
    - -v 或 --show-nonprinting
  - 例：

    + 把 textfile1 的档案内容加上行号后输入 textfile2 这个档案里

       cat -n textfile1 > textfile2

    + 把 textfile1 和 textfile2 的档案内容加上行号（空白行不加）之后将内容附加到 textfile3 里。

       cat -b textfile1 textfile2 >> textfile3

    + 把[**test**](http://www.cnblogs.com/perfy/admin/).txt文件扔进垃圾箱，赋空值test.txt

       cat /dev/null > /etc/test.txt  

+ echo
  + echo ".gitignore" >> .gitignore 
    + 追加某一行到某个文件

## File Merge

+ https://www.cnblogs.com/bldly1989/p/7093163.html

## File Append

+ https://blog.csdn.net/czg13548930186/article/details/81179853

## Find and grep

- find命令是根据文件的属性进行查找，如文件名，文件大小，所有者，所属组，是否为空，访问时间，修改时间等

  - ### find (在文件系统中查找文件)

    - 基本格式：find  path expression
    - 按照文件名查找
      - find / -name httpd.conf　　#在根目录下查找文件httpd.conf，表示在整个硬盘查找
      - find /etc -name httpd.conf　　#在/etc目录下文件httpd.conf
      - find /etc -name 'srm'　　#使用通配符(0或者任意多个)。表示在/etc目录下查找文件名中含有字符串‘srm’的文件
      - find . -name 'srm' 　　#表示当前目录下查找文件名开头是字符串‘srm’的文件
    - 按照文件特征查找 　　　　
      - find / -amin -10 　　# 查找在系统中最后10分钟访问的文件(access time)
      - find / -atime -2　　 # 查找在系统中最后48小时访问的文件
      - find / -empty 　　# 查找在系统中为空的文件或者文件夹
      - find / -group cat 　　# 查找在系统中属于 group为cat的文件
      - find / -mmin -5 　　# 查找在系统中最后5分钟里修改过的文件(modify time)
      - find / -mtime -1 　　#查找在系统中最后24小时里修改过的文件
      - find / -user fred 　　#查找在系统中属于fred这个用户的文件
      - find / -size +10000c　　#查找出大于10000000字节的文件(c:字节，w:双字，k:KB，M:MB，G:GB)
      - find / -size -1000k 　　#查找出小于1000KB的文件
    - 使用混合查找方式查找文件
      - 参数有： ！，-and(-a)，-or(-o)。
      - find /tmp -size +10000c -and -mtime +2 　　#在/tmp目录下查找大于10000字节并在最后2分钟内修改的文件
      - find / -user fred -or -user george 　　#在/目录下查找用户是fred或者george的文件文件
      - find /tmp ! -user panda　　#在/tmp目录中查找所有不属于panda用户的文件

- grep 是根据文件的内容进行查找，会对文件的每一行按照给定的模式(patter)进行匹配查找

  - Grep 文本中查找

    - 基本格式：find  expression
    - 主要参数：
      + －c：只输出匹配行的计数
      + －i：不区分大小写
      + －h：查询多文件时不显示文件名
      + －l：查询多文件时只输出包含匹配字符的文件名
      + －n：显示匹配行及行号
      + －s：不显示不存在或无匹配文本的错误信息
      + －v：显示不包含匹配文本的所有行。
    - pattern正则表达式主要参数：
      + \： 忽略正则表达式中特殊字符的原有含义
      + ^：匹配正则表达式的开始行
      + $: 匹配正则表达式的结束行
      + <：从匹配正则表达 式的行开始
      + ：到匹配正则表达式的行结束
      + [ ]：单个字符，如[A]即A符合要求
      + [ - ]：范围，如[A-Z]，即A、B、C一直到Z都符合要求
      + .：所有的单个字符。
    - 实例　 
      - grep 'test' d*　　#显示所有以d开头的文件中包含 test的行
      - grep ‘test’ aa bb cc 　　 #显示在aa，bb，cc文件中包含test的行
      - grep ‘[a-z]{5}’ aa 　　#显示所有包含每行字符串至少有5个连续小写字符的字符串的行
      - grep magic /usr/src　　#显示/usr/src目录下的文件(不含子目录)包含magic的行
      - grep -r magic /usr/src　　#显示/usr/src目录下的文件(包含子目录)包含magic的行
      - grep -w pattern files ：只匹配整个单词，而不是字符串的一部分(如匹配’magic’，而不是’magical’)

    +  grep -rn “hello word”
      + 查找当前所在目录下，所有包含“hello world”的所有文件

## Linux Background Running

+ 重定向
  + python train.py > log.txt 2 > &1 
    + 将错误输出 也 重定向到 标准输出
    + 2 表示错误输出
    + 1 表示标准输出 

+ &
  + 当前程序在后台运行，终端推出后，此程序终止

+ nohup
  + 使用&命令后，作业被提交到后台运行，当前控制台没有被占用，但是一但把当前控制台关掉(退出帐户时)，作业就会停止运行
  + nohup命令可以在你退出帐户之后继续运行相应的进程。nohup就是不挂起的意思( no hang up)

## GPU Operation

+ 使用率查看，GPU-Util
  $ nvidia-smi
  实时查看
  $ watch [options]  command
  最常用的参数是 -n， 后面指定是每多少秒来执行一次命令。
  监视显存：我们设置为每 10s 显示一次显存的情况：
  $ watch -n 10 nvidia-smi

  

## Network Operation

- 网络流量
  网络流量实时监控
  nload 

+ tcp连接状态查询
  netstat -an
  netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

## Disk Operation

+ 磁盘查看
  硬盘：df -h --total（du -sh xxxx/，du -sh ）
  du -h -d 1：最深路径为1以内的所有目录大小
  du -sh ：-s, --summarize display only a total for each argument

## Text Operation

+ 删除文本的前三行 sed -i '3d' test.csv 

+ 文本合成
  + A quick tip to concatenate many small disparate `.txt` files into one large training file: `ls *.txt | xargs -L 1 cat >> input.txt`.