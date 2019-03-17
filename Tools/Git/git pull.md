+ git pull
```
apollo@Mars:~/Documents/Tool$ git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> master

apollo@Mars:~/Documents/Tool$ git pull https://github.com/Apollo2Mars/Tool.git
From https://github.com/Apollo2Mars/Tool
 * branch            HEAD       -> FETCH_HEAD
Updating bcdd912..b2ab624
Fast-forward
 Git.md | 158 +++++++++++++++++++++++++++++++++++++++---------------------------------------------
 1 file changed, 73 insertions(+), 85 deletions(-)

```

### 拉取远程分支到本地

+ git fetch origin branchname:branchname
  + 可以把远程某各分支拉去到本地的branchname下，如果没有branchname，则会在本地新建branchname

+ git checkout origin/remoteName -b localName
  + 获取远程分支remoteName 到本地新分支localName，并跳到localName分支