
def words_count(list_a):
    count_dict = {}
    if not isinstance(list_a, list) or list_a == []:
        print('输入非列表或列表为空!')
    for word in list_a:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1
    return count_dict


if __name__ == '__main__':
    list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']
    result = words_count(list_s)
    print(result)
