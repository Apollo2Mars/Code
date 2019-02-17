# Numpy clear up
+ # Office tutorial links
	+ links : https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

---


+ # The Basics
	NumPy’s main object is the homogeneous multidimensional array(均匀多维矩阵). It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In NumPy dimensions are called axes. The number of axes is rank.

	For example, the coordinates of a point in 3D space [1, 2, 1] is an array of rank 1, because it has one axis. That axis has a length of 3. In the example pictured below, the array has rank 2 (it is 2-dimensional). The first dimension (axis) has a length of 2, the second dimension has a length of 3.
	[[ 1., 0., 0.],
 	[ 0., 1., 2.]]

	NumPy’s array class is called ndarray. It is also known by the alias array. Note that numpy.array is not the same as the Standard Python Library class array.array, which only handles one-dimensional arrays and offers less functionality. The more important attributes of an ndarray object are:

+ ### ndarray.ndim
	the number of axes (dimensions) of the array. In the Python world, the number of dimensions is referred to as rank.
+ ### ndarray.shape
	the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, shape will be (n,m). The length of the shape tuple is therefore the rank, or number of dimensions, ndim.
+ ### ndarray.size
	the total number of elements of the array. This is equal to the product of the elements of shape.
+ ### ndarray.dtype
	an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.
+ ### ndarray.itemsize
	the size in bytes of each element of the array. For example, an array of elements of type float64 has itemsize 8 (=64/8), while one of type complex32 has itemsize 4 (=32/8). It is equivalent to ndarray.dtype.itemsize.
+ ### ndarray.data
	the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.


