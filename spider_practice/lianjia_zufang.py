from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Any
from time import sleep
import csv


class LianJiaZuFang:
    """
    链接租房信息抓取并保存到CSV文件。
    :arg
    """
    def __init__(self):
        self.req_home_url = 'https://sh.lianjia.com/zufang/'
        self.headers = {'Sec-Fetch-Dest': 'document', 'Connection': 'keep-alive', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36', 'Sec-Fetch-Mode': 'navigate', 'Cookie': 'lianjia_uuid=3b401430-d5ec-4ca6-9f6a-1b5089007315; lianjia_ssid=69cc3c70-30ef-4ff6-9d6b-9e35a6af6038; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNmI4ZmNjNzZkYjA0NjBiMjdlYWVkZDRhZDU1ZGZjNDI1YTQzN2FkMWVjYzllYmQ4ZTdkNjdjNWQ2MzBjM2QzMDZiOGJmODhmZTdhOTY3YTk1ZmQ1NDY2Zjg4M2JjM2YxZjY5ZDVhZWYyNjNiMzk1ZWE2N2JiYWQwNjM3NzdiNWFjNmEwYjBlZTY1ODlmODUzMjkzM2Y4NmQxZTQzMjMzMTZmNDdiYTVmNzgwOGEwNTIzODY4MWUwOTNiMDFkOWQ3NmNjODMwZTEwZTcwZmIyZWE1Yzc2MTkyMjJlMDRkNjQwOTUxYmNjNTAyOWU2ODE0M2ZmNjEzOTRjNDI0MjBkMjQwNGZhOWZkMzg2YWM5ZTc4MTQ1MTk3NzQxNWFkMzYwY2Y1N2E3NTI4ZDdhMzYwYzY5MWMzNGEyODkyNmI1ZTk0MGE4NjAzODY1YTdlODUyMjQzYmI5M2Q2MGMyMjA4OVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0YTAyNzQyY1wifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='}
        self.title = ['区县', '区域', '小区', '月租', '格局', '面积', '朝向', '楼层', '链接', '品牌', '出租方式', '看房时间', '新增']
        self.datas: List[Any] = []

    def get_data(self, pages):
        for page in range(1, pages):
            if page > 1:
                try:
                    req = requests.get(self.req_home_url+str(page), headers=self.headers)
                    print(self.req_home_url+str(page))
                except :
                    print('抓取第%s页时，网络requests请求异常！' % page)
                    continue
            else:
                try:
                    req = requests.get(self.req_home_url, headers=self.headers)
                    print(self.req_home_url)
                except:
                    print('抓取首页时，网络requests请求异常！')
                    break
            soup = BeautifulSoup(req.text, features="lxml")
            # page_data: bs4.element.Tag 对象组成的 list
            page_data = soup.select('.content__list--item--main')
            for house in range(len(page_data)):
                # 需要抓取的房屋信息
                house_data: Dict[Any, Any] = {}
                # 是否新增加的可租房屋  不一定有  type: string
                try:
                    is_new = soup.select('.content__list--item--main')[house].select('.content__item__tag--is_new')[0].string
                    house_data['新增'] = is_new
                except IndexError:
                    house_data['新增'] = ''
                # 看房时间  type: string
                is_key = page_data[house].select('.content__item__tag--is_key')[0].string
                house_data['看房时间'] = is_key
                # 品牌： 贝壳优选  type: string
                brand = page_data[house].select('.brand')[0].string.strip()
                house_data['品牌'] = brand
                # 月租 元/月， example 5500  type: string
                price = page_data[house].select('.content__list--item-price')[0].em.string
                house_data['月租'] = price
                # 此房屋链接 example /zufang/SH2326134993455693824.html  type: string
                house_url = 'https://sh.lianjia.com' + page_data[house].a.get_attribute_list('href')[0]
                house_data['链接'] = house_url
                # 出租方式  example 整租  type: string
                rent_type = page_data[house].a.string.strip().split('·')[0]
                house_data['出租方式'] = rent_type
                # 房屋综合信息  dict like ['徐汇-华东理工-梅陇六村', '/', '42㎡', '/南/', '1室1厅1卫', '/', '低楼层（6层）']
                house_info_list = page_data[house].select('.content__list--item--des')[0].get_text().strip().replace(' ', '').split('\n')
                # 房屋所在区县    type: string
                des = house_info_list[0].split('-')[0]
                house_data['区县'] = des
                # 房屋所在二级区域  type: string
                second_des = house_info_list[0].split('-')[1]
                house_data['区域'] = second_des
                # 房屋所在小区名称  type: string
                third_des = house_info_list[0].split('-')[2]
                house_data['小区'] = third_des
                # 房屋面积  type: string  42㎡
                house_size = house_info_list[2]
                house_data['面积'] = house_size
                # 房屋朝向  type: string
                house_direction = house_info_list[3].split('/')[1]
                house_data['朝向'] = house_direction
                # 房屋格局  如一室一厅   type: string
                house_type = house_info_list[4]
                house_data['格局'] = house_type
                # 房屋所在楼层信息  如低楼层（6层）type: string
                house_height = house_info_list[6]
                house_data['楼层'] = house_height
                # 每套房的字典信息存放入总数据列表中。
                self.datas.append(house_data)
            # 请求间隔5秒防止被网站屏蔽
            sleep(2)
        return self.datas

    def save_data(self):
        with open('ShangHaiLianJiaZuFang.csv', 'w', newline='') as f:
            f_csv = csv.DictWriter(f, self.title)
            f_csv.writeheader()
            f_csv.writerows(self.datas)
            
            
if __name__ == '__main__':
    lianjia = LianJiaZuFang()
    lianjia.get_data(101)
    lianjia.save_data()
