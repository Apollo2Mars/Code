# File -i/I

+ 显示文件编码格式



# enca 

+ mac
  + 检测
  + 转码
+ https://blog.csdn.net/jinguangliu/article/details/83414806



# iconv

+ iconv -f GBK file1.txt -t UTF-8 -o file2.txt
iconv [选项...] [文件...]

有如下选项可用:

输入/输出格式规范：
-f, --from-code=名称 原始文本编码
-t, --to-code=名称 输出编码

信息：
-l, --list 列举所有已知的字符集

输出控制：
-c 从输出中忽略无效的字符
-o, --output=FILE 输出文件
-s, --silent 关闭警告
--verbose 打印进度信息

iconv -f utf-8 -t gb2312 /server_test/reports/software_.txt > /server_test/reports/software_asserts.txt

 一般加 -c
