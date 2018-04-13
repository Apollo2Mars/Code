+ before    
    + code
    ```
      parser = argparse.ArgumentParser()
      parser.add_argument('data_dir', type=str, help='Path to SQuAD data directory', default='../data/SQuAD')
      parser.add_argument('out_dir', type=str, help='Path to output file dir', default='../data/SQuAD')
      parser.add_argument('--split', type=str, help='Filename for train/dev split',
                          default='dev-v1.1')
      parser.add_argument('--workers', type=int, default=None)
      parser.add_argument('--tokenizer', type=str, default='corenlp')
    ```
  + error
    ```
      usage: SQuAD_json2python.py [-h] [--split SPLIT] [--workers WORKERS]
                            [--tokenizer TOKENIZER]
                            data_dir out_dir
      SQuAD_json2python.py: error: the following arguments are required: data_dir, out_dir
    ```
+ after
    + code
    ```
      parser = argparse.ArgumentParser()
      parser.add_argument('--data_dir', type=str, help='Path to SQuAD data directory', default='../data/SQuAD')
      parser.add_argument('--out_dir', type=str, help='Path to output file dir', default='../data/SQuAD')
      parser.add_argument('--split', type=str, help='Filename for train/dev split',
                          default='dev-v1.1')
      parser.add_argument('--workers', type=int, default=None)
      parser.add_argument('--tokenizer', type=str, default='corenlp')
    ```
  + result
    ```
      Loading dataset ../data/SQuAD/dev-v1.1.json
      Will write to file ../data/SQuAD/dev-v1.1-processed-corenlp.txt
    ```
+ parser.register()
	+ http://blog.csdn.net/a1964543590/article/details/69791760

    ```
    parser = argparse.ArgumentParser()#创建一个命令解析器的句柄
	#注册一个命令解析器参数类型,其中lambda v: v.lower()=="true"
	#是代表一个匿名函数的实现，主要判断获取到的参数v转换成小写后是否等于true
	parser.register("type", "bool", lambda v: v.lower() == "true")
	#这个接口主要是添加命令解析器命令。其中下面使用的type就是上面注册的类型(注意:bool 是带双引号的)
	parser.add_argument(
  	"--debug",
  	type="bool",
  	nargs="?",
  	const=True,
  	default=False,
  help="Use debugger to track down bad values during training")
    ```
