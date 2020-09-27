import csv
from datetime import datetime


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
    with open('news.csv', 'r', newline='', encoding='utf-8') as csvfile:
        lst1807 = []
        lst1808 = []
        lst1809 = []
        lst1810 = []
        lst1811 = []
        lst1812 = []
        lst1901 = []
        lst1902 = []
        lst1903 = []
        lst1904 = []
        lst1905 = []
        lst1906 = []
        lst1907 = []
        lst1908 = []
        lst1909 = []
        lst1910 = []
        lst1911 = []
        lst1912 = []

        next(csvfile)
        reader = csv.reader(csvfile)
        for rows in enumerate(reader):
            if comTime('2019/12/1', '2019/12/31', rows[1][1]):
                lst1912.append(rows[0])
            elif comTime('2019/11/1', '2019/11/30', rows[1][1]):
                lst1911.append(rows[0])
            elif comTime('2019/10/1', '2019/10/31', rows[1][1]):
                lst1910.append(rows[0])
            elif comTime('2019/9/1', '2019/9/30', rows[1][1]):
                lst1909.append(rows[0])
            elif comTime('2019/8/1', '2019/8/31', rows[1][1]):
                lst1908.append(rows[0])
            elif comTime('2019/7/1', '2019/7/31', rows[1][1]):
                lst1907.append(rows[0])
            elif comTime('2019/6/1', '2019/6/30', rows[1][1]):
                lst1906.append(rows[0])
            elif comTime('2019/5/1', '2019/5/31', rows[1][1]):
                lst1905.append(rows[0])
            elif comTime('2019/4/1', '2019/4/30', rows[1][1]):
                lst1904.append(rows[0])
            elif comTime('2019/3/1', '2019/3/30', rows[1][1]):
                lst1903.append(rows[0])
            elif comTime('2019/2/1', '2019/2/28', rows[1][1]):
                lst1902.append(rows[0])
            elif comTime('2019/1/1', '2019/1/31', rows[1][1]):
                lst1901.append(rows[0])
            elif comTime('2018/12/1', '2018/12/31', rows[1][1]):
                lst1812.append(rows[0])
            elif comTime('2018/11/1', '2018/11/30', rows[1][1]):
                lst1811.append(rows[0])
            elif comTime('2018/10/1', '2018/10/31', rows[1][1]):
                lst1810.append(rows[0])
            elif comTime('2018/9/1', '2018/9/30', rows[1][1]):
                lst1809.append(rows[0])
            elif comTime('2018/8/1', '2018/8/31', rows[1][1]):
                lst1808.append(rows[0])
            elif comTime('2018/7/1', '2018/7/31', rows[1][1]):
                lst1807.append(rows[0])

        print(lst1912)
        print(lst1911)
        print(lst1910)
        print(lst1909)
        print(lst1908)
        print(lst1907)
        print(lst1906)
        print(lst1905)
        print(lst1904)
        print(lst1903)
        print(lst1902)
        print(lst1901)
        print(lst1812)
        print(lst1811)
        print(lst1810)
        print(lst1809)
        print(lst1808)
        print(lst1807)
