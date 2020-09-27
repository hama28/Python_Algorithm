n, m = map(int, input().split())

fare = []
for i in range(m):
    j =  int(input())
    fare.append(j)

point = 0

for i in range(m):
    if point >= fare[i]:
        point = point - fare[i]
    else:
        point += fare[i]/10
        n = n - fare[i]
    print(n, end=' ')
    print('{:.0f}'.format(point))