# 人数、合格点
n, m = map(int, input().split())
man = []

for i in range(n):
    j, k = map(int, input().split())
    man.append([j,k])

for i in range(n):
    point = man[i][0] - (man[i][1] * 5)
    # 点がマイナスでも合格点が0なら合格
    if abs(point) >= m:
        print(i + 1)