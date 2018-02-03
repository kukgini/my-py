#!/usr/bin/python

chulsu = [90, 85, 70]
yonghee = [88, 79, 92]
yong = [100, 100, 100]
minsu = [90, 60, 70]

students = [chulsu, yonghee, yong, minsu]

print("==========[ OLD STYLE ]============")
for scores in students:
    total = 0
    for s in scores:
        total = total + s
    average = total / 3
    print(scores, total, average)

print("==========[ NEW STYLE ]============")
import operator
for scores in students:
    total = reduce(operator.add, scores)
    average = total / len(scores)
    print(scores, total, average)

