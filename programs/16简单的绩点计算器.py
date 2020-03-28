
def jidian(score):
    if score < 60:
        return 0
    elif score <= 61:
        return 1.3
    elif score <= 65:
        return 1.7
    elif score <= 70:
        return 2
    elif score <= 74:
        return 2.3
    elif score <= 77:
        return 2.7
    elif score <= 81:
        return 3
    elif score <= 84:
        return 3.3
    elif score <= 89:
        return 3.7
    elif score <= 100:
        return 4
    else:
        return '分数错误'


def calc(jidians, xuefens):
    if not isinstance(jidians, list) or not isinstance(xuefens, list):
        print('传入的绩点记录或学分记录错误!')
    new = []
    for x in range(len(jidians)):
        new.append(jidians[x]*xuefens[x])
    avg_jidian = sum(new)/sum(xuefens)
    print('现在的平均绩点为：%.2f' % avg_jidian)


if __name__ == '__main__':
    jidians = []
    xuefens = []
    i = 1
    while True:
        score = int(input('输入第%s门课程分数：' % i))
        xuefen = float(input('输入第%s门课程学分：' % i))
        jidians.append(jidian(score))
        xuefens.append(xuefen)
        calc(jidians, xuefens)
        i += 1
