## 栈与队列
+ 使用数组和链表实现栈
+ 使用O(1)的时间复杂度求栈中的最小元素
+ 使用数组和链表实现队列
+ 栈模拟队列
	+ 栈 A B
		+ 入队列： 入栈A
		+ 出栈：把队列A的前n-1个元素倒到队列B，把第n个元素去掉。此时数据在B中，下次操作，则对B操作。
		+ 栈顶：把队列A的前n-1个元素倒到队列B，把第n个元素作为栈顶。
+ 队列模拟栈
	+ 队列A、B
		+ 入栈：入队列A
		+ 出栈：把队列A的前n-1个元素倒到队列B，把第n个元素去掉。此时数据在B中，下次操作，则对B操作。
		+ 栈顶：把队列A的前n-1个元素倒到队列B，把第n个元素作为栈顶。