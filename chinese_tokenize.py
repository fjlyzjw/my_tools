#author: Jiawen
#date: 2020.06.11
#chinese tokenization using jieba lib
#usage: python chinese_tokenize.py -t <text> [-i <input_text_file> -o <output_text_file>]

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, string
import operator
import argparse
import jieba
import importlib

cn_punc = ['！','？','｡','＂','＃','＄','％','＆','＇','（','）','＊','＋','，','－','／','：','；','＜','＝','＞','＠','［','＼','］','～']

def is_ch_valid(ch):
    if ch == ' ':
        return False
    if '\u4e00' <= ch <= '\u9fff':
        return True
    if '\u3000' <= ch <= '\u303f':
        return True
    if ch in cn_punc:
        return True
    elif ch.encode( 'UTF-8' ).isalpha():
        return True
    elif ch.encode( 'UTF-8' ).isdigit():
        return True
    elif ch in string.punctuation:
        return True

    return False

def filter_no_valid(sent):
    res = ""
    for i in sent:
        if is_ch_valid(i)== False:
            continue
        res += i
    return res

def tokenize_file(input_file,output_file=None):
    if output_file:
        fout = open(output_file,'w',encoding='utf8')
    else:
        fout = None
    with open(input_file,'r',encoding='utf8') as f:
        for line in f:
            line = line.strip('\n')
            line = filter_no_valid(line)
            seg = jieba.cut(line)  
            line = ' '.join(seg)

            if not fout:
                print(line)
            else:
                fout.write(line+'\n')

def tokenize_text(text,output_file=None):
    if output_file:
        fout = open(output_file,'w',encoding='utf8')
    else:
        fout = None
            
    line = text
    line = line.strip('\n')
    line = filter_no_valid(line)
    seg = jieba.cut(line)  
    line = ' '.join(seg)
            
    if fout == None:
        print(line)
    else:
        fout.write(line+'\n')
            


if __name__ == "__main__":

    importlib.reload(sys)

    parser = argparse.ArgumentParser(description='process user given parameters')
    parser.add_argument("-i", "--inputfile", required = False, dest = "inputfile", default = None, help = "input file")
    parser.add_argument("-o", "--output", required =  False, dest="output", default = None, help = "output file")
    parser.add_argument("-t", "--text", required = False, dest = "text", default = None, help = "input text")


    args = parser.parse_args()
    file_path = args.inputfile
    output = args.output
    text = args.text

    if not file_path and not text:
        print("please input a file (-i <file_name>)or texts (-t <texts>)")
    elif file_path and not text:
        tokenize_file(file_path,output)
    else:
        tokenize_text(text,output)