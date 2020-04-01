from bs4 import BeautifulSoup
import requests
from typing import List
from time import sleep

# class

req_url = 'https://sh.lianjia.com/zufang/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36', 'Sec-Fetch-Mode': 'navigate'}
req = requests.get(req_url, headers=headers)
soup = BeautifulSoup(req.text)

# page_data: bs4.element.Tag 对象组成的 list
page_data = soup.find_all(class_='content__list--item--main')

# 需要抓取的房屋信息


# 是否新增加的可租房屋
is_new = soup.select('.content__list--item--main')[0].select('.content__item__tag--is_new')[0].string
# 看房时间
is_key = soup.select('.content__list--item--main')[0].select('.content__item__tag--is_key')[0].string
# 品牌： 贝壳优选
brand = soup.select('.content__list--item--main')[0].select('.brand')[0].string.strip()
# 月租 元/月， example 5500
price = soup.select('.content__list--item--main')[0].select('.content__list--item-price')[0].em.string
# 此房屋链接 example /zufang/SH2326134993455693824.html
house_url = 'https://sh.lianjia.com' + soup.select('.content__list--item--main')[0].a.get_attribute_list('href')[0]
# 出租方式  example 整租
rent_type = soup.select('.content__list--item--main')[0].a.string.strip().split('·')[0]
# 房屋所在区县
# des =
# 房屋所在二级区域
# 房屋所在小区名称
