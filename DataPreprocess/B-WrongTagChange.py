# -*- coding:utf-8 -*-
# author : apollo.sun
# function : change A-makeData.py output 'data_output/GJYW_UTF-8_1.txt'
# from
# '/ta','/td', '/te', '/tf', '/th', '/ti', '/tk', '/tm', '/tmq', '/tn', '/tnd', '/tnh', '/tnt', '/to', '/tq', '/tr', '/tu', '/tv', '/tx'
# to
# '/a', '/d', '/e', '/f', '/h', '/i', '/k', '/m', '/mq', '/n', '/nd', '/nh', '/nt', '/o', '/q', '/r', '/u', '/v', '/x'
# Delete some line contains errorTag

import re
import codecs
tagSet = set()

changeTagDic = {'双髻鲨/t ｎ':'双髻鲨/n', 'ｎ/t':'/nt','n/t':'/nt', '/I': 'i', '/ｎ': '/n', '/ta': '/a', '/td': '/d ', '/te': '/e', '/tf': '/f', '/th': '/h', '/ti': '/i', '/tk': '/k', '/tm': '/m', '/tmq': "/mq", '/tn':'/n', '/tnd':'/nd', '/tnh':'/nh', '/tnt':'/nt', '/to':'/o', '/tq':'/q', '/tr':'/r', '/tu':'/u', '/tv':'/v', '/tx':'/x'}
# errorTagList = ['/av', '/t观点', '/01', '/xx']
errorTagList = ['/n分离', '/nz', '/av', '/t观点', '/01', '/t', '/xx']


def check_single_tag(file__input):
    single_tag = '/t'
    count = 0
    with codecs.open(file__input, 'r', 'utf-8') as f:
        for line in f:
            if single_tag in line:
                print(line)
                count += 1
    print(count)


def error_tag_change(file__input, file__output):
    file_output_s = codecs.open(file__output, 'w', 'utf-8')
    del_count = 0
    with codecs.open(file__input, 'r', 'utf-8') as file:
        for line in file:
            flag = False
            # replace error tag
            for tmp in changeTagDic.keys():
                if tmp in line:
                    line = line.replace(tmp, changeTagDic.get(tmp))
                    # print(tmp)
                    # print(line)
            # delete error tag
            for tmp in errorTagList:
                if tmp in line:
                    flag = True
                    del_count += 1
                    # print(tmp)
                    # print(line)
            if flag is False:
                file_output_s.writelines(line)
    print('delete count is ' + str(del_count))
    file_output_s.close()


def tagset_extract(file__input):
    p = re.compile(r'/[\w]+')
    with codecs.open(file__input, 'r', 'utf-8') as f:
        for line in f:
            # m = re.search(r'/[\w]*', line)
            for m in p.finditer(line):
                tagSet.add(m.group().strip())
    print(sorted(tagSet))
    print(len(tagSet))
    tagSet.clear()


if __name__ == '__main__':
    file_input = 'data_output/GJYW_UTF-8_1.txt'
    file_output = 'data_output/GJYW_UTF-8_2.txt'

    tagset_extract(file_input)
    error_tag_change(file_input, file_output)
    tagset_extract(file_output)

    check_single_tag(file_output)
