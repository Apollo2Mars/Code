# Keras 文本预处理
## Reference
+ [1] Keras 快速入门 P74

## 步骤
+ 文字拆分
+ 建立索引
+ 序列补齐(Padding)
+ 转化为矩阵
+ 使用标注类批量处理文本文件

## 文字拆分
+ 英文
	+ text_to_word_sequence
+ 中文
	+ jieba
	+ text_to_word_sequence

## 建立索引
+ 完成分词后, 得到的单字或单词不能直接用于建模, 还需要将其转化为数字符号,才能进行后续处理
+ one_hot

## 序列补全
+ pad_sequences
	+ maxlen 补全后的长度
		+ 序列长度大于 maxlen, 会产生截断
	+ padding
		+ post : 右侧 加 0
		+ pre : 左侧 加 0
	+ value
		+ 补全值, 默认是0
		+ 可以改变

## Tokenizer 标注类
+ 较之前的方法更高效


## Demo
+ https://blog.csdn.net/lovebyz/article/details/77712003

```
import keras.preprocessing.text as T
from keras.preprocessing.text import Tokenizer
 
text1='some thing to eat'
text2='some thing to drink'
texts=[text1,text2]
 
print T.text_to_word_sequence(text1)  #以空格区分，中文也不例外 ['some', 'thing', 'to', 'eat']
print T.one_hot(text1,10)  #[7, 9, 3, 4] -- （10表示数字化向量为10以内的数字）
print T.one_hot(text2,10)  #[7, 9, 3, 1]
 
tokenizer = Tokenizer(num_words=None) #num_words:None或整数,处理的最大单词数量。少于此数的单词丢掉
tokenizer.fit_on_texts(texts)
print( tokenizer.word_counts) #[('some', 2), ('thing', 2), ('to', 2), ('eat', 1), ('drink', 1)]
print( tokenizer.word_index) #{'some': 1, 'thing': 2,'to': 3 ','eat': 4, drink': 5}
print( tokenizer.word_docs) #{'some': 2, 'thing': 2, 'to': 2, 'drink': 1,  'eat': 1}
print( tokenizer.index_docs) #{1: 2, 2: 2, 3: 2, 4: 1, 5: 1}
 
# num_words=多少会影响下面的结果，行数=num_words
print( tokenizer.texts_to_sequences(texts)) #得到词索引[[1, 2, 3, 4], [1, 2, 3, 5]]
print( tokenizer.texts_to_matrix(texts))  # 矩阵化=one_hot
[[ 0.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.],
 [ 0.,  1.,  1.,  1.,  0.,  1.,  0.,  0.,  0.,  0.]]
```

+ 标注类有两个方法将文本序列转化为待建模序列
	+ text_to_matrix
	+ sequence_to_matrix


# 序列数据的处理
+ skipgrams

# 图片数据的处理
+ Keras.preprocessing.image,ImageDataGenerator
	+ 生成一个数据生成器对象