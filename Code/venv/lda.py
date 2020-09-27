import csv
import jieba
import jieba.analyse as ana
import jieba.posseg as psg
from datetime import datetime
from gensim import corpora, models
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


stopwords = []
f = open('stopwords.txt')
for line in f:
    if line != '':
        stopwords.append(line.strip())

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
            corpus_1912 = corpus_1912 + sentence + "|"
        elif comTime('2019/11/1', '2019/11/30', row[1]):
            sentence = (row[0] + row[3]).replace('&nbsp;', '')
            corpus_1911 = corpus_1911 + sentence + "|"
        elif comTime('2019/10/1', '2019/10/31', row[1]):
            sentence = (row[0] + row[3]).replace('&nbsp;', '')
            corpus_1910 = corpus_1910 + sentence + "|"
        elif comTime('2019/9/1', '2019/9/30', row[1]):
            sentence = (row[0] + row[3]).replace('&nbsp;', '')
            corpus_1909 = corpus_1909 + sentence + "|"
        elif comTime('2019/8/1', '2019/8/31', row[1]):
            sentence = (row[0] + row[3]).replace('&nbsp;', '')
            corpus_1908 = corpus_1908 + sentence + "|"


def draw(x_lst, y_lst):
    plt.title('热门词', fontsize=18)
    plt.xlabel('热门词', fontsize=12)
    plt.ylabel('LDA', fontsize=12)
    plt.bar(range(len(y_lst)), y_lst, color='rgb', tick_label=x_lst)
    plt.xticks(rotation=45)
    plt.show()


# lda
flags = ['n', 'nr', 'ns']
# 1908
# corpus_1908 = corpus_1908.split('|')
# for c in corpus_1908:
#     if c == '':
#         corpus_1908.remove(c)
# ana.set_stop_words('stopwords.txt')
# words = []
# for sentence in corpus_1908:
#     word = [w.word for w in psg.cut(sentence) if w.flag in flags and w.word not in stopwords]
#     words.append(word)
# dictionary = corpora.Dictionary(words)
# corpus = [dictionary.doc2bow(ws) for ws in words]
# lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1)
# print("201908")
# x_lst_8 = []
# y_lst_8 = []
# for topic in lda.print_topics(num_words=30):
#     res = topic[1]
#     res = res.split('+')
#     for r in res:
#         r2 = eval(r.split('*')[1])
#         r1 = r.split('*')[0]
#         # print(r1, r2)
#         x_lst_8.append(r2)
#         y_lst_8.append(float(r1.strip()))
# print(len(x_lst_8), x_lst_8)
# print(len(y_lst_8), y_lst_8)
# draw(x_lst_8, y_lst_8)
# 1909
# corpus_1909 = corpus_1909.split('|')
# for c in corpus_1909:
#     if c == '':
#         corpus_1909.remove(c)
# ana.set_stop_words('stopwords.txt')
# words = []
# for sentence in corpus_1909:
#     word = [w.word for w in psg.cut(sentence) if w.flag in flags and w.word not in stopwords]
#     words.append(word)
# dictionary = corpora.Dictionary(words)
# corpus = [dictionary.doc2bow(ws) for ws in words]
# lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1)
# print("201909")
# x_lst_9 = []
# y_lst_9 = []
# for topic in lda.print_topics(num_words=30):
#     res = topic[1]
#     res = res.split('+')
#     for r in res:
#         r2 = eval(r.split('*')[1])
#         r1 = r.split('*')[0]
#         # print(r1, r2)
#         x_lst_9.append(r2)
#         y_lst_9.append(float(r1.strip()))
# print(len(x_lst_9), x_lst_9)
# print(len(y_lst_9), y_lst_9)
# draw(x_lst_9, y_lst_9)
# 1910
corpus_1910 = corpus_1910.split('|')
for c in corpus_1910:
    if c == '':
        corpus_1910.remove(c)
ana.set_stop_words('stopwords.txt')
words = []
for sentence in corpus_1910:
    word = [w.word for w in psg.cut(sentence) if w.flag in flags and w.word not in stopwords]
    words.append(word)
dictionary = corpora.Dictionary(words)
corpus = [dictionary.doc2bow(ws) for ws in words]
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1)
print("201910")
x_lst_10 = []
y_lst_10 = []
for topic in lda.print_topics(num_words=30):
    res = topic[1]
    res = res.split('+')
    for r in res:
        r2 = eval(r.split('*')[1])
        r1 = r.split('*')[0]
        # print(r1, r2)
        x_lst_10.append(r2)
        y_lst_10.append(float(r1.strip()))
print(len(x_lst_10), x_lst_10)
print(len(y_lst_10), y_lst_10)
draw(x_lst_10, y_lst_10)
# 1911
# corpus_1911 = corpus_1911.split('|')
# for c in corpus_1911:
#     if c == '':
#         corpus_1911.remove(c)
# ana.set_stop_words('stopwords.txt')
# words = []
# for sentence in corpus_1911:
#     word = [w.word for w in psg.cut(sentence) if w.flag in flags and w.word not in stopwords]
#     words.append(word)
# dictionary = corpora.Dictionary(words)
# corpus = [dictionary.doc2bow(ws) for ws in words]
# lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1)
# print("201911")
# x_lst_11 = []
# y_lst_11 = []
# for topic in lda.print_topics(num_words=30):
#     res = topic[1]
#     res = res.split('+')
#     for r in res:
#         r2 = eval(r.split('*')[1])
#         r1 = r.split('*')[0]
#         # print(r1, r2)
#         x_lst_11.append(r2)
#         y_lst_11.append(float(r1.strip()))
# print(len(x_lst_11), x_lst_11)
# print(len(y_lst_11), y_lst_11)
# draw(x_lst_11, y_lst_11)
# 1912
# corpus_1912 = corpus_1912.split('|')
# for c in corpus_1912:
#     if c == '':
#         corpus_1912.remove(c)
# ana.set_stop_words('stopwords.txt')
# words = []
# for sentence in corpus_1912:
#     word = [w.word for w in psg.cut(sentence) if w.flag in flags and w.word not in stopwords]
#     words.append(word)
# dictionary = corpora.Dictionary(words)
# corpus = [dictionary.doc2bow(ws) for ws in words]
# lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=1)
# print("201912")
# x_lst_12 = []
# y_lst_12 = []
# for topic in lda.print_topics(num_words=30):
#     res = topic[1]
#     res = res.split('+')
#     for r in res:
#         r2 = eval(r.split('*')[1])
#         r1 = r.split('*')[0]
#         # print(r1, r2)
#         x_lst_12.append(r2)
#         y_lst_12.append(float(r1.strip()))
# print(len(x_lst_12), x_lst_12)
# print(len(y_lst_12), y_lst_12)
# draw(x_lst_12, y_lst_12)
