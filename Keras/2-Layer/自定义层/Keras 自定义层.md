# Keras 自定义层
## Reference
+ [1] http://www.cnblogs.com/bymo/p/7552839.html

## 自定义层中没有要学习的参数
+ 对于简单的定制操作，可以通过使用layers.core.Lambda层来完成。该方法的适用情况：仅对流经该层的数据做个变换，而这个变换本身没有需要学习的参数

```
# 切片后再分别进行embedding和average pooling
import numpy as np  
from keras.models import Sequential  
from keras.layers import Dense, Activation,Reshape  
from keras.layers import merge  
from keras.utils import plot_model
from keras.layers import *
from keras.models import Model  

def get_slice(x, index):
    return x[:, index]

keep_num = 3 
field_lens = 90
input_field = Input(shape=(keep_num, field_lens))
avg_pools = []
for n in range(keep_num):
    block = Lambda(get_slice,output_shape=(1,field_lens),arguments={'index':n})(input_field)
    x_emb = Embedding(input_dim=100, output_dim=200, input_length=field_lens)(block)
    x_avg = GlobalAveragePooling1D()(x_emb)
    avg_pools.append(x_avg)  
output = concatenate([p for p in avg_pools])
model = Model(input_field, output) 
plot_model(model, to_file='model/lambda.png',show_shapes=True)  

plt.figure(figsize=(21, 12))
im = plt.imread('model/lambda.png')
plt.imshow(im)
```
+ 这里用Lambda定义了一个对张量进行切片操作的层
![](https://images2017.cnblogs.com/blog/1182656/201709/1182656-20170919171906915-1979874933.png)

## 对于具有可训练权重的定制层，需要自己来实现
```
from keras import backend as K
from keras.engine.topology import Layer
import numpy as np

class MyLayer(Layer):

    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(MyLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        # Create a trainable weight variable for this layer.
        self.kernel = self.add_weight(name='kernel', 
                                      shape=(input_shape[1], self.output_dim),
                                      initializer='uniform',
                                      trainable=True)
        super(MyLayer, self).build(input_shape)  # Be sure to call this somewhere!

    def call(self, x):
        return K.dot(x, self.kernel)

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.output_dim)
```