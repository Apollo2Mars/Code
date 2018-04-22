load和loads都是实现“反序列化”，区别在于（以Python为例）：

1.loads针对内存对象，即将Python内置数据序列化为字串

如使用json.dumps序列化的对象d_json=json.dumps({'a':1, 'b':2})，在这里d_json是一个字串'{"b": 2, "a": 1}'

d=json.loads(d_json)  #{ b": 2, "a": 1}，使用load重新反序列化为dict

2.load针对文件句柄

如本地有一个json文件a.json则可以d=json.load(open('a.json'))

相应的，dump就是将内置类型序列化为json对象后写入文件

JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。它基于 ECMAScript (w3c制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。