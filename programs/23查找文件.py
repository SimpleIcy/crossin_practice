# -*- coding: utf-8 -*-
import os
from typing import List, Dict


def find_file(keyword, input_dir='.'):
    # 初始化记录包含关键字的文件夹，文件名
    found_list: Dict[str] = {'dirs': [], 'files': []}
    all_files: List[str] = []
    all_dirs: List[str] = []

    for root, dirs, files in os.walk(input_dir):
        for _name in files:
            all_files.append(os.path.join(root, _name))
        for _name in dirs:
            all_dirs.append(os.path.join(root, _name))
    for file in all_dirs:
        if keyword in file:
            found_list['dirs'].append(file)
    for file in all_files:
        if keyword in file:
            found_list['files'].append(file)
        else:
            try:
                with open(file, encoding='utf-8') as f:
                    for line in f:
                        if keyword in line:
                            found_list['files'].append(file + ' : ' + line.strip())
                            break
            except:
                pass
    return found_list


if __name__ == '__main__':
    keyword = input('匹配关键字：')
    path = input('搜索目录（不填默认为当前目录）：')
    if not path.strip():
        path = '.'

    result = find_file(keyword, path)
    print('+++++++ 匹配结果 +++++++')
    print('包含关键字的文件夹:')
    if not result['dirs']:
        print('无')
    for directory in result['dirs']:
        print(directory)
    print('包含关键字的文件:')
    if not result['files']:
        print('无')
    for name in result['files']:
        print(name)
