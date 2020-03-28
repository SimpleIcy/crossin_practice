import re


with open('from.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        all_words = '' + line
    f.close()

english_words = re.findall(pattern='[a-zA-Z]+', string=all_words)
sorted_words = sorted(english_words)

with open('to.txt', 'w') as f:
    for word in sorted_words:
        f.write(word+'\n')
    print('完成英文单词提取并保存成功!')
    f.close()
