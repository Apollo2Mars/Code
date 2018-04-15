## Data Structure and Algorithm implemented by Java

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
// double pointer
// pointer p : return pointer
// pointer q : traverse the linkedlist; find the repeated node and delete it 
// tips : p, q operate one linkedlist
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
		// 第一次的时候 pPrev 是 null
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
+ 判断有环链表的起始节点
	+ 判断节点有环后，使用（快慢指针相交的节点）确定环的长度N，从原有头节点开始遍历，如果当前Node 与 Node + N 第一次相等，则此节点为环的起始节点
+ 不知道头指针的情况下，删除指定节点
+ 判断两个链表是否相交
	+ 链表相交的含义（？？？）
		+ 求两个链表的长度差，长的链表的头指针先移动这个长度差，之后判断移动后的长链表与短链表是否相同
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

## 查找
七大查找方法 ：http://www.cnblogs.com/leezx/p/5719012.html
+ 顺序查找
+ 分块查找
+ 差值查找
+ 菲波那切查找
+ 树表查找
+ 哈希查找
+ 二分查找
```
public class BinarySearch { 
        /** 
        * 二分查找算法 
        * 
        * @param srcArray 有序数组 
        * @param key 查找元素 
        * @return key的数组下标，没找到返回-1 
        */  
        public static void main(String[] args) { 
            int srcArray[] = {3,5,11,17,21,23,28,30,32,50,64,78,81,95,101};   
            System.out.println(binSearch(srcArray, 0, srcArray.length - 1, 81));  
        } 

        // 二分查找递归实现   
        public static int binSearch(int srcArray[], int start, int end, int key) {   
            int mid = (end - start) / 2 + start;   
            if (srcArray[mid] == key) {   
                return mid;   
            }   
            if (start >= end) {   
                return -1;   
            } else if (key > srcArray[mid]) {   
                return binSearch(srcArray, mid + 1, end, key);   
            } else if (key < srcArray[mid]) {   
                return binSearch(srcArray, start, mid - 1, key);   
            }   
            return -1;   
        } 

        // 二分查找普通循环实现   
        public static int binSearch(int srcArray[], int key) {   
            int mid = srcArray.length / 2;   
            if (key == srcArray[mid]) {   
                return mid;   
            }   

            int start = 0;   
            int end = srcArray.length - 1;   
            while (start <= end) {   
                mid = (end - start) / 2 + start;   
                if (key < srcArray[mid]) {   
                   end = mid - 1;   
                } else if (key > srcArray[mid]) {   
                    start = mid + 1;   
                } else {   
                    return mid;   
                }   
            }   
            return -1;   
        } 
}
```

## 排序
+ 堆排序
	+ http://www.cnblogs.com/CherishFX/p/4643940.html
	+ 堆排序是一种树形选择排序方法，它的特点是：在排序的过程中，将array[0，...，n-1]看成是一颗完全二叉树的顺序存储结构，利用完全二叉树中双亲节点和孩子结点之间的内在关系，在当前无序区中选择关键字最大（最小）的元素。

+ 归并排序
	+ 归并排序（Merge）是将两个（或两个以上）有序表合并成一个新的有序表，即把待排序序列分为若干个子序列，每个子序列是有序的。然后再把有序子序列合并为整体有序序列
	+ 工作原理：
		+ 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
		+ 设定两个指针，最初位置分别为两个已经排序序列的起始位置
		+ 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
		+ 重复步骤3直到某一指针达到序列尾
		+ 将另一序列剩下的所有元素直接复制到合并序列尾
```
public class MergeSortTest {

	public static void main(String[] args) {
		int[] data = new int[] { 5, 3, 6, 2, 1, 9, 4, 8, 7 };
		print(data);
		mergeSort(data);
		System.out.println("排序后的数组：");
		print(data);
	}

	public static void mergeSort(int[] data) {
		sort(data, 0, data.length - 1);
	}

	public static void sort(int[] data, int left, int right) {
		if (left >= right)
			return;
		// 找出中间索引
		int center = (left + right) / 2;
		// 对左边数组进行递归
		sort(data, left, center);
		// 对右边数组进行递归
		sort(data, center + 1, right);
		// 合并
		merge(data, left, center, right);
		print(data);
	}

	/**
	 * 将两个数组进行归并，归并前面2个数组已有序，归并后依然有序
	 * 
	 * @param data
	 *            数组对象
	 * @param left
	 *            左数组的第一个元素的索引
	 * @param center
	 *            左数组的最后一个元素的索引，center+1是右数组第一个元素的索引
	 * @param right
	 *            右数组最后一个元素的索引
	 */
	public static void merge(int[] data, int left, int center, int right) {
		// 临时数组
		int[] tmpArr = new int[data.length];
		// 右数组第一个元素索引
		int mid = center + 1;
		// third 记录临时数组的索引
		int third = left;
		// 缓存左数组第一个元素的索引
		int tmp = left;
		while (left <= center && mid <= right) {
			// 从两个数组中取出最小的放入临时数组
			if (data[left] <= data[mid]) {
				tmpArr[third++] = data[left++];
			} else {
				tmpArr[third++] = data[mid++];
			}
		}
		// 剩余部分依次放入临时数组（实际上两个while只会执行其中一个）
		while (mid <= right) {
			tmpArr[third++] = data[mid++];
		}
		while (left <= center) {
			tmpArr[third++] = data[left++];
		}
		// 将临时数组中的内容拷贝回原数组中
		// （原left-right范围的内容被复制回原数组）
		while (tmp <= right) {
			data[tmp] = tmpArr[tmp++];
		}
	}
}
```
+ 快速排序
```
public static void sort(int array[], int low, int high){
	int i,j;
	int key;
	if(low >= high){
		return;
	}
	i = low;
	j = high;
	//
	key = arrar[i];
	while(i<j){
		while(i<j && array[j] >= index){
			j--;
		}
	    	if(i < j){
			array[i++] = array[j];
	    	}
	    	while(i<j && array[i] < index){
			i++;
	    	}
	    	if(i<j){
			array[j--] == array[i];
	    	}
	}
	array[i] = key;
	sort(array, low, i-1);
	sort(array, i+1, high);
}
```

