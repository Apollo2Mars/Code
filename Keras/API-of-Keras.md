
### API Documents
- https://keras.io/getting-started/sequential-model-guide/

+ Models
	+ Sequential
	+ Model(Functional API)
+ Layers
	+ core Layers
	+ Convolutional Layers
		+ https://keras-cn.readthedocs.io/en/latest/layers/convolutional_layer/
	+ Pooling Layers
    + Locally-connected Layers
    + Recurrent Layers
    + Embedding Layers
    	```
        # model.add(Embedding(len(vacab)+1, 200, weights=[embedding_matrix]))
        # input_dim : 字典长度
        # output_dim : 全链接嵌入的维度
        # input_length : 当输入序列的长度固定时，该值为其长度
        #                如果要在该层后接Flatten层，然后接Dense层，则必须指定该参数，否则Dense层的输出维度无法自动推断。
        # 输入shape
        # 形如（samples，sequence_length）的2D张量
        # 输出shape
        # 形如(samples, sequence_length, output_dim)的3D张量
        #
    	```
    + Merge Layers
    + Advanced Activations Layers
    +  Normalization Layers
    +  Noise Layers
    +  Layer Wappers
    +  Writing your own Keras Layers
+ Preprocessing
	 + Sequence
	 + Text
     + Image
+ Losses
+ Metrics
+ Optimizers
+ Activations
+ Callbacks
+ Datasets
+ Applications
+ Backend
+ Initializers
	+ Initialize method
		+ https://keras-cn.readthedocs.io/en/latest/other/initializations/
	+ 初始化方法定义了对Keras层设置初始化权重的方法,不同的层可能使用不同的关键字来传递初始化方法，一般来说指定初始化方法的关键字是kernel_initializer 和 bias_initializer
	```
    model.add(Dense(64,
