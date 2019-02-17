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