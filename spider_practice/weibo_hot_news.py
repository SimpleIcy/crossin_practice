import requests

url = 'https://weibo.com/a/hot/realtime'
headers = {
    'Cookie': "_s_tentry=www.51testing.com; Apache=7218768281992.733.1557470780610; "
              "SINAGLOBAL=7218768281992.733.1557470780610; ULV=1557470780619:1:1:1:7218768281992.733.1557470780610:; "
              "SUB=_2AkMqJCTtf8NxqwJRmPARzmPibIt_zwrEieKceNU2JRMxHRl-yT9jqlwntRB6AaQKAgS7Ao9N77zJ-0tzglcgpMX6s-G9; "
              "SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFJZ3Wc6dIJ4bc-OM043J1g; UOR=www.51testing.com,widget.weibo.com,"
              "news.ifeng.com; Ugrow-G0=9ec894e3c5cc0435786b4ee8ec8a55cc; YF-V5-G0=b1b8bc404aec69668ba2d36ae39dd980; "
              "WBStorage=42212210b087ca50|undefined",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.97 Safari/537.36',
}

data = requests.get(url, headers=headers).text
with open('weibo_hot_news.html', 'w', encoding='utf-8') as f:
    f.write(data)
    f.close()
