from numpy import *
import csv
import numpy as np
import random
import jieba
import jieba.analyse as ana
import jieba.posseg as psg
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib.font_manager import _rebuild

_rebuild()

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams["axes.unicode_minus"] = False


def createDataset():
    with open('new-dict.csv', encoding='utf-8') as f:
        next(f)
        csv_file = csv.reader(f)
        lst = []
        lst_1 = []
        lst_2 = []
        lst_3 = []
        lst_4 = []
        lst_5 = []
        lst_6 = []
        lst_7 = []
        lst_8 = []
        lst_9 = []
        lst_10 = []
        for row in csv_file:
            l = row[1].split(',')
            for item in l:
                if item == '1':
                    lst_1.append(row[0])
                elif item == '2':
                    lst_2.append(row[0])
                elif item == '3':
                    lst_3.append(row[0])
                elif item == '4':
                    lst_4.append(row[0])
                elif item == '5':
                    lst_5.append(row[0])
                elif item == '6':
                    lst_6.append(row[0])
                elif item == '7':
                    lst_7.append(row[0])
                elif item == '8':
                    lst_8.append(row[0])
                elif item == '9':
                    lst_9.append(row[0])
                elif item == '10':
                    lst_10.append(row[0])
        ls = [lst_1, lst_2, lst_3, lst_4, lst_5, lst_6, lst_7, lst_8, lst_9, lst_10]
        for l in ls:
            lst.append(l)
        return lst


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            pass
    return returnVec


def bagOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
        return returnVec


def countX(aList, el):
    count = 0
    for item in aList:
        if item == el:
            count += 1
    return count


def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive1 = countX(trainCategory, 1) / float(numTrainDocs)
    pAbusive2 = countX(trainCategory, 2) / float(numTrainDocs)
    pAbusive3 = countX(trainCategory, 3) / float(numTrainDocs)
    pAbusive4 = countX(trainCategory, 4) / float(numTrainDocs)
    pAbusive5 = countX(trainCategory, 5) / float(numTrainDocs)
    pAbusive6 = countX(trainCategory, 6) / float(numTrainDocs)
    pAbusive7 = countX(trainCategory, 7) / float(numTrainDocs)
    pAbusive8 = countX(trainCategory, 8) / float(numTrainDocs)
    pAbusive9 = countX(trainCategory, 9) / float(numTrainDocs)
    pAbusive10 = countX(trainCategory, 10) / float(numTrainDocs)
    p1Num = np.ones(numWords)
    p2Num = np.ones(numWords)
    p3Num = np.ones(numWords)
    p4Num = np.ones(numWords)
    p5Num = np.ones(numWords)
    p6Num = np.ones(numWords)
    p7Num = np.ones(numWords)
    p8Num = np.ones(numWords)
    p9Num = np.ones(numWords)
    p10Num = np.ones(numWords)
    p1Denom = 2.0
    p2Denom = 2.0
    p3Denom = 2.0
    p4Denom = 2.0
    p5Denom = 2.0
    p6Denom = 2.0
    p7Denom = 2.0
    p8Denom = 2.0
    p9Denom = 2.0
    p10Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 2:
            p2Num += trainMatrix[i]
            p2Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 3:
            p3Num += trainMatrix[i]
            p3Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 4:
            p4Num += trainMatrix[i]
            p4Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 5:
            p5Num += trainMatrix[i]
            p5Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 6:
            p6Num += trainMatrix[i]
            p6Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 7:
            p7Num += trainMatrix[i]
            p7Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 8:
            p8Num += trainMatrix[i]
            p8Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 9:
            p9Num += trainMatrix[i]
            p9Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 10:
            p10Num += trainMatrix[i]
            p10Denom += sum(trainMatrix[i])
    p10Vect = np.log(p10Num / p10Denom)
    p9Vect = np.log(p9Num / p9Denom)
    p8Vect = np.log(p8Num / p8Denom)
    p7Vect = np.log(p7Num / p7Denom)
    p6Vect = np.log(p6Num / p6Denom)
    p5Vect = np.log(p5Num / p5Denom)
    p4Vect = np.log(p4Num / p4Denom)
    p3Vect = np.log(p3Num / p3Denom)
    p2Vect = np.log(p2Num / p2Denom)
    p1Vect = np.log(p1Num / p1Denom)
    return p1Vect, p2Vect, p3Vect, p4Vect, p5Vect, p6Vect, p7Vect, p8Vect, p9Vect, p10Vect, pAbusive1, \
           pAbusive2, pAbusive3, pAbusive4, pAbusive5, pAbusive6, pAbusive7, pAbusive8, pAbusive9, pAbusive10


