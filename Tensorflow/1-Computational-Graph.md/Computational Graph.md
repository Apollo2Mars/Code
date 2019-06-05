# Computational Graph
## Reference
+ LHY Deep Learning Y2017 3
+ Deep Learning Chapter 6.5
## Define
+ A language describing a function
	+ Node : variable(scalar, vector, tensor)
	+ Edge : operation(some function)
	+ Example : (Review Chain Rule)
		+ $y = f(g(h(x)))$
		+ $e = (a+b)*(b+1)$

+ Jacobian Matrix
	+ $x_1, x_2, x_3$
	+ $y_1, y_2$
	+ 求导之后得到的矩阵

+  Computational Graph for Recurrent Network
	+  $C = C_1 + C_2 + C_3$
	+  很多次连乘会造成许多问题，故引入引入LSTM等其他方法