# Linux System

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
    