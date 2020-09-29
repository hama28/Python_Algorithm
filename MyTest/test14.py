n, x = map(int, input().split())
num = []
bin_num = bin(x)

for i in range(n):
    j = int(input())
    num.append(j)

for i in range(n):
    j = num[i]
    print(bin_num[-j])
