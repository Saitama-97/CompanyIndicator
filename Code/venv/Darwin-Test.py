import numpy as np


# 定义tanh函数
def tanh(x):
    return np.tanh(x)


# tanh函数的导数
def tan_deriv(x):
    return 1.0 - np.tanh(x) * np.tan(x)


# sigmoid函数
def logistic(x):
    return 1 / (1 + np.exp(-x))


# sigmoid函数的导数
def logistic_derivative(x):
    return logistic(x) * (1 - logistic(x))


class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        """
        神经网络算法构造函数
        :param layers: 神经元层数
        :param activation: 使用的函数（默认tanh函数）
        :return:none
        """
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tan_deriv

        # 权重列表
        self.weights = []

        # 初始化权重（随机）
        for i in range(1, len(layers) - 1):
            self.weights.append((2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1) * 0.25)
            self.weights.append((2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1) * 0.25)

    def fit(self, X, y, learning_rate=0.2, epochs=10000):
        """
        训练神经网络
        :param X: 数据集（通常是二维）
        :param y: 分类标记
        :param learning_rate: 学习率（默认0.2）
        :param epochs: 训练次数（最大循环次数，默认10000）
        :return: none
        """
        # 确保数据集是二维的
        X = np.atleast_2d(X)

        temp = np.ones([X.shape[0], X.shape[1] + 1])
        temp[:, 0: -1] = X
        X = temp
        y = np.array(y)

        for k in range(epochs):
            # 随机抽取X的一行
            i = np.random.randint(X.shape[0])
            # 用随机抽取的这一组数据对神经网络更新
            a = [X[i]]
            # 正向更新
            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            error = y[i] - a[-1]
            deltas = [error * self.activation_deriv(a[-1])]

            # 反向更新
            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T) * self.activation_deriv(a[l]))
                deltas.reverse()
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


def Merge(A, B):
    for k, v in B.items():
        A[k] = A.get(k, 0) + v
    return A


def score(mydict1, mydict2):
    print('获取当月数据...')
    print('计算权重...')
    mydict1_copy = mydict1.copy()
    mydict = Merge(mydict1_copy, mydict2)
    scoreDict = {}
    total = 0
    for i in mydict.values():
        total += i

    try:
        one = mydict[1] / total
        scoreDict['1'] = one
    except:
        pass

    try:
        two = mydict[2] / total
        scoreDict['2'] = two
    except:
        pass

    try:
        three = mydict[3] / total
        scoreDict['3'] = three
    except:
        pass

    try:
        four = mydict[4] / total
        scoreDict['4'] = four
    except:
        pass

    try:
        five = mydict[5] / total
        scoreDict['5'] = five
    except:
        pass

    try:
        six = mydict[6] / total
        scoreDict['6'] = six
    except:
        pass

    try:
        seven = mydict[7] / total
        scoreDict['7'] = seven
    except:
        pass

    try:
        eight = mydict[8] / total
        scoreDict['8'] = eight
    except:
        pass

    try:
        nine = mydict[9] / total
        scoreDict['9'] = nine
    except:
        pass

    try:
        ten = mydict[10] / total
        scoreDict['10'] = ten
    except:
        pass

    sum = 0
    lst = scoreDict.values()
    for i in lst:
        sum += i
    print('1:', scoreDict['1'])
    print('2:', scoreDict['2'])
    print('3:', scoreDict['3'])
    print('4:', scoreDict['4'])
    print('5:', scoreDict['5'])
    print('6:', scoreDict['6'])
    print('7:', scoreDict['7'])
    print('8:', scoreDict['8'])
    print('9:', scoreDict['9'])
    print('10:', scoreDict['10'])


