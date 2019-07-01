CRF Tools 

- Neural CRF Parsing
  - 
- CRF++
  - Parameters
    - -t  产生文本格式的模型
  - Pos template
        # Unigram
        U00:%x[-3,0]
        U01:%x[-2,0]
        U02:%x[-1,0]
        U03:%x[0,0]
        U04:%x[1,0] // 下一个字对当前标签的影响
        U05:%x[2,0]
        U06:%x[3,0] // 下数第三个字对当前标签的影响
        U07:%x[-1,0]/%x[0,0] // 上一个字和当前字对当前标签的影响
        U08:%x[0,0]/%x[1,0]
        # Bigram
        B
  - References 
    - http://lovecontry.iteye.com/blog/1251227
    - CRF Paper
      - http://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf
    - FlexCRFs
      - http://flexcrfs.sourceforge.net/flexcrfs.pdf
  - Todo
    - Support semi-Markov CRF
    - Support piece-wise CRF
    - Provide useful C++/C API (Currently no APIs are available)
  - Reference
    - J. Lafferty, A. McCallum, and F. Pereira. Conditional random fields: Probabilistic models for segmenting and labeling sequence data, In Proc. of ICML, pp.282-289, 2001
    - F. Sha and F. Pereira. Shallow parsing with conditional random fields, In Proc. of HLT/NAACL 2003
    - NP chunking
    - CoNLL 2000 shared task: Chunking
---


## crf++里的特征模板得怎么理解
+ Reference : 链接：https://www.zhihu.com/question/20279019/answer/273594958
+ Unigram和Bigram模板分别生成CRF的状态特征函数$s_l(y_i,x,i)$和转移特征函数$t_k(y_{i-1},y_i,x,i)$ 
+ 其中$y_i$标签，x是观测序列，i是当前节点位置。
+ 训练的目的是获取每个特征模板的权值

+ crf++模板定义里的%x[row,col]，即是特征函数的参数 
+ 举个例子,假设有如下用于分词标注的训练文件：
  ```
  北    N    B
  京    N    E
  欢    V    B
  迎    V    M
  你    N    E
  ```
  - 其中第3列是标签，也是测试文件中需要预测的结果，有BME3种状态
  - 第二列是词性，不是必须的
  - 特征模板格式：%x[row,col],x可取U或B，对应两种类型
  - 方括号里的编号用于标定特征来源，row表示相对当前位置的行，0即是当前行；col对应训练文件中的列。这里只使用第1列（编号0），即文字
  
- Unigram类型
    - 每一行模板生成一组状态特征函数，数量是L\*N个，L是标签状态数，N是模板展开后的特征数，也就是训练文件中行数， 这里L\*N = 3\*5=15
    - 例如：U01:%x[0,0]，生成如下15个函数：
    ```
    func1 = if (output = B and feature=U01:"北") return 1 else return 0
    func2 = if (output = M and feature=U01:"北") return 1 else return 0
    func3 = if (output = E and feature=U01:"北") return 1 else return 0
    func4 = if (output = B and feature=U01:"京") return 1 else return 0
    ...
    func13 = if (output = B and feature=U01:"你") return 1 else return 0
    func14 = if (output = M and feature=U01:"你") return 1 else return 0
    func15 = if (output = E and feature=U01:"你") return 1 else return 0
    ```
  - 这些函数经过训练后，其权值表示函数内文字对应该标签的概率（形象说法，概率和可大于1）。
  - 又如 U02:%x[-1,0]，训练后，该组函数权值反映了句子中上一个字对当前字的标签的影响

- Bigram类型
  - 与Unigram不同的是，Bigram类型模板生成的函数会多一个参数：上个节点的标签$y_{i-1}$
  - 生成函数类似于：
    ```
    func1 = if (prev_output = B and output = B and feature=B01:"北") return 1 else return 0
    ```
  - 这样，每行模板则会生成 L\*L\*N 个特征函数
  - 经过训练后，这些函数的权值反映了上一个节点的标签对当前节点的影响
  - 每行模版可使用多个位置。例如：U18:%x[1,1]/%x[2,1]
  - 字母U后面的01，02是唯一ID，并不限于数字编号
  - 如果不关心上下文，甚至可以不要这个ID