## 位运算

## 数组
+ 找到数组中的最小值和最大值
	+ 取单元素：分别找最大和最小 2N
	+ 取双元素(0.5N),双元素区别大小(1)，大与Max比(1)，小与min比(1) （0.5N * (1 + 1 + 1)）
	+ 取双元素（0.5N),将小的放在左边，大的放在右边（0.5 或 1， 需要改变数组结构），大者组取最大(0.5),小者组取最小（0.5） 1.5N 或 2N
	+ 分治： 数组分成两半,分别取两半的最小值和最大值（最终结果在左半最小值，右半最小值，左半最大值，右半最大值 间 产生）
+ 找到数组中第二大的值
	+ 快速排序 O(nlogn) + 找第二个 O(n)
	+ 双变量 ： 分别存储最大数和次大数
+ （××）最大子数组之和
	+ 暴力
	+ 重复利用已经计算的子数组和
	+ 动态规划
	+ 优化的动态规划
+ 数组中两两相加等于20的组合数量
	+ 排序法
		+ 快速排序 O(nlogn)
		+ 双下标
			+ arr[end] + arr[begin] < 20
				+ begin ++
			+ arr[end] + arr[begin] > 20
				+ end --
+ 把数组循环右移k位
	+ 12345 右移 2 位
	+ 123 和 45 的顺序不变
	+ 每个部分反转 ： 321 54
	+ 整体反转 ： 45 123
+ 第K个最小的数
	+ 排序法
		+ 快排 + 查找
			+ 时间复杂度 O(nlogn) 空间复杂度 O(logn)
	+ 剪枝法
		+ 选一个数tmp做参考值，比它小的放左边，比它大的放右边
		+ 检查 tmp 的 位置 是否是 k-1
			+ 如果是 返回 tmp
			+ 如果tmp小于 k-1, 则检索tmp 的右半部分
			+ 如果tmp大于 k-1, 则检索左半部分
+ 数组中只出现一次的数
	+ 问题：一个整型数组除了1个数字出现一次之外，其他数字都出现了2k次
	+ 排序法
		+ 快排后，当前数与下一个数比较
		+ 时间 O(nlogn)
	+ 异或法
		+ 时间复杂度 O(n), 空间复杂度 O(1)
		+ 异或思想 ： 转为 二进制， 相同为零，不同为一
		```
		public static int findNotDouble(int []){
		    	int result = a[0];
		    	for (int i=0; i < a.length; i++){
				result ^=a[i];
		    	}
		}
        	```
	+ 问题：一个整型数组除了1个数字出现一次之外，其他数字都出现了2k+1次
		+ 数组中所有数字对应的二进制数各个位置上1的个数对2k+1求余数，就可以得到所求数的二进制表示
	+ 问题：一个整型数组除了2个数字出现一次之外，其他数字都出现了2k次
		+ 例子
		```
		23, 23, 19, 19, 1, 88, 88, 3, 3, 2, 56, 56
		x = 23^23^19^19^1^88^88^3^3^2^56^56 = 1^2
		例如：这里x = 3 = 00000011B，从这里看出，a1和a2在1~2比特位上是不一样的。我们随便选取其中一位，比如右起第一位为区分位，这样所有数字可以分为两组：
		比特位末位为0：88, 88, 2, 56, 56
			比特位末位为1：23, 23, 19, 19, 1, 3, 3

		这样分完后，我们发现，a1和a2分到不同的组里了。将其中任意一组所有数字进行异或，便可以得出其中一个不重复的数字：
			a1 = 88^88^2^56^56 = 2
			a2 = a1^x = a1^a1^a2 = 1
			这样，我们只需要遍历两遍数组，就可以找出这两个数。
        	```
+ 找出数组中唯一的重复元素
	+ 问题：数组 a[N], 1～N-1 ， 其中某个数字重复了一次
	+ 要求：每个数组只能访问一次
		+ 求和
			+ sum(a) - sum(1~N-1)
	+ 要求： 不能使用辅助空间
		+ 异或法
		+ 位图法
