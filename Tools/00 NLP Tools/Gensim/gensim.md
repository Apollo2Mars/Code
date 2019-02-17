# Gensim
## Reference 
1. https://radimrehurek.com/gensim/intro.html
2. http://www.cnblogs.com/iloveai/p/gensim_tutorial.html

## Introduction[1]
+ Gensim is a free Python library designed to automatically extract **semantic topics** from documents, as efficiently (computer-wise) and painlessly (human-wise) as possible
+ Doc2Vec
	- class gensim.models.doc2vec.Doc2Vec(documents=None, dm_mean=None, dm=1, dbow_words=0, dm_concat=0, dm_tag_count=1, docvecs=None, docvecs_mapfile=None, comment=None, trim_rule=None, callbacks=(), **kwargs)¶
	- Bases: gensim.models.base_any2vec.BaseWordEmbeddingsModel
	- Class for training, using and evaluating neural networks described in http://arxiv.org/pdf/1405.4053v2.pdf
	- Initialize the model from an iterable of documents. Each document is a TaggedDocument object that will be used for training.

Parameters:
	- documents (iterable of iterables) – The documents iterable can be simply a list of TaggedDocument elements, but for larger corpora, consider an iterable that streams the documents directly from disk/network. If you don’t supply documents, the model is left uninitialized – use if you plan to initialize it in some other way.
	- dm (int {1,0}) – Defines the training algorithm. If dm=1, ‘distributed memory’ (PV-DM) is used. Otherwise, distributed bag of words (PV-DBOW) is employed.
	- size (int) – Dimensionality of the feature vectors.
	- window (int) – The maximum distance between the current and predicted word within a sentence.
	- alpha (float) – The initial learning rate.
	- min_alpha (float) – Learning rate will linearly drop to min_alpha as training progresses.
	- seed (int) – Seed for the random number generator. Initial vectors for each word are seeded with a hash of the concatenation of word + str(seed). Note that for a fully deterministically-reproducible run, you must also limit the model to a single worker thread (workers=1), to eliminate ordering jitter from OS thread scheduling. (In Python 3, reproducibility between interpreter launches also requires use of the PYTHONHASHSEED environment variable to control hash randomization).
	- min_count (int) – Ignores all words with total frequency lower than this.
	- max_vocab_size (int) – Limits the RAM during vocabulary building; if there are more unique words than this, then prune the infrequent ones. Every 10 million word types need about 1GB of RAM. Set to None for no limit.
	- sample (float) – The threshold for configuring which higher-frequency words are randomly downsampled, useful range is (0, 1e-5).
	- workers (int) – Use these many worker threads to train the model (=faster training with multicore machines).
	- iter (int) – Number of iterations (epochs) over the corpus.
	- hs (int {1,0}) – If 1, hierarchical softmax will be used for model training. If set to 0, and negative is non-zero, negative sampling will be used.
	- negative (int) – If > 0, negative sampling will be used, the int for negative specifies how many “noise words” should be drawn (usually between 5-20). If set to 0, no negative sampling is used.
	- dm_mean (int {1,0}) – If 0 , use the sum of the context word vectors. If 1, use the mean. Only applies when dm is used in non-concatenative mode.
	- dm_concat (int {1,0}) – If 1, use concatenation of context vectors rather than sum/average; Note concatenation results in a much-larger model, as the input is no longer the size of one (sampled or arithmetically combined) word vector, but the size of the tag(s) and all words in the context strung together.
	- dm_tag_count (int) – Expected constant number of document tags per document, when using dm_concat mode; default is 1.
	- dbow_words (int {1,0}) – If set to 1 trains word-vectors (in skip-gram fashion) simultaneous with DBOW doc-vector training; If 0, only trains doc-vectors (faster).
	- trim_rule (function) – Vocabulary trimming rule, specifies whether certain words should remain in the vocabulary, be trimmed away, or handled using the default (discard if word count < min_count). Can be None (min_count will be used, look to keep_vocab_item()), or a callable that accepts parameters (word, count, min_count) and returns either gensim.utils.RULE_DISCARD, gensim.utils.RULE_KEEP or gensim.utils.RULE_DEFAULT. Note: The rule, if given, is only used to prune vocabulary during build_vocab() and is not stored as part of the model.
	- callbacks – List of callbacks that need to be executed/run at specific stages during training.
