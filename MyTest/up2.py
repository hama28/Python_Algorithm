h, w, n = map(int, input().split())

ma = []
for i in range(h):
    j = input()
    ma.append(j)

for i in range(n):
    j,k = map(int, input().split())
    word = ma[j]
    word = word[:k] + '#' + word[k:]
    ma[j] = word

for i in ma:
    print(i)