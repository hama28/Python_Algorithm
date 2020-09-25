#a b c   #配座駅へまで時間 a 分, 配座駅から儀野駅の乗車時間 b 分, 儀野駅から会社までの時間 c 分
#N       #配座駅から出る電車の本数を表す整数 N
#h_1 m_1 #1本目の電車の発車時刻 h_1 時 m_1 分
#h_2 m_2 #2本目の電車の発車時刻 h_2 時 m_2 分
#...
#h_N m_N #N本目の電車の発車時刻 h_N 時 m_N 分

import datetime
import numpy

a, b, c = map(int, input().split())
a = datetime.timedelta(0,0,0,0,a)
b = datetime.timedelta(0,0,0,0,b)
c = datetime.timedelta(0,0,0,0,c)

count = int(input())
train = []
for i in range(count):
    h, m =  map(int, input().split())
    tr = datetime.timedelta(0,0,0,0,m,h)
    train.append(tr)

limit = datetime.timedelta(0,0,0,0,59,8)

limit = limit - c

for i in range(len(train)):
    max_value = max(train)
    max_index = train.index(max_value)
    if limit < train[max_index]:
        del train[max_index]

print(train)

limit = limit - b

for i in range(len(train)):
    max_value = max(train)
    max_index = train.index(max_value)
    if limit < train[max_index]:
        del train[max_index]

print(train)

limit = limit - a

print(limit)