+ 用递归的方法求整数数组的最大元素
	+ WTF
+ 求数对之差的最大值
	+ 问题描述：数组中一个数字减去右边子数组的一个数字可以得到一个差值，求所有可能插值中的最大值
	+ 二分法
		+ 最大差值的减数与被减数都在左侧
		+ 最大差值的减数与被减数都在右侧
		+ 最大差值的减数与被减数分别在两侧
		+ max(leftMax,rightMax,mixMax)
		+ 代码
		```
        to be continued
        ```
	+ 动态规划
		+ O(n), O(n)
		+ 额外申请两个数组
			+ diff[i] : 以第i个数为减数，所有数对之差的最大值
			+ max[i] : 前i个数字的最大值
		+ 已知diff[i],则diff[i+1] 有两种可能：
			+ 等于diff[i]
			+ 等于MAX[i]-a[i+1]
		+ diff[i+1] = max(diff[i], MAX[i+1]-a[i+1]), MAX[i+1]=max(MAX[i],a[i+1])
+ 求绝对值最小的数
	+ 排序
	+ 二分查找
+ 求数组中两个元素的最小距离
	+ 遍历数组
	+ 遇到n1,求n1_index,求n1_index 与 最近一次 n2_index 的间距
	+ 遇到n2,求n2_index,求n2_index 与 最近一次 n1_index 的间距
	+ 求所有间距中欧你的最小间距
+ 找出数组在数组中第一次出现的位置
	+ 跳跃搜索
+ 两个有序子序列进行合并
	+ 要求：空间O(1)
	+ a[0, mid-1] 和 a[mid, num-1] 各自升序
	+ 遍历 0～mid-1 , 如果 a[tmp] > a[mid], 则交换两个位置的数
	+ 交换后的a[mid]在 a[mid, num-1]间进行插入排序
+ 两个有序整型数据的交集
	+ 双指针 二路归并
	+ 特殊情况：
		+ 两个数组长度相差悬殊：
			+ 便利短数组，在长数组中二分查找
+ 一个数组是否连续相邻
	+ 最大值减最小值与数组长度比较
+ 数组中反序对的个数
	+ 归并排序 外加计数器
+ 最小三元组的距离
	+ 最小数所在的数组向后移动一个位置

## 字符串
+ 字符串反转
	+ 反转整句后反转单词
+ 两个字符串是否由相同的字符组成
	+ 空间换时间
+ 删除字符串中相同重复的字符
	+ 空间换时间
+ 打印数组的排列情况
+ 输出字符串中所有的组合
+ 最长公共字串
+ 最长回文子串

## 二叉树
+ 基本概念
	+ 满二叉树
		+ 所有节点都有左右节点，并且所有子节点都在同一层上
	+ 完全二叉树
		+ 满二叉树的最底层的节点都在树的左侧
	+ 二叉排序树
		+ 如果左节点不空，左节点的值小于根节点
		+ 如果右节点不空，右节点的值大于根节点
	+ 平衡二叉树
		+ 它是一 棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树，同时，平衡二叉树必定是二叉搜索树，反之则不一定
	+ AVL树是带有平衡条件的二叉查找树
		+ AVL树是带有平衡条件的二叉查找树,一般是用平衡因子差值判断是否平衡并通过旋转来实现平衡,左右子树树高不超过1,和红黑树相比,它是严格的平衡二叉树,平衡条件必须满足(所有节点的左右子树高度差不超过1).不管我们是执行插入还是删除操作,只要不满足上面的条件,就要通过旋转来保持平衡,而旋转是非常耗时的,由此我们可以知道AVL树适合用于插入删除次数比较少，但查找多的情况。
		![](https://img-blog.csdn.net/20160717080221088)
	+ 红黑树
		+ 红黑树并不追求“完全平衡”——它只要求部分地达到平衡要求，降低了对旋转的要求，从而提高了性能
		+ 红黑树是一种自平衡二叉查找树，是在计算机科学中用到的一种数据结构，典型的用途是实现关联数组。它是在1972年由Rudolf Bayer发明的，他称之为"对称二叉B树"，它现代的名字是在 Leo J. Guibas 和 Robert Sedgewick 于1978年写的一篇论文中获得的。它是复杂的，但它的操作有着良好的最坏情况运行时间，并且在实践中是高效的: 它可以在O(log n)时间内做查找，插入和删除，这里的n是树中元素的数目。
		+ 红黑树的应用比较广泛，主要是用它来存储有序的数据，它的时间复杂度是O(lgn)，效率非常之高。
		+ 例如，Java集合中的TreeSet和TreeMap
		![](https://img-blog.csdn.net/20160717102628283)

+ 二叉树排序
+ 各种遍历
+ 已知先序和中序，如何求后序
+ 节点的最大距离
+ 公共父节点

## 海量数据的问题
+ Hash法
+ Bit-map 法
+ Bloom Filter 法
+ 外排序
	+ 文件太大，内存无法处理
+ Trie树（字典树或键树）
+ 堆
	+ 堆是一种树形数据结构
+ 双层桶法
+ MapReduce 法

+ TopK问题
+ 重复问题
+ 排序问题
