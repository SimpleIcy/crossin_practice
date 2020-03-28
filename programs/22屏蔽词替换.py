def load_blocked():
    with open('pingbi.txt', encoding='utf-8') as f:
        global shadow_words
        shadow_words = [l.strip() for l in f.readlines() if l]
        # 此处去掉带有的空格，换行符，空字符


def replace_words(input_str):
    for word in shadow_words:
        if word in input_str:
            input_str = input_str.replace(word, '*'*len(word))
    return input_str


if __name__ == '__main__':
    load_blocked()
    while True:
        str_before = input('请输入一段文字:')
        if not str_before:
            print('输入为空，退出!')
            break
        print(replace_words(str_before))
