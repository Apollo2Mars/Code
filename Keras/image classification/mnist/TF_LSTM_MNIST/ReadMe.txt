LSTM_MNIST.py

https://m.aliyun.com/yunqi/articles/202939?tk=nwzLFAxyonH%2BvDsFcz9mKUntp%2B0KR9212pFWMTksy7w%3D


# initialize variables
init = tf.global_variables_initializer()
# 这里要注意的一个关键点，我们的图像基本上是被平坦化为一个单一的维度矢量784。函数next_batch(batch_size)必然返回batch_size为784维度向量的批次，因此它们被重塑为[batch_size,time_steps,n_input]可以被占位符接受。
with tf.Session() as sess:
    sess.run(init)
    iter = 1
    while iter < 800:
        batch_x, batch_y = mnist.train.next_batch(batch_size=batch_size)
        batch_x = batch_x.reshape((batch_size, time_steps, n_input))
        sess.run(opt, feed_dict={x: batch_x, y: batch_y})
        if iter % 10 == 0:
            acc = sess.run(accuracy,feed_dict={x: batch_x, y: batch_y})
            los = sess.run(loss,feed_dict={x: batch_x, y: batch_y})
            print("For iter ", iter)
            print("Accuracy ", acc)
            print("Loss ", los)
            print("__________________")
        iter=iter + 1

=======================================================================================================
P:AttributeError: 'module' object has no attribute 'static_rnn'
  AttributeError: 'module' object has no attribute 'rnn_cell'
S: For people using the newer version of tensorflow, add this to the code:

from tensorflow.contrib import rnn
lstm_cell = rnn.BasicLSTMCell(rnn_size)
outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)

instead of

from tensorflow.python.ops import rnn, rnn_cell
lstm_cell = rnn_cell.BasicLSTMCell(rnn_size,state_is_tuple=True)
outputs, states = rnn.rnn(lstm_cell, x, dtype=tf.float32)﻿