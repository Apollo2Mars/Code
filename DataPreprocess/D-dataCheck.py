import  codecs


# check line of tag lines
def check_line_length(file):
    b_error_exist = False
    with codecs.open(file, 'r', 'utf-8') as f:
        last_4_line = ''
        last_3_line = ''
        last_2_line = ''
        last_1_line = ''
        for line in f:
            line = line.strip()
            last_4_line = last_3_line
            last_3_line = last_2_line
            last_2_line = last_1_line
            last_1_line = line
            tmpLen = len(line)
            if tmpLen != 3:
                if tmpLen != 0:
                    print('###')
                    print(last_4_line)
                    print(last_3_line)
                    print(last_2_line)
                    print(last_1_line)
                    print(line)
                    print('length is '+ str(len(line)))

                    b_error_exist = True
    return b_error_exist


# find continuous blank lines
# print blank lines
def check_multi_line(file):
    with codecs.open(file, 'r', 'utf-8') as f:
        i_line_count = 0
        i_null_line_count = 0
        b_last_line_is_null = False
        for line in f:
            line = line.strip()
            # print(line)
            i_line_count = i_line_count + 1
            if len(line) == 0:
                if b_last_line_is_null is True:
                    i_null_line_count = i_null_line_count + 1
                    # print('Null count' + str(i_null_line_count))
                    # print('Line count ' + str(i_line_count))

                b_last_line_is_null = True
            else:
                b_last_line_is_null = False


def delete_continous_blank_lines(file, file_output):
    file_output_s = codecs.open(file_output, 'w', 'utf-8')
    with codecs.open(file, 'r', 'utf-8') as f:
        i_line_count = 0
        i_null_line_count = 0
        b_last_line_is_null = False
        for line in f:
            line = line.strip()
            # print(line)
            i_line_count = i_line_count + 1
            if len(line) == 0:
                if b_last_line_is_null is True:
                    i_null_line_count = i_null_line_count + 1
                    # print('Null count' + str(i_null_line_count))
                    # print('Line count ' + str(i_line_count))
                else:
                    file_output_s.writelines(line)
                    file_output_s.writelines('\n')
                b_last_line_is_null = True

            else:
                b_last_line_is_null = False
                file_output_s.writelines(line)
                file_output_s.writelines('\n')


def make_seg_corpus():
    # file_input = 'data_output/zh-seg_train.txt'
    # file_output = 'data_output/zh-seg_train.txt-check'

    # file_input = 'data_output/zh-seg_dev.txt'
    # file_output = 'data_output/zh-seg_dev.txt-check'

    file_input = 'data_output/zh-seg_test.txt'
    file_output = 'data_output/zh-seg_test.txt-check'

    if check_line_length(file_input) is False:  # error not exist
        print("file_input not contains error")
        # check_multi_line(file_input)
        delete_continous_blank_lines(file_input, file_output)
    else:
        print("error occur in file input")


def make_pos_corpus():
    # file_input = 'data_output/zh-pos_test.txt'
    # file_output = 'data_output/zh-pos_test.txt-check'

    file_input = 'data_output/zh-pos_dev.txt'
    file_output = 'data_output/zh-pos_dev.txt-check'

    # file_input = 'data_output/zh-pos_train.txt'
    # file_output = 'data_output/zh-pos_train.txt-check'

    delete_continous_blank_lines(file_input, file_output)

if __name__ == '__main__':
    # make_seg_corpus()
    make_pos_corpus()
