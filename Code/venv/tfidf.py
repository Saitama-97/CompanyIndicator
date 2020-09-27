import csv
import wordcloud
import jieba
import jieba.analyse as ana
import jieba.posseg as psg
import cv2
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib.font_manager import _rebuild

_rebuild()

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams["axes.unicode_minus"] = False


def comTime(start, end, today):
    try:
        s = datetime.strptime(start, '%Y/%m/%d')
        e = datetime.strptime(end, '%Y/%m/%d')
        t = datetime.strptime(today, '%Y/%m/%d')
        if s <= t <= e:
            return True
        else:
            return False
    except:
        pass


if __name__ == '__main__':
    with open('news.csv', newline='', encoding='utf-8') as csvfile:
        next(csvfile)
        rows = csv.reader(csvfile)
        corpus_1912 = ''
        corpus_1911 = ''
        corpus_1910 = ''
        corpus_1909 = ''
        corpus_1908 = ''
        for row in rows:
            if comTime('2019/12/1', '2019/12/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1912 += sentence
            elif comTime('2019/11/1', '2019/11/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1911 += sentence
            elif comTime('2019/10/1', '2019/10/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1910 += sentence
            elif comTime('2019/9/1', '2019/9/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1909 += sentence
            elif comTime('2019/8/1', '2019/8/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1908 += sentence

        ana.set_stop_words('stopwords.txt')
        keywords_1912 = ana.extract_tags(sentence=corpus_1912, topK=30, allowPOS=('ns', 'n', 'nr'), withWeight=True)
        print("keywords_1912 =", keywords_1912)
        keywords_1911 = ana.extract_tags(sentence=corpus_1911, topK=30, allowPOS=('ns', 'n', 'nr'), withWeight=True)
        print("keywords_1911 =", keywords_1911)
        keywords_1910 = ana.extract_tags(sentence=corpus_1910, topK=30, allowPOS=('ns', 'n', 'nr'), withWeight=True)
        print("keywords_1910 =", keywords_1910)
        keywords_1909 = ana.extract_tags(sentence=corpus_1909, topK=30, allowPOS=('ns', 'n', 'nr'), withWeight=True)
        print("keywords_1909 =", keywords_1909)
        keywords_1908 = ana.extract_tags(sentence=corpus_1908, topK=30, allowPOS=('ns', 'n', 'nr'), withWeight=True)
        print("keywords_1908 =", keywords_1908)

        lst = [keywords_1908, keywords_1909, keywords_1910, keywords_1911, keywords_1912]
        name = 8
        for l in lst:
            x_list = []
            y_list = []
            print(l)
            for i in l:
                print(i[0])
                x_list.append(i[0])
                y_list.append(i[1])
            plt.title('热门词&TF_IDF', fontsize=18)
            plt.xlabel('热门词', fontsize=12)
            plt.ylabel('TF_IDF', fontsize=12)
            # for y in y_list:
            #     print(type(y))
            plt.bar(range(len(y_list)), y_list, color='rgb', tick_label=x_list)
            plt.xticks(rotation=45)
            plt.show()
