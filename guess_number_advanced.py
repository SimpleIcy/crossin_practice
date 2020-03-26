import requests
import os


def guess_num():
    all_data = []
    all_player = []
    if os.path.exists('data.txt'):
        with open('data.txt') as f:
            for line in f.readlines():
                all_data.append(list(line.strip().split()))
    else:
        with open('data.txt', 'w') as f:
            f.close()
    if all_data:
        for i in all_data:
            all_player.append(i[0])
    player = str(input('请输入你的名字：\t'))
    exist_player = False
    if player in all_player:
        exist_player = True
        play_index = all_player.index(player)
        least_times = int(all_data[play_index][2])
        print('%s,你已经玩了%s次，最少%s轮猜出答案，平均%s轮猜出答案，开始游戏！' % (player, all_data[play_index][1],  all_data[play_index][2], all_data[play_index][3]))
    else:
        least_times = 0
        print('%s,你已经玩了0次，最少0轮猜出答案，平均0轮猜出答案，开始游戏！' % player)

    times = 0
    guess = True
    random_num = int(requests.get('https://python666.cn/cls/number/guess/').text)
    while guess:
        all_guess_nums = []
        try:
            you_num = int(input('请输入1-100的数字:\t'))
        except ValueError:
            print('输入错误，请输入100以内的数字!')
            continue
        if 100 > you_num > random_num:
            times += 1
            print("猜大了再试试")
        elif 0 < you_num < random_num:
            times += 1
            print("猜小了再试试")
        elif you_num == random_num:
            times += 1
            print("猜对了，你一共猜了%s轮" % times)
            all_guess_nums.append(times)
            if least_times == 0 or least_times > times:
                least_times = times
            if exist_player:
                # 将存在用户的数据的list更新
                play_index = all_player.index(player)
                exist_all = int(all_data[play_index][1]) + 1
                exist_alltimes = sum(all_guess_nums) + int(all_data[play_index][1]) * float(all_data[play_index][3])
                guess_avg = round(exist_alltimes / exist_all, 2)
                all_data[play_index] = [player, exist_all, least_times, guess_avg]
                print('%s,你已经玩了%s次，最少%s轮猜出答案，平均%s轮猜出答案' % (player, exist_all, least_times, guess_avg))

            else:
                # 用户猜数数据新增此用户的数据
                all_data.append([player, 1, least_times, times])
                all_player.append(player)
                print('%s,你已经玩了%s次，最少%s轮猜出答案，平均%s轮猜出答案' % (player, 1, least_times, times))
                exist_player = True
            times = 0
            choose = str(input('是否继续游戏？（输入y继续，其他退出）'))
            if choose == 'y':
                guess = True
                random_num = int(requests.get('https://python666.cn/cls/number/guess/').text)
            else:
                guess = False
                print("退出游戏，欢迎下次再来！")
    # 将数据重新写入用户数据记录文件
    with open('data.txt', 'w') as f:
        for user in all_data:
            for x in user:
                user[user.index(x)] = str(x)
            userdata = ' '.join(user)
            f.write(userdata)
            f.write('\n')


if __name__ == '__main__':
    guess_num()
