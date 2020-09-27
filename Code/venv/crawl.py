import json
import csv
import sys
import pandas
from urllib import parse
import re
import requests


def getContent(url):
    jsUrlTemp = url.rsplit('/')

    try:
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
            jsUrl = jsUrlTemp[0] + '//' + jsUrlTemp[2] + '/' + jsUrlTemp[3] + '/data' + jsUrlTemp[4].replace('html',
                                                                                                             'js')
            res = requests.get(jsUrl)
            res.encoding = 'utf-8'
            for key, value in json.loads(res.text.lstrip('globalCache = ').rstrip(';'), encoding='utf-8').items():
                if key == 'fp8ttetzkclds001':
                    pattern = re.compile(r'<[^>]+>', re.S)
                    content = pattern.sub('', value['detail']['content']).replace(' ', '。')
        return content
    except:
        print("error+", url)


if __name__ == '__main__':
    with open('news.json', 'r', encoding='utf-8') as f:
        load_dict = json.load(f)
    file = open('news.csv', 'w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['title', 'publishTime', 'url'])
    for i in enumerate(load_dict):
        try:
            i = i[1]
            cont = getContent(i['url'])
            print(i['title'], i['publishTime'].split(' ')[0], i['url'], cont)
            writer.writerow([i['title'], i['publishTime'].split(' ')[0], i['url'], cont])
        except:
            print("fail:" + i['url'])
    f.close()
    df = pandas.read_csv('news.csv', encoding='utf_8')
    df.to_csv('news.csv', encoding='utf_8_sig')
