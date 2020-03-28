
for n in range(1, 200):
    sq = n * n
    str_sq = str(sq)

    # 通过切片把字符串逆序
    isstr_sq = str_sq[::-1]
    if str_sq == isstr_sq:
        print(n)

    # # 方法二：转成list后比较
    list_sq = list(str_sq)
    reverse_sq = list(reversed(str_sq))
    if list_sq == reverse_sq:
        print(n)

    # 方法三： 逐个遍历比较
    for i in range(len(str_sq)):
        if str_sq[i] != str_sq[-(i+1)]:
            break
    else:
        print(n)
