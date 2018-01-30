ps -ef|grep weibo|awk '{print $2}'|xargs kill -9
