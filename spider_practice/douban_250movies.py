import requests
from PIL import Image
from io import BytesIO
from time import sleep
from typing import List, Dict, Any
import csv

# 批量获取250部电影的id,电影名、评分、主演、豆瓣链接、等数据，保存数据到本地 csv 文件；


START = 0
movies_data = []
movie_image_url = []
for i in range(5):
    movies_url = f'https://api.douban.com/v2/movie/top250?start={START}&count=50&apikey=0df993c66c0c636e29ecbb5344252a4a'
    data_50movies = requests.get(movies_url, headers={'user-agent': 'chrome'}).json()
    for j in range(50):
        movie_data = {'movie_id': data_50movies.get('subjects')[j]['id'],
                      'movie_name': data_50movies.get('subjects')[j]['title'],
                      'movie_rating': data_50movies.get('subjects')[j]['rating']['average']}
        movie_casts: List[Any] = []
        for k in data_50movies.get('subjects')[j]['casts']:
            movie_casts.append(k['name'])
        movie_data['movie_casts'] = ','.join(movie_casts)
        movie_data['movie_douban_url'] = data_50movies.get('subjects')[j]['alt']

        movie_image_url.append(data_50movies.get('subjects')[j]['images']['large'])
        movies_data.append(movie_data)
    sleep(3)
    START += 50
# 将电影数据写入csv文件中
headers = ['movie_id', 'movie_name', 'movie_rating', 'movie_casts', 'movie_douban_url']
with open('douban_250movies.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(movies_data)

# 将所有电影的海报图片下载下来并保存
for x in range(len(movie_image_url)):
    url = movie_image_url[x]
    r = requests.get(url, headers={'user-agent': 'chrome'})
    pic = Image.open(BytesIO(r.content))
    pic.save('%s.webp' % movies_data[x]['movie_name'])
    sleep(3)



