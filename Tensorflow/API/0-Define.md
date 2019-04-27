# Tensorflow 
## Reference
+ 常用函数
	+ https://blog.csdn.net/wuqingshan2010/article/details/71056292

## 常用函数
+ TensorFlow 将图形定义转换成分布式执行的操作, 以充分利用可用的计算资源(如 CPU 或 GPU。一般你不需要显式指定使用 CPU 还是 GPU, TensorFlow 能自动检测。
+ 如果检测到 GPU, TensorFlow 会尽可能地利用找到的第一个 GPU 来执行操作.
+ 并行计算能让代价大的算法计算加速执行，TensorFlow也在实现上对复杂操作进行了有效的改进。大部分核相关的操作都是设备相关的实现，比如GPU
+ 下面是一些重要的操作/核：
	+ Maths
		+ Add, Sub, Mul, Div, Exp, Log, Greater, Less, Equal
	+ Array	
		+ Concat, Slice, Split, Constant, Rank, Shape, Shuffle
	+ Matrix
		+ MatMul, MatrixInverse, MatrixDeterminant
	+ Neuronal Network	
		+ SoftMax, Sigmoid, ReLU, Convolution2D, MaxPool
	+ Checkpointing	
		+ Save, Restore
	+ Queues and syncronizations
		+ Enqueue, Dequeue, MutexAcquire, MutexRelease
	+ Flow control	
		+ Merge, Switch, Enter, Leave, NextIteration
