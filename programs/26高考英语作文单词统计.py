import re
from typing import List, AnyStr


def open_file(path) -> AnyStr:
    with open(path, encoding='utf-8') as f:
        data = f.readlines()
        str_of_data = ''.join(data)
    return str_of_data


def word_filter(data) -> List:
    words_list = re.findall(r'\b\w+\b', data)
    return words_list


if __name__ == '__main__':
    file_path = input('请输入英文纯文本txt文件的路径：')
    txt_data = open_file(file_path)
    words = word_filter(txt_data)
    print('There are %s words in %s' % (len(words), file_path))
