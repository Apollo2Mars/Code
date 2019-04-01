'''This is a reproduction of the IRNN experiment
with pixel-by-pixel sequential MNIST in
"A Simple Way to Initialize Recurrent Networks of Rectified Linear Units"
by Quoc V. Le, Navdeep Jaitly, Geoffrey E. Hinton
arxiv:1504.00941v2 [cs.NE] 7 Apr 2015
http://arxiv.org/pdf/1504.00941v2.pdf
Optimizer is replaced with RMSprop which yields more stable and steady
improvement.
Reaches 0.93 train/test accuracy after 900 epochs
(which roughly corresponds to 1687500 steps in the original paper.)
'''

import keras

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import SimpleRNN
from keras import initializers

from keras.layers import LSTM
from keras.layers import LSTMCell
from keras.layers import StackedRNNCells
from keras.layers import ConvLSTM2D
from keras.layers import CuDNNLSTM

from keras.layers import GRU
from keras.layers import GRUCell
from keras.layers import CuDNNGRU

# import keras.initializations as ins
from keras.optimizers import RMSprop

from keras.utils import np_utils


batch_size = 1024
num_classes = 10
epochs = 20
hidden_units = 100

learning_rate = 1e-6
clip_norm = 1.0

# a = 7/3  2.33333
# b = 7%3  1
# c = 7//3  2

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = reshape  (60000,28,28) to (60000,784,1)
x_train = x_train.reshape(x_train.shape[0], -1, 1)
x_test = x_test.reshape(x_test.shape[0], -1, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
# 把y变为one-hot 的形式
# 例如 3 = ·[0,0,0,1,0,0,0,0,0,0]
y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)

print('Evaluate IRNN...')
model = Sequential()
# SimpleRNN : 全连接RNN网络，RNN的输出会被回馈到输入
# kernel_initializer：权值初始化方法，为预定义初始化方法名的字符串，或用于初始化权重的初始化器
# recurrent_initializer：循环核的初始化方法，为预定义初始化方法名的字符串，或用于初始化权重的初始化器
# RandomNormal ： 正态分布初始化
# Identity : 使用单位矩阵初始化，仅适用于2D方阵;gain：单位矩阵的乘性系数

# kernel_initializer ： 初始 w 的初始值
# recurrent_initializer : 循环 w 权值 的 初始值
# IRNN test score: 1.75098527851
# IRNN test accuracy: 0.3791
model.add(SimpleRNN(hidden_units,
                    kernel_initializer=initializers. RandomNormal(stddev=0.001),
                    recurrent_initializer=initializers.Identity(gain=1.0),
                    activation='relu',
                    input_shape=x_train.shape[1:]))

model.add(Dense(num_classes))
model.add(Activation('softmax'))
rmsprop = RMSprop(lr=learning_rate)
model.compile(loss='categorical_crossentropy',
              optimizer=rmsprop,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

scores = model.evaluate(x_test, y_test, verbose=0)
print('IRNN test score:', scores[0])
print('IRNN test accuracy:', scores[1])