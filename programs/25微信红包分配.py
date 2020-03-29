import random
from typing import List, Any


def red_package(people, money):
    result: List[Any] = []
    remain = people
    max_money = money / people * 2
    for i in range(people):
        remain -= 1
        if remain > 0:
            red = random.randint(1, min(money - remain, max_money) * 100)
            result.append(red/100)
            money = money - red / 100
        else:
            red = round(money, 2)
            result.append(red)
    return result


if __name__ == '__main__':
    p = int(input('参与抢红包人数：'))
    m = float(input('红包金额（元）：'))
    print('%s个人抢红包分别抢到：' % p)
    for rmb in red_package(p, m):
        print('￥' + str(rmb))