+ Word2Vec
	- class gensim.models.word2vec.Word2Vec(sentences=None, size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None, sample=0.001, seed=1, workers=3, min_alpha=0.0001, sg=0, hs=0, negative=5, cbow_mean=1, hashfxn=<built-in function hash>, iter=5, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=10000, compute_loss=False, callbacks=())¶
	- Bases: gensim.models.base_any2vec.BaseWordEmbeddingsModel

    -Class for training, using and evaluating neural networks described in https://code.google.com/p/word2vec/

    - If you’re finished training a model (=no more updates, only querying) then switch to the gensim.models.KeyedVectors instance in wv

    - The model can be stored/loaded via its save() and load() methods, or stored/loaded in a format compatible with the original word2vec implementation via wv.save_word2vec_format() and Word2VecKeyedVectors.load_word2vec_format().

    - Initialize the model from an iterable of sentences. Each sentence is a list of words (unicode strings) that will be used for training.

    - Parameters:	
        - sentences (iterable of iterables) – The sentences iterable can be simply a list of lists of tokens, but for larger corpora, consider an iterable that streams the sentences directly from disk/network. See BrownCorpus, Text8Corpus or LineSentence in word2vec module for such examples. If you don’t supply sentences, the model is left uninitialized – use if you plan to initialize it in some other way.
        - sg (int {1, 0}) – Defines the training algorithm. If 1, skip-gram is employed; otherwise, CBOW is used.
        - size (int) – Dimensionality of the feature vectors.
        - window (int) – The maximum distance between the current and predicted word within a sentence.
        - alpha (float) – The initial learning rate.
        - min_alpha (float) – Learning rate will linearly drop to min_alpha as training progresses.
        - seed (int) – Seed for the random number generator. Initial vectors for each word are seeded with a hash of the concatenation of word + str(seed). Note that for a fully deterministically-reproducible run, you must also limit the model to a single worker thread (workers=1), to eliminate ordering jitter from OS thread scheduling. (In Python 3, reproducibility between interpreter launches also requires use of the PYTHONHASHSEED environment variable to control hash randomization).
        - min_count (int) – Ignores all words with total frequency lower than this.
        - max_vocab_size (int) – Limits the RAM during vocabulary building; if there are more unique words than this, then prune the infrequent ones. Every 10 million word types need about 1GB of RAM. Set to None for no limit.
        - sample (float) – The threshold for configuring which higher-frequency words are randomly downsampled, useful range is (0, 1e-5).
        - workers (int) – Use these many worker threads to train the model (=faster training with multicore machines).
        - hs (int {1,0}) – If 1, hierarchical softmax will be used for model training. If set to 0, and negative is non-zero, negative sampling will be used.
        - negative (int) – If > 0, negative sampling will be used, the int for negative specifies how many “noise words” should be drawn (usually between 5-20). If set to 0, no negative sampling is used.
        - cbow_mean (int {1,0}) – If 0, use the sum of the context word vectors. If 1, use the mean, only applies when cbow is used.
        - hashfxn (function) – Hash function to use to randomly initialize weights, for increased training reproducibility.
        - iter (int) – Number of iterations (epochs) over the corpus.
        - trim_rule (function) – Vocabulary trimming rule, specifies whether certain words should remain in the vocabulary, be trimmed away, or handled using the default (discard if word count < min_count). Can be None (min_count will be used, look to keep_vocab_item()), or a callable that accepts parameters (word, count, min_count) and returns either gensim.utils.RULE_DISCARD, gensim.utils.RULE_KEEP or gensim.utils.RULE_DEFAULT. Note: The rule, if given, is only used to prune vocabulary during build_vocab() and is not stored as part of the model.
        - sorted_vocab (int {1,0}) – If 1, sort the vocabulary by descending frequency before assigning word indexes.
        - batch_words (int) – Target size (in words) for batches of examples passed to worker threads (and thus cython routines).(Larger batches will be passed if individual texts are longer than 10000 words, but the standard cython code truncates to that maximum.)
        - compute_loss (bool) – If True, computes and stores loss value which can be retrieved using model.get_latest_training_loss().
        - callbacks – List of callbacks that need to be executed/run at specific stages during training.

## What is Gensim?[2]
+ Gensim是一款开源的第三方Python工具包，用于从原始的非结构化的文本中，无监督地学习到文本隐层的主题向量表达。它支持包括TF-IDF，LSA，LDA，和word2vec在内的多种主题模型算法，支持流式训练，并提供了诸如相似度计算，信息检索等一些常用任务的API接口。

+ 基本概念
	+ 语料（Corpus）：一组原始文本的集合，用于无监督地训练文本主题的隐层结构。语料中不需要人工标注的附加信息。在Gensim中，Corpus通常是一个可迭代的对象（比如列表）。每一次迭代返回一个可用于表达文本对象的稀疏向量。
	+ 向量（Vector）：由一组文本特征构成的列表。是一段文本在Gensim中的内部表达。
	+ 稀疏向量（Sparse Vector）：通常，我们可以略去向量中多余的0元素。此时，向量中的每一个元素是一个(key, value)的tuple。
	+ 模型（Model）：是一个抽象的术语。定义了两个向量空间的变换（即从文本的一种向量表达变换为另一种向量表达）。

