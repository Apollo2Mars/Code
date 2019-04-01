## 模型参数
+ https://blog.csdn.net/lujiandong1/article/details/46386201
+ SVM模型有两个非常重要的参数C与gamma。其中 C是惩罚系数，即对误差的宽容度。c越高，说明越不能容忍出现误差,容易过拟合。C越小，容易欠拟合。C过大或过小，泛化能力变差
+ gamma是选择RBF函数作为kernel后，该函数自带的一个参数。隐含地决定了数据映射到新的特征空间后的分布，gamma越大，支持向量越少，gamma值越小，支持向量越多。支持向量的个数影响训练与预测的速度。


+ http://sklearn.apachecn.org/cn/0.19.0/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC
+ gamma : float, optional (default=’auto’)
Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’. If gamma is ‘auto’ then 1/n_features will be used instead.

Mnist keys is dict_keys(['DESCR', 'COL_NAMES', 'target', 'data'])
Start learning at 2018-05-17 14:50:52.172298
Stop learning 2018-05-17 15:18:24.317328
Elapsed learning 0:27:32.145030
Classification report for classifier SVC(C=5, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma=0.05, kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False):
             precision    recall  f1-score   support

        0.0       0.99      0.99      0.99      1024
        1.0       0.99      0.99      0.99      1185
        2.0       0.98      0.99      0.98      1051
        3.0       0.98      0.98      0.98      1057
        4.0       0.99      0.99      0.99       964
        5.0       0.98      0.98      0.98       964
        6.0       0.99      0.99      0.99      1085
        7.0       0.99      0.98      0.99      1128
        8.0       0.97      0.98      0.97      1037
        9.0       0.98      0.97      0.98      1005

avg / total       0.99      0.99      0.99     10500


Confusion matrix:
[[1014    0    2    0    0    2    2    0    1    3]
 [   0 1177    2    1    1    0    1    0    2    1]
 [   2    2 1037    2    0    0    0    2    5    1]
 [   0    0    3 1035    0    5    0    6    6    2]
 [   0    0    1    0  957    0    1    2    0    3]
 [   1    1    0    4    1  947    4    0    5    1]
 [   2    0    1    0    2    0 1076    0    4    0]
 [   1    1    8    1    1    0    0 1110    2    4]
 [   0    4    2    4    1    6    0    1 1018    1]
 [   3    1    0    7    5    2    0    4    9  974]]
Accuracy=0.9852380952380952

Process finished with exit code 0
