import requests
from time import sleep
from typing import List, Any
import csv
# 参考别人的代码写的，自己没找到链接的规律。
# 写代码时，应该多注意单选数据保存使用的list在每次循环中应该重新初始化的。
# 此程序未完成考虑返回数据很多为空的情况，导致很多时候抓的数据不全。
# 参考https://gitee.com/fridge86/study/blob/master/Crossin学习小组/04知乎首页推荐.py


class ZhiHuQA:
    def __init__(self):
        self.headers = {'cookie': '_zap=03ccf7b2-7a00-4ddd-a4e6-cc20edc15232; _xsrf=9f8ccee3-d4e4-4ba5-9087-958b49b81415; d_c0="AOAgo26m7A-PThQw9LneieS4o9TBuz1ngnk=|1566359358"; q_c1=64bb1b0a67cb4efaa3869d8c259f0d18|1579417896000|1579417896000; capsion_ticket="2|1:0|10:1585017946|14:capsion_ticket|44:Mzk2MDkwOWUwOTFmNDQ0ZjkxMTQ3MDg3YjNkMzI0NWY=|7930f86e326f072f1470cdffe66e6bd5ad80fc08d86ae61877a3274f12d20e69"; z_c0="2|1:0|10:1585017973|4:z_c0|92:Mi4xdEYzNEFRQUFBQUFBNENDamJxYnNEeWNBQUFDRUFsVk5kUUdoWGdBTkZXRnhBMFhkMHgydzNsYmZlTWRjSU9oeG5B|af9b5c736ce7e40513ba9d8d2bd7c9400c3297e267d953037101ebfa133d6cb0"; tst=r; _ga=GA1.2.1183365960.1585289482; _gid=GA1.2.172492695.1585552780; SESSIONID=Owqidzn7Rsq6zkBxpTvb4a9unbm2Uo21iyDCef3uzIp; JOID=Ul4TA09ZlJ0nwD3_Gll2ger-URMMEOPqSqBBkSsP4ewXvlK7YtMPHnnCO_kY2Y8P0RWpxjftb97F3JP3UeGFnlQ=; osd=U1wRC09Ylp8vwDz9GFF2gOj8WRMNEuHiSqFDkyMP4O4VtlK6YNEHHnjAOfEY2I0N2RWoxDXlb9_H3pv3UOOHllQ=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1585289480,1585552779,1585620970; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1585620970; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1585645672|1585645662',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                      'like Gecko) Chrome/78.0.3904.97 Safari/537.36',
                        'refer': 'https://www.zhihu.com/',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin'}
        self.title = ['问题', '答题者', '答题者标题', '答题者粉丝', '点赞数', '评论数', '答题摘要']
        self.page_number = 2
        self.after_id = 5
        self.page_plus = 1
        self.after_id_plus = 6
        self.url = r'https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=2322e6893aaebfe7d8094ecc48111c5e&desktop=true&page_number={0}&limit=6&action=down&after_id={1}&ad_interval=-1'.format(
            str(self.page_number), str(self.after_id))

    def get_qa(self, pages=10):
        for page in range(0, pages):
            req = requests.get(self.url, headers=self.headers)
            zhihu_data = req.json()
            for item in zhihu_data['data']:
                answer: List[Any] = []
                try:
                    answer.append(item.get('target').get('title'))
                    answer.append(item.get('target').get('author').get('name'))
                    answer.append(item.get('target').get('author').get('headline'))
                    answer.append(item.get('target').get('author').get('followers_count'))
                    answer.append(item.get('target').get('voteup_count'))
                    answer.append(item.get('target').get('comment_count'))
                    answer.append(item.get('target').get('excerpt'))
                except :
                    pass
                with open('zhihu_QA.csv', 'a', encoding='cp936') as f:
                    csv_writer = csv.writer(f)
                    try:
                        csv_writer.writerow(answer)
                    except :
                        pass
            # 间隔抓取次数，防止网站屏蔽
            sleep(3)
            self.page_number += self.page_plus
            self.after_id += self.after_id_plus

    def write_title(self):
        with open('zhihu_QA.csv', 'w', encoding='cp936') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.title)


if __name__ == '__main__':
    reader = ZhiHuQA()
    reader.write_title()
    reader.get_qa()