+ Step 1. 训练语料的预处理
	+ 训练语料的预处理指的是将文档中原始的字符文本转换成Gensim模型所能理解的稀疏向量的过程。
	+ 通常，我们要处理的原生语料是一堆文档的集合，每一篇文档又是一些原生字符的集合。在交给Gensim的模型训练之前，我们需要将这些原生字符解析成Gensim能处理的稀疏向量的格式。
	+ 由于语言和应用的多样性，Gensim没有对预处理的接口做出任何强制性的限定。通常，我们需要先对原始的文本进行分词、去除停用词等操作，得到每一篇文档的特征列表。例如，在词袋模型中，文档的特征就是其包含的word：
    
        ```
        texts = [['human', 'interface', 'computer'],
         ['survey', 'user', 'computer', 'system', 'response', 'time'],
         ['eps', 'user', 'interface', 'system'],
         ['system', 'human', 'system', 'eps'],
         ['user', 'response', 'time'],
         ['trees'],
         ['graph', 'trees'],
         ['graph', 'minors', 'trees'],
         ['graph', 'minors', 'survey']]
        ```
	
    + 其中，corpus的每一个元素对应一篇文档。接下来，我们可以调用Gensim提供的API建立语料特征（此处即是word）的索引字典，并将文本特征的原始表达转化成词袋模型对应的稀疏向量的表达。依然以词袋模型为例：
	
        ```
        from gensim import corpora
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        print corpus[0] # [(0, 1), (1, 1), (2, 1)]
        ```
	
    + 到这里，训练语料的预处理工作就完成了。我们得到了语料中每一篇文档对应的稀疏向量（这里是bow向量）；向量的每一个元素代表了一个word在这篇文档中出现的次数。值得注意的是，虽然词袋模型是很多主题模型的基本假设，这里介绍的doc2bow函数并不是将文本转化成稀疏向量的唯一途径。在下一小节里我们将介绍更多的向量变换函数。最后，出于内存优化的考虑，Gensim支持文档的流式处理。我们需要做的，只是将上面的列表封装成一个Python迭代器；每一次迭代都返回一个稀疏向量即可
    
	```
    class MyCorpus(object):
        def __iter__(self):
            for line in open('mycorpus.txt'):
                # assume there's one document per line, tokens separated by whitespace
                yield dictionary.doc2bow(line.lower().split())
	```

+ Step 2. 主题向量的变换
	+ 对文本向量的变换是Gensim的核心。通过挖掘语料中隐藏的语义结构特征，我们最终可以变换出一个简洁高效的文本向量。
	+ 在Gensim中，每一个向量变换的操作都对应着一个主题模型，例如上一小节提到的对应着词袋模型的doc2bow变换。每一个模型又都是一个标准的Python对象。下面以TF-IDF模型为例，介绍Gensim模型的一般使用方法。
	+ 首先是模型对象的初始化。通常，Gensim模型都接受一段训练语料（注意在Gensim中，语料对应着一个稀疏向量的迭代器）作为初始化的参数。显然，越复杂的模型需要配置的参数越多。
     
	```
	from gensim import models
	tfidf = models.TfidfModel(corpus)
    ```
	+ 其中，corpus是一个返回bow向量的迭代器。这两行代码将完成对corpus中出现的每一个特征的IDF值的统计工作。
	+ 接下来，我们可以调用这个模型将任意一段语料（依然是bow向量的迭代器）转化成TFIDF向量（的迭代器）。需要注意的是，这里的bow向量必须与训练语料的bow向量共享同一个特征字典（即共享同一个向量空间）。
	```
	doc_bow = [(0, 1), (1, 1)]
	print tfidf[doc_bow] # [(0, 0.70710678), (1, 0.70710678)]
	```
	+ 注意，同样是出于内存的考虑，model[corpus]方法返回的是一个迭代器。如果要多次访问model[corpus]的返回结果，可以先讲结果向量序列化到磁盘上。
	+ 我们也可以将训练好的模型持久化到磁盘上，以便下一次使用：
	```
	tfidf.save("./model.tfidf")
	tfidf = models.TfidfModel.load("./model.tfidf")
    ```
	+ Gensim内置了多种主题模型的向量变换，包括LDA，LSI，RP，HDP等。这些模型通常以bow向量或tfidf向量的语料为输入，生成相应的主题向量。所有的模型都支持流式计算。关于Gensim模型更多的介绍，可以参考这里：API Reference

+ Step 3. 文档相似度的计算
	+ 在得到每一篇文档对应的主题向量后，我们就可以计算文档之间的相似度，进而完成如文本聚类、信息检索之类的任务。在Gensim中，也提供了这一类任务的API接口。
	+ 以信息检索为例。对于一篇待检索的query，我们的目标是从文本集合中检索出主题相似度最高的文档。
	+ 首先，我们需要将待检索的query和文本放在同一个向量空间里进行表达（以LSI向量空间为例）：
	```
    # 构造LSI模型并将待检索的query和文本转化为LSI主题向量
    # 转换之前的corpus和query均是BOW向量
    lsi_model = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    documents = lsi_model[corpus]
    query_vec = lsi_model[query]_
    ```
	+ 接下来，我们用待检索的文档向量初始化一个相似度计算的对象：
	```
    index = similarities.MatrixSimilarity(documents)
    ```
    + 我们也可以通过save()和load()方法持久化这个相似度矩阵：
	```
	index.save('/tmp/deerwester.index')
	index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')
	```
	+ 注意，如果待检索的目标文档过多，使用similarities.MatrixSimilarity类往往会带来内存不够用的问题。此时，可以改用similarities.Similarity类。二者的接口基本保持一致。
	+ 最后，我们借助index对象计算任意一段query和所有文档的（余弦）相似度：
	```
    sims = index[query_vec] # return: an iterator of tuple (idx, sim)
    ```