if __name__ == '__main__':
    # nn = NeuralNetwork([2, 2, 1], 'tanh')
    # temp = [[0, 0], [0, 1], [1, 0], [2, 3]]
    # X = np.array(temp)
    # y = np.array([0, 1, 1, 0])
    # nn.fit(X, y)
    # for i in temp:
    #     print(i, nn.predict(i))

    # score-1908
    dic1908_1 = {6: 236, 9: 88, 3: 25, 0: 9, 4: 6, 7: 4}
    dic1908_2 = {9: 207, 6: 110, 3: 19, 4: 10, 0: 9, 7: 9, 1: 4}
    dic1908 = Merge(dic1908_1.copy(), dic1908_2)
    # print('1908', dic1908)
    # score1908 = score(dic1908_1, dic1908_2)

    # score-1909
    dic1909_1 = {6: 246, 9: 111, 3: 15, 4: 12, 0: 9, 7: 3}
    dic1909_2 = {9: 212, 6: 128, 3: 24, 4: 10, 0: 9, 7: 7, 1: 6}
    dic1909 = Merge(dic1909_1.copy(), dic1909_2)
    # print('dic1909', dic1909)
    dic1909 = Merge(dic1908.copy(), dic1909)
    # print('New-dic1909', dic1909)
    # score1909 = score(dic1909_1, dic1909_2)

    # score-1910
    dic1910_1 = {6: 211, 9: 112, 3: 14, 4: 10, 7: 1, 0: 1}
    dic1910_2 = {9: 183, 6: 120, 3: 20, 4: 13, 7: 8, 1: 4, 0: 1}
    dic1910 = Merge(dic1910_1.copy(), dic1910_2)
    # print('dic1910', dic1910)
    dic1910 = Merge(dic1909.copy(), dic1910)
    # print('New-dic1910', dic1910)
    # score1910 = score(dic1910_1, dic1910_2)

    # score-1911
    dic1911_1 = {6: 272, 9: 126, 3: 11, 4: 7, 7: 5, 0: 2}
    dic1911_2 = {9: 243, 6: 139, 3: 13, 4: 13, 7: 9, 1: 4, 0: 2}
    dic1911 = Merge(dic1911_1.copy(), dic1911_2)
    # print('dic1911', dic1911)
    dic1911 = Merge(dic1910.copy(), dic1911)
    # print('New-dic1911', dic1911)
    # score1911 = score(dic1911_1, dic1911_2)

    # score-1912
    dic1912_1 = {6: 168, 9: 85, 3: 10, 4: 9, 0: 4, 7: 4}
    dic1912_2 = {9: 145, 6: 99, 3: 13, 1: 9, 4: 8, 0: 4, 7: 2}
    dic1912 = Merge(dic1912_1.copy(), dic1912_2)
    # print('dic1912', dic1912)
    dic1912 = Merge(dic1911.copy(), dic1912)
    # print('New-dic1912', dic1912)
    # score1912 = score(dic1912_1, dic1912_2)

    # train

    # score-1907
    dic1907_1 = {6: 264, 9: 130, 3: 24, 4: 6, 0: 5, 7: 1}
    dic1907_2 = {9: 221, 6: 140, 3: 33, 4: 16, 7: 8, 1: 7, 0: 5}
    # score1907 = score(dic1907_1, dic1907_2)

    # score-1906
    dic1906_1 = {6: 203, 9: 82, 3: 18, 4: 15, 0: 7, 7: 3}
    dic1906_2 = {9: 171, 6: 101, 3: 26, 4: 12, 7: 9, 0: 7, 1: 2}
    # score1906 = score(dic1906_1, dic1906_2)

    # score-1905
    dic1905_1 = {6: 202, 9: 101, 3: 18, 4: 18, 0: 7, 7: 3}
    dic1905_2 = {9: 182, 6: 128, 4: 16, 3: 8, 0: 7, 1: 4, 7: 4}
    # score1905 = score(dic1905_1, dic1905_2)

    # score-1904
    dic1904_1 = {6: 210, 9: 82, 3: 33, 4: 10, 0: 6, 7: 1}
    dic1904_2 = {9: 174, 6: 98, 3: 29, 4: 23, 7: 7, 0: 6, 1: 5}
    # score1904 = score(dic1904_1, dic1904_2)

    # score-1903
    dic1903_1 = {6: 118, 9: 56, 3: 6, 4: 4, 7: 2, 0: 1}
    dic1903_2 = {9: 100, 6: 61, 4: 12, 3: 12, 0: 1, 7: 1}
    # score1903 = score(dic1903_1, dic1903_2)

    # score-1902
    dic1902_1 = {6: 79, 9: 57, 4: 8, 3: 6, 0: 4}
    dic1902_2 = {9: 69, 6: 64, 3: 8, 4: 6, 0: 4, 7: 3}
    # score1902 = score(dic1902_1, dic1902_2)

    # score-1901
    dic1901_1 = {6: 120, 9: 43, 3: 6, 0: 1}
    dic1901_2 = {9: 109, 6: 44, 3: 7, 7: 4, 4: 4, 1: 1, 0: 1}
    # score1901 = score(dic1901_1, dic1901_2)

    # score-1812
    dic1812_1 = {6: 120, 9: 62, 3: 7, 7: 5, 4: 2, 0: 2}
    dic1812_2 = {9: 106, 6: 67, 3: 11, 7: 7, 4: 3, 1: 2, 0: 2}
    # score1812 = score(dic1812_1, dic1812_2)

    # score-1811
    dic1811_1 = {6: 145, 9: 66, 3: 5, 4: 3, 0: 2}
    dic1811_2 = {9: 132, 6: 68, 3: 10, 7: 5, 4: 3, 0: 2, 1: 1}
    # score1811 = score(dic1811_1, dic1811_2)

    # score-1810
    dic1810_1 = {6: 107, 9: 42, 3: 5, 0: 2, 4: 1}
    dic1810_2 = {9: 99, 6: 42, 3: 5, 7: 4, 4: 4, 0: 2, 1: 1}
    # score1810 = score(dic1810_1, dic1810_2)

    # score-1809
    dic1809_1 = {6: 158, 9: 77, 3: 10, 7: 7, 0: 5, 4: 2}
    dic1809_2 = {9: 148, 6: 87, 7: 8, 3: 7, 0: 5, 4: 3, 1: 1}
    # score1809 = score(dic1809_1, dic1809_2)

    # score-1808
    dic1808_1 = {6: 197, 9: 69, 3: 14, 4: 8, 0: 7}
    dic1808_2 = {9: 168, 6: 81, 3: 17, 4: 13, 7: 7, 0: 7, 1: 2}
    # score1808 = score(dic1808_1, dic1808_2)

    # score-1807
    dic1807_1 = {6: 89, 9: 34, 3: 9, 4: 4, 7: 1, 0: 1}
    dic1807_2 = {9: 80, 6: 42, 3: 8, 4: 3, 7: 2, 1: 2, 0: 1}
    # score1807 = score(dic1807_1, dic1807_2)

    dic_1 = {6: 2012, 9: 901, 3: 161, 4: 281, 10: 50, 7: 23, 5: 300}
    dic_2 = {9: 1759, 6: 900, 3: 181, 4: 118, 7: 69, 10: 50, 1: 228, 2: 200, 8: 300}
    train = Merge(dic_1.copy(), dic_2)
    # print('train',train)
    # score()

    dct = {1: '经济', 2: '文化', 3: '社会', 4: '生态', 5: '科技', 6: '依法', 7: '廉洁', 8: '组织', 9: '思想', 10: '作风'}
    print(dct)
    month = input("请输入月份(例-201908): ").strip()

    if month == '201908':
        score(train, dic1908)
    elif month == '201909':
        score(train, dic1909)
    elif month == '201910':
        score(train, dic1910)
    elif month == '201911':
        score(train, dic1911)
    elif month == '201912':
        score(train, dic1912)
