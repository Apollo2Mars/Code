{
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "softmax_cross_entropy_with_logits_v2\n",
        "\n",
        "# https://blog.csdn.net/tsyccnh/article/details/81069308\n",
        "\n",
        "tf.nn.softmax_cross_entropy_with_logits(记为f1) 和 \n",
        "tf.nn.sparse_softmax_cross_entropy_with_logits(记为f3),以及 \n",
        "tf.nn.softmax_cross_entropy_with_logits_v2(记为f2) \n",
        "之间的区别。\n",
        "\n",
        "f1和f3对于参数logits的要求都是一样的，即未经处理的，直接由神经网络输出的数值， 比如 [3.5,2.1,7.89,4.4]。两个函数不一样的地方在于labels格式的要求，f1的要求labels的格式和logits类似，比如[0,0,1,0]。而f3的要求labels是一个数值，这个数值记录着ground truth所在的索引。以[0,0,1,0]为例，这里真值1的索引为2。所以f3要求labels的输入为数字2(tensor)。一般可以用tf.argmax()来从[0,0,1,0]中取得真值的索引。\n",
        "\n",
        "f1和f2之间很像，实际上官方文档已经标记出f1已经是deprecated 状态，推荐使用f2。两者唯一的区别在于f1在进行反向传播的时候，只对logits进行反向传播，labels保持不变。而f2在进行反向传播的时候，同时对logits和labels都进行反向传播，如果将labels传入的tensor设置为stop_gradients，就和f1一样了。 \n",
        "那么问题来了，一般我们在进行监督学习的时候，labels都是标记好的真值，什么时候会需要改变label？f2存在的意义是什么？实际上在应用中labels并不一定都是人工手动标注的，有的时候还可能是神经网络生成的，一个实际的例子就是对抗生成网络（GAN）。"
      ],
      "outputs": [],
      "execution_count": null,
      "metadata": {}
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.8"
    },
    "nteract": {
      "version": "0.12.3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}