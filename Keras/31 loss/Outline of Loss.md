# Loss Function

## Reference
+ https://keras-cn.readthedocs.io/en/latest/other/objectives/

## Details
+ mean_squared_error或mse
+ mean_absolute_error或mae
+ mean_absolute_percentage_error或mape
+ mean_squared_logarithmic_error或msle
+ squared_hinge
+ hinge
+ categorical_hinge
+ binary_crossentropy（亦称作对数损失，logloss）
+ logcosh
+ categorical_crossentropy：亦称作多类的对数损失，注意使用该目标函数时，需要将标签转化为形如(nb_samples, nb_classes)的二值序列
+ sparse_categorical_crossentrop：如上，但接受稀疏标签。注意，使用该函数时仍然需要你的标签与输出值的维度相同，你可能需要在标签数据上增加一个维度：np.expand_dims(y,-1)
+ kullback_leibler_divergence:从预测值概率分布Q到真值概率分布P的信息增益,用以度量两个分布的差异.
+ poisson：即(predictions - targets * log(predictions))的均值
+ cosine_proximity：即预测值与真实标签的余弦距离平均值的相反数

+ 注意: 当使用"categorical_crossentropy"作为目标函数时,标签应该为多类模式,即one-hot编码的向量,而不是单个数值. 可以使用工具中的to_categorical函数完成该转换.示例如下:

```
from keras.utils.np_utils import to_categorical
categorical_labels = to_categorical(int_labels, num_classes=None)
```