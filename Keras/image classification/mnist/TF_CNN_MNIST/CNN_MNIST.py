# coding=utf-8
#
#  http://www.tensorfly.cn/tfdoc/tutorials/mnist_pros.html
#  tensorflow API
#

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)     #download and load mnist data
x = tf.placeholder(tf.float32, [None, 784])                        #input data placeholder
y_actual = tf.placeholder(tf.float32, shape=[None, 10])            #input label placeholder


# function : initial all W
def weight_variable(shape):
    #
    # shape表示生成张量的维度，mean是均值，stddev是标准差。这个函数产生正太分布，均值和标准差自己设定。
    # 这是一个截断的产生正太分布的函数，就是说产生正太分布的值如果与均值的差值大于两倍的标准差，那就重新生成。
    # 和一般的正太分布的产生随机数据比起来，这个函数产生的随机数与均值的差距不会超过两倍的标准差，但是一般的别的函数是可能的。
    #
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


# function : initial all b
def bias_variable(shape):

    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# function : build convolutional network
def conv2d(x, W):
    #
    # 第一个参数input：指需要做卷积的输入图像，它要求是一个Tensor，具有[batch, in_height, in_width, in_channels]这样的shape，
    #   具体含义是[训练时一个batch的图片数量, 图片高度, 图片宽度, 图像通道数]，注意这是一个4维的Tensor，要求类型为float32和float64其中之一
    # 第二个参数filter：相当于CNN中的卷积核，它要求是一个Tensor，具有[filter_height, filter_width, in_channels, out_channels]这样的shape，
    #   具体含义是[卷积核的高度，卷积核的宽度，图像通道数，卷积核个数]，要求类型与参数input相同，有一个地方需要注意，第三维in_channels，就是参数input的第四维
    # 第三个参数strides：卷积时在图像每一维的步长，这是一个一维的向量，长度4
    # 第四个参数padding：string类型的量，只能是"SAME","VALID"其中之一，这个值决定了不同的卷积方式（后面会介绍）
    # 第五个参数：use_cudnn_on_gpu:bool类型，是否使用cudnn加速，默认为true
    #
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# function : build pooling layer
def max_pool(x):
    #
    # value 表示输入数据形式。
    # ksize 表示池化的大小，是一个4个元素的列表，跟输入数据的格式对应，即[batch,in_height,in_wide, in_channels]，目前一般batch和channels对应的都为1
    # strides 表示在特征图上移动，是一个4个元素的列表，跟输入数据的格式对应，即[batch,in_height,in_wide, in_channels]，目前一般batch和channels对应的都为1
    # data_format 表示输入数据的格式，需要跟输入数据的格式保持一致。有”NHWC“和”NCHW“两种。默认是”NHWC“即[batch, in_height,in_wide,in_channels]
    # padding 表示是否填充，有两个格式  ”SAME“得到的输出特征图跟输入特征图相同  ”VALID“得到的输出特征图跟输入特征图不相同
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# build network
#
# z.reshape(-1)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])

# z.reshape(-1, 1) z变成只有一列，行数不知道多少
#z.reshape(-1,1)
# array([[ 1],
#        [ 2],
#       [ 3],
#        [ 4],
#        [ 5],
#        [ 6],
#        [ 7],
#        [ 8],
#        [ 9],
#        [10],
#        [11],
#        [12],
#        [13],
#        [14],
#        [15],
#        [16]])
#

#
#   现在我们可以开始实现第一层了。它由一个卷积接一个max pooling完成。
#   卷积在每个5x5的patch中算出32个特征。卷积的权重张量形状是[5, 5, 1, 32]，前两个维度是patch的大小，接着是输入的通道数目，最后是输出的通道数目。
#   而对于每一个输出通道都有一个对应的偏置量。
#

#   为了用这一层，我们把x变成一个4d向量，其第2、第3维对应图片的宽、高，最后一维代表图片的颜色通道数(因为是灰度图所以这里的通道数为1，如果是rgb彩色图，则为3)。
x_image = tf.reshape(x, [-1,28,28,1])         # convert input data shape, so that use in network
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)     #first convolutional layer
h_pool1 = max_pool(h_conv1)                                  #first pooling layer

#   为了构建一个更深的网络，我们会把几个类似的层堆叠起来。第二层中，每个5x5的patch会得到64个特征。
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)      #second convolution layer
h_pool2 = max_pool(h_conv2)                                   #second pooling layer

#   现在，图片尺寸减小到7x7，我们加入一个有1024个神经元的全连接层，用于处理整个图片。我们把池化层输出的张量reshape成一些向量，乘上权重矩阵，加上偏置，然后对其使用ReLU。
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])              #reshape to vector
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)    #first fully connection layer

keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)                  #dropout layer

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_predict=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)   #softmax layer

cross_entropy = -tf.reduce_sum(y_actual*tf.log(y_predict))     #cross-entropy
train_step = tf.train.GradientDescentOptimizer(1e-3).minimize(cross_entropy)    #gradient descent method
correct_prediction = tf.equal(tf.argmax(y_predict,1), tf.argmax(y_actual,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))                 #calculate accuracy



sess=tf.InteractiveSession()
sess.run(tf.initialize_all_variables())

count = 0
for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i%100 == 0: # train 100 times , test 1 time
        train_acc = accuracy.eval(feed_dict={x:batch[0], y_actual: batch[1], keep_prob: 1.0})
        print ('step %d, training accuracy %g'%(i,train_acc))
        print ('x' + str(batch[0]))
        print ('y' + str(batch[1]))
    train_step.run(feed_dict={x: batch[0], y_actual: batch[1], keep_prob: 0.5})

test_acc = accuracy.eval(feed_dict={x: mnist.test.images, y_actual: mnist.test.labels, keep_prob: 1.0})
print ("test accuracy %g"%test_acc)