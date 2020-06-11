# my_tools
Several commandline tools implemented by myself for data preprocessing.

Including:
1. Chinese tokenization based on jieba lib
2. Data splitation

# Usage
## Chinese tokenization
```
python chinese_tokenize.py -t <text> [-i <input_text_file> -o <output_text_file>]
```
## Data split
```
python data_split.py -i <input_text_file> -r <train_set_ratio> -o <output_text_file_prefix>
example:
python data_split.py -i data.txt -r 0.8 -o out
```
