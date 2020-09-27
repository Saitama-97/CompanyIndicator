import csv

set1 = set()
set2 = set()

f1 = open('dict.csv', 'r', encoding='utf-8')
next(f1)
csv_reader1 = csv.reader(f1)
for c in csv_reader1:
    set1.add(c[0])

f2 = open('new-dict.csv', 'r', encoding='utf-8')
next(f2)
csv_reader2 = csv.reader(f2)
for c in csv_reader2:
    set2.add(c[0])

print(len(set1))
print(len(set2))

print(len(set1.intersection(set2)))
print(len(set1.union(set2)))

# lst1 = [1, 3, 5]
# lst2 = [2, 4, 5, 6]
# set1 = {1, 3, 5}
# set2 = {2, 4, 5, 6}
# print(set1.union(set2))
# print(set1.intersection(set2))
