## Java Data Structure and Algorithm

## 链表
```
class Node{
	Node next = null;
    int data;
    public Node(int data){this.data = data;}
}
```
+ 链表的增加删除
	```
    public class MyLinkedList{
    	Node head = null;
        /*add a data to LinkedList*/
        public void addNode(int d){
        	Node newNode = new Node(d);
            if ( head == null){
            	head = newNode;
            }
            Node tmp = head;
            while(tmp.next != null){
            	tmp = tmp.next;
            }
            //add to the end
            tmp.next = newNode;
        }
        /* delete the index th node*/
        public Boolean deleteNode(int index){
        	if( index < 1 || index > length()){
            	return false;
            }
            //delete the first node
            if (index == 1){
            	head = head.next;
                return true;
            }
            int i = 1;
            Node preNode = head;
            Node curNode = preNode.next;
            while(curNode != null){
            	if(i == index){
                	preNode.next = curNode.next;
                    return true;
                }
                preNode = curNode;
                curNode = curNode.next;
                i++;
            }
        }
        /* return the length of LinkedList*/
        public int length(){
        	Node tmp = head;
            int len = 0;
        	while(tmp != null){
            	len++;
                tmp = tmp.next;
            }
            return len;
        }
        /* sort and return the LinkedList*/
        public Node orderList(){
        	Node nextNode = null;
            Node curNode = head;
            int tmp = 0;
            while(curNode != null){
            	nextNode = curNode.next;
                while(nextNode != null){
                	if(curNode.data > nextNode.data){
                    	tmp = curNode.data;
                        curNode.data = nextNode.data;
                        nextNode.data = tmp;
                    }
                    nextNode = nextNode.next;
                }
                curNode = curNode.next;
            }
            return head;
        }
    }
    ```
+ 链表删除重复元素
	```
    public void deleteDuplecate(Node head){
    	Node p = head;
        while(p != null){
        	Node q = p;
            while(q.next != null){
            	if(p.data == q.next.data){
                	q.next = q.next.next;
                }else{
                	q = q.next;
                }
            }
            p = p.next
        }
    }
    ```
+ 找出单链表的倒数第K个元素
	```
    //正向可查找第 length-k：问题是需要遍历两次列表
    public findElem(Node head, int k){
    	if(k < 1 || k > length()){
        	return null
        }
        Node p1 = head;
        Node p2 = head;
        for (int iCount = 0; i < k ; i++){
        	p1 = p1.next
        }
        while(p1.next != null){
        	p1 = p1.next;
            p2 = p2.next;
        }
        return p2;
    }
    ```
+ 实现链表的反转
	```
    public Node reverseLinkedList(Node head){
    	Node pReverHead = Head;
        Node pNode = head;
        Node pPrev = null;
        while(pNode != null){
        	Node pNext = pNode.next;
            if(pNext == null){
            	pReverHead = pNode;
            }
            pNode.next = pPrev;
            pPrev = pNode;
            pNode = pNext;
        }
        this.head = pReverHead;
    }
    ```
+ 从尾到头输出单链表
	```
    public void printReverse(Node head){
    	if(head.next != null){
        	printReverse(head.next);
        	System.out.println(head.next.data);
        }
    }
    ```
+ 寻找单链表的中间节点
	+ 设置两个指针，快指针一次跳两步，慢指针一次跳一步
	+ 快指针到尾部时，慢指针为中间节点（奇数个为慢指针指向的那个，偶数时为慢指针指向的那个及下一个）
+ 检测链表是否有环
	+ 设置两个指针，快指针一次跳两步，慢指针一次跳一步
	+ 快指针每次运动后都和慢指针比较，如果快指针等于慢指针，则证明链表是带环的单链表，否则证明这个链表是不带环的循环链表
+ 不知道头指针的情况下，删除制定节点
+ 判断两个链表是否相交
	+ 链表相交的含义（？？？）
	+ 判断是否有相同的尾节点

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

## 排序

## 位运算

## 数组

## 字符串

## 二叉树

## 海量数据的问题
+ 文件太大，内存无法处理