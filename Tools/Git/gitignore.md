+ gitignore
	+ 共享式忽略新建 .gitignore 文件，放在工程目录任意位置即可。.gitignore 文件可以忽略自己。忽略的文件，只针对未跟踪文件有效，对已加入版本库的文件无效。
	+ 独享式忽略针对具体版本库 ：.git/info/exclude针对本地全局：  git config --global core.excludefile ~/.gitignore
	+ 规则
	```
	在项目工程中，常会生成一些运行缓存，而这些是不能 push 的，所以需要 .gitignore 配置规则来过滤。
	配置规则：
	以 # 开头行为注释  
	以斜杠“/”开头表示目录；
	/target/ 过滤根目录的 target 文件夹
	target/ 过滤任何目录包含的 target 文件夹
	以星号“*”通配多个字符；
	*.zip 过滤所有.zip文件
	以问号“?”通配单个字符；
	以方括号“[]”包含单个字符的匹配列表；
	以叹号“!”表示不忽略(跟踪)匹配到的文件或目录；
	/doc/
	!/doc/common.doc
	
	忽略的语法规则：
    	(#)表示注释
    	(*)  表示任意多个字符; 
    	(?) 代表一个字符;
     	([abc]) 代表可选字符范围
    	如果名称最前面是路径分隔符 (/) ，表示忽略的该文件在此目录下。
    	如果名称的最后面是 (/) ，表示忽略整个目录，但同名文件不忽略。
    	通过在名称前面加 (!) ，代表不忽略。
    	例子如下：
    	# 这行是注释
    	*.a                   # 忽略所有 .a 伟扩展名的文件
    	!lib.a                # 但是 lib.a 不忽略，即时之前设置了忽略所有的 .a
    	/TODO            # 只忽略此目录下 TODO 文件，子目录的 TODO 不忽略 
    	build/               # 忽略所有的 build/ 目录下文件
    	doc/*.txt           # 忽略如 doc/notes.txt, 但是不忽略如 doc/server/arch.txt 
	
	```
	+ 此外，git 对于 .ignore 配置文件是按行从上到下进行规则匹配的，意味着如果前面的规则匹配的范围更大，则后面的规则将不会生效；
	+ 被过滤掉的文件就不会出现在你的GitHub库中了，当然本地中还有，只是push的时候不会上传。
	+ 如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的。那么解决方法就是先把本地缓存删除（改变成未track状态），然后再提交：
	```
	git rm -r --cached .
	git add .
	git commit -m ‘update .gitignore‘
	```
	+ 文件中的操作
		+ 经测试发现，若要忽略一个文件夹下的部分文件夹，应该一个一个的标示。可能有更好的方法。
		+ 若test下有多个文件和文件夹。若要ignore某些文件夹，应该这个配置.gitignore文件。若test下有test1，test2,test3文件。要track test3，则.gitignore文件为：
		```
		test/test1
    		test/test2
    		!test/test3
    		若为：
    		test/
    		!test/test3 ，则不能track test3。
		```