+ git rm 
	+ git rm  bnlp-zh-hk-trainer/resources/ -rf
	+ 当我们需要删除暂存区或分支上的文件, 同时工作区也不需要这个文件了, 可以使用
	```
	git rm file_path
	git commit -m 'delete somefile'
	git push
	```
	+ 当我们需要删除暂存区或分支上的文件, 但本地又需要使用, 只是不希望这个文件被版本控制, 可以使用
	```
	git rm --cached file_path
	git commit -m 'delete remote somefile'
	git push
	```

+ 已经add 未 commit
　删除缓冲区中的文件

 git rm --cached "文件路径"，不删除物理文件，仅将该文件从缓存中删除；
 git rm --f "文件路径"，不仅将该文件从缓存中删除，还会将物理文件删除（不会回收到垃圾桶）；
 

　　如果一个文件已经add到暂存区，还没有 commit，此时如果不想要这个文件了，有两种方法：

用版本库内容清空暂存区，git reset HEAD 回退到当前版本（在Git中，用HEAD表示当前版本，上一个版本就是HEAD^，上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100）；
只把特定文件从暂存区删除，git rm --cached xxx；

+ 已经add， 已经commit
