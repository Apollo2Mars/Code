

GPU使用率
使用率查看，GPU-Util
$ nvidia-smi
实时查看
$ watch [options]  command
最常用的参数是 -n， 后面指定是每多少秒来执行一次命令。
监视显存：我们设置为每 10s 显示一次显存的情况：
$ watch -n 10 nvidia-smi
网络流量
网络流量实时监控
nload 
磁盘查看
硬盘：df -h --total（du -sh xxxx/，du -sh ）
du -h -d 1：最深路径为1以内的所有目录大小
du -sh ：-s, --summarize display only a total for each argument

tcp连接状态查询
netstat -an
netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

+ 删除文本的前三行
sed -i '3d' test.csv 

+ 文本合成
	+ A quick tip to concatenate many small disparate `.txt` files into one large training file: `ls *.txt | xargs -L 1 cat >> input.txt`.