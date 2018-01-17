# -*- coding:utf-8 -*-
# author : apollo.sun
# function : Make scattered small files into a large file
# corpus : 国家语委平衡语料，共195M
import os
import codecs


# Iterate through the specified directory 'data'
def each_file(folder__input, file__output):

    path_dir = os.listdir(folder__input)
    count = 0
    count_err = 0
    for single_file in path_dir:
        try:
            # read file, and count ++
            read_file('data/'+single_file, file__output)
            count = count + 1
        except:
            # print error count
            print(single_file)
            count_err = count_err + 1
    print('the number of suitable encode file is ' + str(count))
    print('the number of error encode file is ' + str(count_err))


# Read each file and write to a file
def read_file(filename, file__output):
    # 指定一个编码打开文件，使用这个方法打开的文件读取返回的将是unicode
    # r 代表read
    tmp_file = codecs.open(filename, 'r', 'gbk')
    for eachLine in tmp_file:
        # print(eachLine)
        file__output.writelines(eachLine)
    tmp_file.close()

if __name__ == '__main__':
    # folder name
    folder_input = "data"
    file_output = codecs.open('data_output/GJYW_UTF-8_1.txt', 'w', 'utf-8')
    each_file(folder_input, file_output)
    file_output.close()
