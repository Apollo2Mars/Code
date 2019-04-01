# Permute
## Function
+ Permute层将输入的维度按照给定模式进行重排，例如，当需要将RNN和CNN网络连接时，可能会用到该层。

## Parameters
+ dims：整数tuple，指定重排的模式，不包含样本数的维度。重拍模式的下标从1开始。例如（2，1）代表将输入的第二个维度重拍到输出的第一个维度，而将输入的第一个维度重排到第二个维度

## Demo
```
model = Sequential()
model.add(Permute((2, 1), input_shape=(10, 64)))
# now: model.output_shape == (None, 64, 10)
# note: `None` is the batch dimension
```

## 输入shape
任意，当使用激活层作为第一层时，要指定input_shape

## 输出shape
与输入相同，但是其维度按照指定的模式重新排列