def classifyNB(vec2Classify, p1Vec, p2Vec, p3Vec, p4Vec, p5Vec, p6Vec, p7Vec, p8Vec, p9Vec, p10Vec, pClass1,
               pClass2, pClass3, pClass4, pClass5, pClass6,
               pClass7, pClass8, pClass9, pClass10):
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
    p2 = sum(vec2Classify * p2Vec) + np.log(pClass2)
    p3 = sum(vec2Classify * p3Vec) + np.log(pClass3)
    p4 = sum(vec2Classify * p4Vec) + np.log(pClass4)
    p5 = sum(vec2Classify * p5Vec) + np.log(pClass5)
    p6 = sum(vec2Classify * p6Vec) + np.log(pClass6)
    p7 = sum(vec2Classify * p7Vec) + np.log(pClass7)
    p8 = sum(vec2Classify * p8Vec) + np.log(pClass8)
    p9 = sum(vec2Classify * p9Vec) + np.log(pClass9)
    p10 = sum(vec2Classify * p10Vec) + np.log(pClass10)
    dct = {1: p1, 2: p2, 3: p3, 4: p4, 5: p5, 6: p6, 7: p7, 8: p8, 9: p9, 10: p10}
    ts = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10].index(ts[0][1]), [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10].index(
        ts[1][1])


def printMessage(i, j):
    dct = {1: '经济', 2: '文化', 3: '社会', 4: '生态', 5: '科技', 6: '依法', 7: '廉洁', 8: '组织', 9: '思想', 10: '作风'}
    print('主要类别 =', dct[i])
    print('次要类别 =', dct[j])


def getTfWord():
    try:
        with open('news.csv', newline='', encoding='utf-8') as csvfile:
            # r = random.randint(0, 5052)
            next(csvfile)
            reader = csv.reader(csvfile)
            for i, rows in enumerate(reader):
                if i == 169:
                    row = rows
            sent = (row[0] + row[3]).replace('&nbsp;', '')
            print(sent)
            ana.set_stop_words('stopwords.txt')
            keyword = ana.extract_tags(sentence=sent, topK=10, allowPOS=('ns', 'n', 'nr'))
            print(row[0], keyword)
            return keyword
    except:
        pass
    finally:
        keyword2 = ana.extract_tags(sentence=sent, topK=50, allowPOS=('ns', 'n', 'nr'), withWeight=True)
        wordCloud(keyword2)


def wordCloud(keyword2):
    print(keyword2)
    new_keyword = {}
    for i, j in enumerate(keyword2):
        # print(j[0], j[1])
        new_keyword[j[0]] = j[1]

    def show_img(wc):
        plt.figure()
        plt.imshow(wc)
        plt.axis("off")

    wc = WordCloud(
        font_path='/Users/Saitama/PycharmProjects/Project-1/venv/simsun.ttc',
        max_words=2000,
        width=1920,
        height=1080,
        background_color="white",
        margin=5)
    wc.generate_from_frequencies(new_keyword)

    wc.to_file('wc.png')
    show_img(wc)


if __name__ == '__main__':
    dataset = createDataset()
    classVec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    myVocabList = createVocabList(dataset)
    trainMat = []
    for postinDoc in dataset:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p1V, p2V, p3V, p4V, p5V, p6V, p7V, p8V, p9V, p10V, pAb1, pAb2, pAb3, pAb4, pAb5, pAb6, pAb7, pAb8, pAb9, pAb10 = trainNB0(
        array(trainMat), array(classVec))
    tst = getTfWord()
    thisDoc = array(setOfWords2Vec(myVocabList, tst))
    flag1, flag2 = classifyNB(thisDoc, p1V, p2V, p3V, p4V, p5V, p6V, p7V, p8V, p9V, p10V, pAb1, pAb2, pAb3, pAb4, pAb5,
                              pAb6, pAb7, pAb8, pAb9, pAb10)
    # flag1 = 3
    # flag2 = 1
    printMessage(flag1, flag2)
