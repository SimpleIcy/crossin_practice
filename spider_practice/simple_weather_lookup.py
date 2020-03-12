import requests


while True:
    city = input('输入要查询的城市：')
    if city:
        info = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
        weather = info.json()
        if weather.get('desc') == 'OK':
            date = weather.get('data').get('forecast')[0].get('date')
            high_temperature = weather.get('data').get('forecast')[0].get('high')
            low_temperature = weather.get('data').get('forecast')[0].get('low')
            weather_type = weather.get('data').get('forecast')[0].get('type')
            print('%s\n%s\n%s\n%s' % (date, high_temperature, low_temperature, weather_type))
        else:
            print('未获得城市')
            continue
    else:
        break
