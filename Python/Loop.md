## Loop
+ if
    ```
    if expression :
       suite
    elif expression :
       suite
    else :
       suite
    ```
+ while
	+ demo
	```
        while 判断条件：
    	执行语句……
        ```
	+ while else
        ```
        count = 0
        while count < 5:
        print (count, " 小于 5")
        count = count + 1
        else:
        print (count, " 大于或等于 5")
        ```
+ for
	+ range()
        ```
        for i in range(5):
                print(i)
        0
        1
        2
        3
        4
        ```

+ break
    + break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
+ couninue
	+ continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
+ pass
	+ 占位

+ 由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
