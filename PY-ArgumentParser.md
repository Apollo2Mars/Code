+ before    
    + code
      parser = argparse.ArgumentParser()
      parser.add_argument('data_dir', type=str, help='Path to SQuAD data directory', default='../data/SQuAD')
      parser.add_argument('out_dir', type=str, help='Path to output file dir', default='../data/SQuAD')
      parser.add_argument('--split', type=str, help='Filename for train/dev split',
                          default='dev-v1.1')
      parser.add_argument('--workers', type=int, default=None)
      parser.add_argument('--tokenizer', type=str, default='corenlp')
  + error
      usage: SQuAD_json2python.py [-h] [--split SPLIT] [--workers WORKERS]
                            [--tokenizer TOKENIZER]
                            data_dir out_dir
      SQuAD_json2python.py: error: the following arguments are required: data_dir, out_dir

+ after
    + code
      parser = argparse.ArgumentParser()
      parser.add_argument('--data_dir', type=str, help='Path to SQuAD data directory', default='../data/SQuAD')
      parser.add_argument('--out_dir', type=str, help='Path to output file dir', default='../data/SQuAD')
      parser.add_argument('--split', type=str, help='Filename for train/dev split',
                          default='dev-v1.1')
      parser.add_argument('--workers', type=int, default=None)
      parser.add_argument('--tokenizer', type=str, default='corenlp')
    
  + result
      Loading dataset ../data/SQuAD/dev-v1.1.json
      Will write to file ../data/SQuAD/dev-v1.1-processed-corenlp.txt
