### commit 之后， 撤销commit
+ https://www.cnblogs.com/lfxiao/p/9378763.html
+ git reset --soft HEAD^
+ 仅仅撤销commit，代码依然保留

+ HEAD^ 上一个版本， 同HEAD～1
+ 回退两个版本的 commit 使用 HEAD～2

### git reset 的几个参数
+ --mixed 
	+ 不删除改动的代码，撤销commit 和 add 
	+ 默认参数
+ --soft
	+ 不删除改动的代码，撤销commit， 不撤销 add
+ --hard
	+ 删除工作空间改动的代码， 撤销commit ，撤销 git add .

