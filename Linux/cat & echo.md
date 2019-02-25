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

---

+ echo
	+ echo ".gitignore" >> .gitignore 
		+ 追加某一行到某个文件
