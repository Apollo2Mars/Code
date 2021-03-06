# 数组
### 找到数组中的最小值和最大值
+ 取单元素：分别找最大和最小 2N
+ 取双元素(0.5N),双元素区别大小(1)，大与Max比(1)，小与min比(1) （0.5N * (1 + 1 + 1)）
+ 取双元素（0.5N),将小的放在左边，大的放在右边（0.5 或 1， 需要改变数组结构），大者组取最大(0.5),小者组取最小（0.5） 1.5N 或 2N
+ 分治： 数组分成两半,分别取两半的最小值和最大值（最终结果在左半最小值，右半最小值，左半最大值，右半最大值 间 产生）
### 找到数组中第二大的值
+ 快速排序 O(nlogn) + 找第二个 O(n)
+ 双变量 ： 分别存储最大数和次大数
### （××）最大子数组之和
+ 暴力
+ 重复利用已经计算的子数组和
+ 动态规划
+ 优化的动态规划
### 数组中两两相加等于20的组合数量
+ 排序法
        + 快速排序 O(nlogn)
        + 双下标
                + arr[end] + arr[begin] < 20
                        + begin ++
                + arr[end] + arr[begin] > 20
                        + end --
### 把数组循环右移k位
+ 12345 右移 2 位
+ 123 和 45 的顺序不变
+ 每个部分反转 ： 321 54
+ 整体反转 ： 45 123
### 第K个最小的数
+ 排序法
        + 快排 + 查找
                + 时间复杂度 O(nlogn) 空间复杂度 O(logn)
+ 剪枝法
        + 选一个数tmp做参考值，比它小的放左边，比它大的放右边
        + 检查 tmp 的 位置 是否是 k-1
                + 如果是 返回 tmp
                + 如果tmp小于 k-1, 则检索tmp 的右半部分
                + 如果tmp大于 k-1, 则检索左半部分
### 数组中只出现一次的数
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
### 找出数组中唯一的重复元素
+ 问题：数组 a[N], 1～N-1 ， 其中某个数字重复了一次
+ 要求：每个数组只能访问一次
        + 求和
                + sum(a) - sum(1~N-1)
+ 要求： 不能使用辅助空间
        + 异或法
        + 位图法
### 用递归的方法求整数数组的最大元素
	+ WTF
### 求数对之差的最大值
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
### 求绝对值最小的数
+ 排序
+ 二分查找
### 求数组中两个元素(a,b)的最小距离
+ 遍历数组
+ 遇到n1,求n1_index,求n1_index 与 最近一次 n2_index 的间距
+ 遇到n2,求n2_index,求n2_index 与 最近一次 n1_index 的间距
+ 求所有间距中的最小间距
### 找出数组在数组中第一次出现的位置
+ 跳跃搜索
### 两个有序子序列进行合并
+ 要求：空间O(1)
+ a[0, mid-1] 和 a[mid, num-1] 各自升序
+ 遍历 0～mid-1 , 如果 a[tmp] > a[mid], 则交换两个位置的数
+ 交换后的a[mid]在 a[mid, num-1]间进行插入排序
### 两个有序整型数据的交集
+ 双指针 二路归并
+ 特殊情况：
        + 两个数组长度相差悬殊：
                + 便利短数组，在长数组中二分查找
### 一个数组是否连续相邻
+ 最大值减最小值与数组长度比较
### 数组中反序对的个数
+ 归并排序 外加计数器
### 最小三元组的距离
+ 最小数所在的数组向后移动一个位置