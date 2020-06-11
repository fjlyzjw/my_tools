#author: Jiawen
#date: 2020.06.11
#data splitation
#usage: data_split.py -i <input_text_file> -r <train_set_ratio> -o <output_text_file_prefix>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, string
import operator
import getopt
import jieba


def data_seg_split(file_path,ratio,total,out_prefix):
    if not os.path.exists('./splited_seg_data/'):
        os.mkdir('./splited_seg_data/')

    train_path = './splited_seg_data/'+out_prefix+'_train.data'
    val_path = './splited_seg_data/'+out_prefix+'_val.data'
    test_path = './splited_seg_data/'+out_prefix+'_test.data'

    f_train_txt = open(train_path,'w')
    f_val_txt = open(val_path,'w')
    f_test_txt = open(test_path,'w')
    count = 0
    train_num = int(ratio*total)
    val_num = int(((1-ratio)/2)*total)
    test_index = train_num + val_num
    with open(file_path,'r') as f:
        for line in f:
            count += 1
            if count <= train_num:
                f_train_txt.write(line)
            elif train_num < count <= test_index:
                f_val_txt.write(line)
            else:
                f_test_txt.write(line)

    print(train_path+' line number:'+str(train_num)+ '\n'\
        + val_path+' line number:'+str(val_num)+ '\n' \
            + test_path+' line number:'+str(total - train_num - val_num) + '\nsplit done')

	            

if __name__ == "__main__":
    file_path = None
    train_ratio = 0.99

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:r:o:", ["file=","ratio=","output="])
    except getopt.GetoptError:
        print("ERROR! Parameter number error.")
        print("Usage: data_split.py -i <file_name> -r <train_data_ratio> -o <output_prefix>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i","--file"):
            file_path = arg
        elif opt in ("-r","--ratio"):
            train_ratio = arg
            if not float(train_ratio):
                print('-r shoule be float type')
                sys.exit(2)
            train_ratio = float(train_ratio)

        elif opt in ("-o","--output"):
            out_prefix = arg
        else:
            print("Usage: data_split.py -i <file_name> -r <train_data_ratio> -o <output_prefix>")
            sys.exit(2)
    count = -1
    for count, line in enumerate(open(file_path, 'rb')):
        pass
    count += 1

    data_seg_split(file_path,train_ratio,count,out_prefix)

