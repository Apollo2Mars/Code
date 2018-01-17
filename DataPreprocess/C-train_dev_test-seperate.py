# -*- coding:utf-8 -*-
#
# input file with segment and pos_tagging information
#

import re
import codecs
import random

filepath = 'data_output/GJYW_UTF-8_2.txt'
# filepath = 'data_output/test'

# seg file split
file_seg_train = codecs.open('data_output/zh-seg_train.txt', 'w', 'utf-8') # 0.85
file_seg_dev = codecs.open('data_output/zh-seg_dev.txt', 'w', 'utf-8') # 0.05
file_seg_test = codecs.open('data_output/zh-seg_test.txt', 'w', 'utf-8') # 0.1
# pos file split
file_pos_train = codecs.open('data_output/zh-pos_train.txt', 'w', 'utf-8') # 0.85
file_pos_dev = codecs.open('data_output/zh-pos_dev.txt', 'w', 'utf-8') # 0.05
file_pos_test = codecs.open('data_output/zh-pos_test.txt', 'w', 'utf-8') # 0.1
# test file for bnlp-zh test
file_test = codecs.open('data_output/zh-test.txt', 'w', 'utf-8') # 0.1

# u或U开头的字符串表示unicode字符串
strPunc = u"`-=[]\;,，.~!@#$%^&*()_+{}:<>?·=【】、；‘，。～！@#￥%……&×（）—+『』|：“《》？「」！"+'"'

#
# make segment train data and random split it with 9:1
#
posSplit = re.compile('/[\w]+')

iCount = 0

iLineCount = 0
iLengthCount = 0

with codecs.open(filepath, 'r', 'utf-8') as f:
    for lineFull in f:
        # avoid  '忧国忧民i 一身/n 浩然/a 正气/n'
        len1 = len(lineFull.split())
        len2 = len(re.split('/[\w]+', lineFull.strip()))
        if len1 + 1 is not len2:
            continue
        # delete all '
        # lineFull = lineFull.replace(r'[\s]+', 'aaa')
        lineFull = re.sub(r'[\s]+', ' ', lineFull)

        # delete first line indent and '/r/n'
        lineFull = lineFull.strip()
        # if line is empty continue
        if len(lineFull) == 0:
            continue
        # split the complete sentence into sublines
        sub_lines = re.split(r'[，。？!！;；]\s*/w', lineFull)
        for line in sub_lines:
            # delete /r/n
            line = line.strip()
            if len(line) == 0:
                continue
            # record original line
            oldLine = line
            # Build form to facilitate regular expression lookup
            line = line + ' '
            #
            # count sub line number
            iLineCount = iLineCount + 1
            # count length of all line
            iLengthCount = iLengthCount +len (line)
            # prepare line for test, a 10% chance of being a test sentence.
            lineForTest = line
            #
            # get seg and pos file
            #
            linePosListWithSlash = []
            linePosList = []
            for m in posSplit.finditer(line):
                linePosListWithSlash.append(m.group())
            for tmp in linePosListWithSlash:
                tmp = tmp[1:] # delete /
                linePosList.append(tmp)

            if len(linePosList) < 0:
                print(line)
                print('not find pos')
            else:
                lineSegList = []
                # contain an empty ''
                lineSegListTmp = re.split('/[\w]+ ', line)
                # delete the last '' in seg list
                if '' in lineSegListTmp:
                    lineSegListTmp.remove('')
                    lineSegList = lineSegListTmp
                else:
                    lineSegList = lineSegListTmp
                # get seg list length and pos list length
                iSegLen = len(lineSegList)
                iPosLen = len(linePosList)
                # define line for write
                strSeg = ''
                strPos = ''
                # pos length not equal to seg length
                if iSegLen != iPosLen:
                    iCount = iCount + 1
                    # print(oldLine)
                    # print(line)
                    # print('seg numbers is line is # ' + str(iSegLen))
                    # print('pos numbers is line is # ' + str(iPosLen))
                    # print('seg length not equal to pos length')
                else:
                    iPos = 0
                    for wordTmp in lineSegList:
                        if len(wordTmp) is 0:
                            break
                        # get word pos
                        tmpPos = linePosList[iPos]
                        iPos = iPos+1

                        iSeg = 0
                        iWordLength = len(wordTmp)
                        # char level
                        for charTmp in wordTmp:
                            tmpSeg = '###'

                            if iWordLength is 1:
                                tmpSeg = 'S'
                            elif iWordLength is 2:
                                if iSeg is 0:
                                    tmpSeg = 'B'
                                elif iSeg is 1:
                                    tmpSeg = 'E'
                            else:
                                if iSeg is 0:
                                    tmpSeg = 'B'
                                elif iSeg is len(wordTmp)-1:
                                    tmpSeg = 'E'
                                else:
                                    tmpSeg = 'I'
                            iSeg = iSeg + 1

                            strTmp = charTmp + '\t' + tmpSeg + '\n'
                            strSeg.join(strTmp)
                            strSeg = strSeg + strTmp

                        strTmp = wordTmp + '\t' + tmpPos + '\n'
                        strPos = strPos + strTmp

                fTemp = random.random()

                if fTemp < 0.85:
                    # print(len(strSeg))
                    file_seg_train.writelines(strSeg)
                    file_seg_train.writelines("\n")
                    file_pos_train.writelines(strPos)
                    file_pos_train.writelines("\n")

                elif 0.85 < fTemp < 0.9:
                    file_seg_dev.writelines(strSeg)
                    file_seg_dev.writelines("\n")

                    file_pos_dev.writelines(strPos)
                    file_pos_dev.writelines("\n")
                else:
                    file_seg_test.writelines(strSeg)
                    file_seg_test.writelines("\n")

                    file_pos_test.writelines(strPos)
                    file_pos_test.writelines("\n")
                    # line with space
                    file_test.writelines(lineForTest)
                    file_test.writelines("\n")

# test file close
file_pos_train.close()
file_pos_dev.close()
file_pos_test.close()
# seg file close
file_seg_train.close()
file_seg_dev.close()
file_seg_test.close()
# test file
file_test.close()

print('error line count is ' + str(iCount))

print('sub line count is ' + str(iLineCount))
print('line length is ' + str(iLengthCount))
print('average length of sub line is ' + str(iLengthCount/(iLineCount+1)))
