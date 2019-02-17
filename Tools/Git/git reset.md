+ git reset
	+ http://www.cnblogs.com/craftor/archive/2012/11/04/2754140.html
	+ git reset –mixed 默认方式，不带任何参数的git reset,只保留源码，回退commit和index 信息。
	+ git reset –soft 回退到某个版本，只回退了commit，不会恢复index file一级，如果需要提交直接commit就好。
	+ git reset –hard 回退到某个版本，文件全部回退到当前版本，不可恢复。慎用！！！
+ 版本恢复
	+ git Log log命令可以显示所有**提交过的**版本信息
	+ 如果觉得信息显示太繁琐  可以加上参数  --pretty=oneline[只会留下commit  id (版本号 (用SHA1字串表示))和 提交版本时的描述信息] 显示效果如下:
	```
	8e27eb62309a1e7aa2b6c348f6dfa595bcb09898 append GPL  
	dae675a9170a2d60855a6d9f56268f42d9114f40 add distributed  
	c412f7ee690fc80906670c38a762e815abd5e1be wrote a readme file  
	```
	+ git reset --hard commitid  //本地代码回到指定的commitid
	+ git push -f origin branchname//git服务器代码回到指定的commitid
	+ git reflog命令可以对git误操作进行数据恢复。
	如不小心用git commit --amend当成git commit覆盖当前的commit，或不小心把当前的commit给搞没了（reset --hard）。 都可以通过git reflog恢复。
	Git记录每次修改HEAD的操作，git reflog/git log -g可以查看所有的历史操作记录，然后通过git reset命令进行恢复。
	+ example
	```
	apollo@Mars:~/craft/projects/QA-Craft$ git reflog 
	ab284bb HEAD@{0}: reset: moving to HEAD^
	2cdfce4 HEAD@{1}: reset: moving to 2cdfce4
	564d350 HEAD@{2}: reset: moving to 564d350
	8149c69 HEAD@{3}: reset: moving to 8149c69
	7339ef0 HEAD@{4}: reset: moving to 7339ef0
	da52f90 HEAD@{5}: reset: moving to da52f90
	ad62b1a HEAD@{6}: reset: moving to ad62b1a
	c3a7e85 HEAD@{7}: reset: moving to c3a7e85
	317c4c8 HEAD@{8}: reset: moving to 317c4c8f57cbdd9f0e56f6fb52b6f945162f11c1
	c3a7e85 HEAD@{9}: commit (amend): complete data preprocess
	ad62b1a HEAD@{10}: commit: complete data preprocess
	317c4c8 HEAD@{11}: reset: moving to 317c4c8f57cbdd9f0e56f6fb52b6f945162f11c1
	ab284bb HEAD@{12}: reset: moving to ab284bbf13526ebebaa4e6ac9af3df8046bcb651
	da52f90 HEAD@{13}: commit: complete data preprocess
	7ae4bca HEAD@{14}: reset: moving to 7ae4bca2a9f157aa1154026a01fcdbfb122d018d
	8ff5db7 HEAD@{15}: commit (amend): update corpus
	987073a HEAD@{16}: commit (amend): update corpus
	8b43b26 HEAD@{17}: commit (amend): update corpus
	0e142ce HEAD@{18}: commit (amend): update corpus
	7339ef0 HEAD@{19}: commit: update corpus
	8149c69 HEAD@{20}: commit (amend): update for data preprocess
	6587c3a HEAD@{21}: commit (amend): update for data preprocess
	e635bb1 HEAD@{22}: commit (amend): update for data preprocess
	5d40164 HEAD@{23}: commit: update for data preprocess
	564d350 HEAD@{24}: commit: complete preprocess data for reader
	7ae4bca HEAD@{25}: commit: update data/glove
	7dba404 HEAD@{26}: commit: prepare reader
	2cdfce4 HEAD@{27}: commit: complete SQuAD data preprocess
	ab284bb HEAD@{28}: commit: update
	c8d3fdc HEAD@{29}: pull: Fast-forward
	78411cc HEAD@{30}: pull: Fast-forward
	bde2501 HEAD@{31}: commit: add SQuAD and update its README.md
	317c4c8 HEAD@{32}: commit (initial): first commit
	
	apollo@Mars:~/craft/projects/QA-Craft$ git reset --hard ad62b1a
	HEAD is now at ad62b1a complete data preprocess
	apollo@Mars:~/craft/projects/QA-Craft$ 
	apollo@Mars:~/craft/projects/QA-Craft$ git status
	On branch master
	Your branch and 'origin/master' have diverged,
	and have 1 and 6 different commits each, respectively.
	  (use "git pull" to merge the remote branch into yours)
	nothing to commit, working directory clean
	apollo@Mars:~/craft/projects/QA-Craft$ ll
	total 36
	drwxrwxr-x 7 apollo apollo 4096 3月   9 14:52 ./
	drwxrwxr-x 9 apollo apollo 4096 3月   9 14:22 ../
	drwxrwxr-x 3 apollo apollo 4096 3月   9 14:52 craft/
	drwxrwxr-x 4 apollo apollo 4096 3月   9 14:52 drqa/
	drwxrwxr-x 8 apollo apollo 4096 3月   9 14:52 .git/
	-rwxrwxr-x 1 apollo apollo   16 3月   9 14:52 .gitignore*
	drwxrwxr-x 2 apollo apollo 4096 3月   8 18:46 .idea/
	-rw-rw-r-- 1 apollo apollo  740 3月   9 14:52 README.md
	drwxrwxr-x 3 apollo apollo 4096 3月   9 14:52 script/

	```