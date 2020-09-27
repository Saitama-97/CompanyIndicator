import csv
import wordcloud
import jieba
import jieba.analyse as ana
import jieba.posseg as psg
import cv2
from datetime import datetime
import pandas


# import matplotlib.pyplot as plt
# from matplotlib.pyplot import MultipleLocator
# from matplotlib.font_manager import _rebuild

# _rebuild()

# plt.rcParams['font.sans-serif'] = [u'SimHei']
# plt.rcParams["axes.unicode_minus"] = False


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
        corpus_1907 = ''
        corpus_1906 = ''
        corpus_1905 = ''
        corpus_1904 = ''
        corpus_1903 = ''
        corpus_1902 = ''
        corpus_1901 = ''
        corpus_1812 = ''
        corpus_1811 = ''
        corpus_1810 = ''
        corpus_1809 = ''
        corpus_1808 = ''
        corpus_1807 = ''

        # def extractag(a):
        #     print(a)
        #     lst = ana.extract_tags(sentence=a, topK=100, allowPOS=('ns', 'n', 'nr'))
        #     print(len(lst), lst)
        #     for l in lst:
        #         dic_set.add(l)

        for row in rows:
            if comTime('2019/12/1', '2019/12/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1912 += sentence
                # extractag(corpus_1912)
            elif comTime('2019/11/1', '2019/11/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1911 += sentence
                # extractag(corpus_1911)
            elif comTime('2019/10/1', '2019/10/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1910 += sentence
                # extractag(corpus_1910)
            elif comTime('2019/9/1', '2019/9/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1909 += sentence
                # extractag(corpus_1909)
            elif comTime('2019/8/1', '2019/8/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1908 += sentence
                # extractag(corpus_1908)
            elif comTime('2019/7/1', '2019/7/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1907 += sentence
                # extractag(corpus_1907)
            elif comTime('2019/6/1', '2019/6/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1906 += sentence
                # extractag(corpus_1906)
            elif comTime('2019/5/1', '2019/5/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1905 += sentence
                # extractag(corpus_1905)
            elif comTime('2019/4/1', '2019/4/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1904 += sentence
                # extractag(corpus_1904)
            elif comTime('2019/3/1', '2019/3/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1903 += sentence
                # extractag(corpus_1903)
            elif comTime('2019/2/1', '2019/2/28', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1902 += sentence
                # extractag(corpus_1902)
            elif comTime('2019/1/1', '2019/1/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1901 += sentence
                # extractag(corpus_1901)
            elif comTime('2018/12/1', '2018/12/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1812 += sentence
                # extractag(corpus_1812)
            elif comTime('2018/11/1', '2018/11/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1811 += sentence
                # extractag(corpus_1811)
            elif comTime('2018/10/1', '2018/10/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1810 += sentence
                # extractag(corpus_1810)
            elif comTime('2018/9/1', '2018/9/30', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1809 += sentence
                # extractag(corpus_1809)
            elif comTime('2018/8/1', '2018/8/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1808 += sentence
                # extractag(corpus_1808)
            elif comTime('2018/7/1', '2019/7/31', row[1]):
                sentence = (row[0] + row[3]).replace('&nbsp;', '')
                corpus_1807 += sentence
                # extractag(corpus_1807)

        dic_set = set()
        ana.set_stop_words('stopwords.txt')

        keywords_1912 = ana.extract_tags(sentence=corpus_1912, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1912), keywords_1912)
        for i in keywords_1912:
            dic_set.add(i)

        keywords_1911 = ana.extract_tags(sentence=corpus_1911, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1911), keywords_1911)
        for i in keywords_1911:
            dic_set.add(i)

        keywords_1910 = ana.extract_tags(sentence=corpus_1910, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1910), keywords_1910)
        for i in keywords_1910:
            dic_set.add(i)

        keywords_1909 = ana.extract_tags(sentence=corpus_1909, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1909), keywords_1909)
        for i in keywords_1909:
            dic_set.add(i)

        keywords_1908 = ana.extract_tags(sentence=corpus_1908, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1908), keywords_1908)
        for i in keywords_1908:
            dic_set.add(i)

        keywords_1907 = ana.extract_tags(sentence=corpus_1907, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1907), keywords_1907)
        for i in keywords_1907:
            dic_set.add(i)

        keywords_1906 = ana.extract_tags(sentence=corpus_1906, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1906), keywords_1906)
        for i in keywords_1906:
            dic_set.add(i)

        keywords_1905 = ana.extract_tags(sentence=corpus_1905, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1905), keywords_1905)
        for i in keywords_1905:
            dic_set.add(i)

        keywords_1904 = ana.extract_tags(sentence=corpus_1904, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1904), keywords_1904)
        for i in keywords_1904:
            dic_set.add(i)

        keywords_1903 = ana.extract_tags(sentence=corpus_1903, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1903), keywords_1903)
        for i in keywords_1903:
            dic_set.add(i)

        keywords_1902 = ana.extract_tags(sentence=corpus_1902, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1902), keywords_1902)
        for i in keywords_1902:
            dic_set.add(i)

        keywords_1901 = ana.extract_tags(sentence=corpus_1901, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1901), keywords_1901)
        for i in keywords_1901:
            dic_set.add(i)

        keywords_1812 = ana.extract_tags(sentence=corpus_1812, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1812), keywords_1812)
        for i in keywords_1812:
            dic_set.add(i)

        keywords_1811 = ana.extract_tags(sentence=corpus_1811, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1811), keywords_1811)
        for i in keywords_1811:
            dic_set.add(i)

        keywords_1810 = ana.extract_tags(sentence=corpus_1810, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1810), keywords_1810)
        for i in keywords_1810:
            dic_set.add(i)

        keywords_1809 = ana.extract_tags(sentence=corpus_1809, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1809), keywords_1809)
        for i in keywords_1809:
            dic_set.add(i)

        keywords_1808 = ana.extract_tags(sentence=corpus_1808, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1808), keywords_1808)
        for i in keywords_1808:
            dic_set.add(i)

        keywords_1807= ana.extract_tags(sentence=corpus_1807, topK=100, allowPOS=('ns', 'n', 'nr'))
        print(len(keywords_1807), keywords_1807)
        for i in keywords_1807:
            dic_set.add(i)

        print(dic_set)
        print(len(dic_set))

        f = open('dict.csv', 'w', encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(['关键词', '类别'])
        for d in dic_set:
            csv_writer.writerow([d, ''])
        f.close()
        df = pandas.read_csv('dict.csv', encoding='utf_8')
        df.to_csv('dict.csv', encoding='utf_8_sig')
