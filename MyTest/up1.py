h, w, n = map(int, input().split())

ma = []
for i in range(h):
    j = input()
    ma.append(j)

ans = []
for i in range(n):
    j,k = map(int, input().split())
    word = ma[j]
    ans.append(word[k])

for i in ans:
    print(i)