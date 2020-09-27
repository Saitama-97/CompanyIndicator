import requests
import json
from bs4 import BeautifulSoup
from urllib import parse
import re

# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
# }
# urls = ['https://www.xuexi.cn/1830b4408a86b65993236e4b029b3ff9/e43e220633a65f9b6d8b53712cba9caa.html',
#         'https://www.xuexi.cn/lgpage/detail/index.html?id=4335297215960014492',
#         'https://www.xuexi.cn/1830b4408a86b65993236e4b029b3ff9/e43e220633a65f9b6d8b53712cba9caa.html']
# resp = requests.get(url,headers=headers)
# text = resp.content.decode('utf-8')
# soup = BeautifulSoup(text,'html.parser')
# page = soup.find('div',id='C63d493x62hc00')
# print(page)

# url = urls[2]


def getContent(url):
    jsUrlTemp = url.rsplit('/')

    if 'id' in url:
        query = dict(parse.parse_qsl(parse.urlsplit(url).query))
        jsUrl = jsUrlTemp[0] + '//boot-source.xuexi.cn/data/app/' + query['id'] + '.js'
        res = requests.get(jsUrl)
        res.encoding = 'utf-8'
        data = json.loads(res.text.lstrip('callback(').rstrip(')'))
        title = data['title']
        pattern = re.compile(r'<[^>]+>', re.S)
        content = pattern.sub('', data['content']).replace(' ', '。')
    else:
        jsUrl = jsUrlTemp[0] + '//' + jsUrlTemp[2] + '/' + jsUrlTemp[3] + '/data' + jsUrlTemp[4].replace('html', 'js')
        res = requests.get(jsUrl)
        res.encoding = 'utf-8'
        for key, value in json.loads(res.text.lstrip('globalCache = ').rstrip(';'), encoding='utf-8').items():
            if key == 'fp8ttetzkclds001':
                pattern = re.compile(r'<[^>]+>', re.S)
                content = pattern.sub('', value['detail']['content']).replace(' ', '。')
    return content

if __name__ == '__main__':
    content = getContent('https://www.xuexi.cn/lgpage/detail/index.html?id=3903757024715635420')
    print(type(content))