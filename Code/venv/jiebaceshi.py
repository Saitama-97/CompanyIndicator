import jieba
import jieba.analyse as ana
import jieba.posseg as psg
import gensim.corpora.dictionary as dict
import gensim.models as mod

# 语料
corpus = "《知否知否应是绿肥红瘦》是由东阳正午阳光影视有限公司出品，侯鸿亮担任制片人，张开宙执导，曾璐、吴桐编剧，赵丽颖、冯绍峰领衔主演，" \
         "朱一龙、施诗、张佳宁、曹翠芬、刘钧、刘琳、高露、王仁君、李依晓、王鹤润、张晓谦、李洪涛主演，王一楠、陈瑾特别出演的古代社会家庭题材电视剧"

# textrank
keywords_textrank = ana.textrank(corpus)
print("textrank =", keywords_textrank)

# tf-idf
keywords_tfidf = ana.tfidf(corpus)
print("tfidf =", keywords_tfidf)

# lda
corpus_lda = [
    '北京市气象台今晨发布1时至9时降水量',
    '降雪期间地面湿滑，能见度下降',
    '演员翟天临的博士学位及相关论文被网友质疑',
    '质疑翟天临“学术造假问题”']
jieba.add_word('博士', 9, 'n')
flags = ('n', 'nr', 'ns')
stopwords = ('时', '是', '的', '被')
words = []
for sentence in corpus_lda:
    word = [w for w in psg.cut(sentence) if w.flag in flags and w.word not in stopwords]
    words.append(word)
print(words)