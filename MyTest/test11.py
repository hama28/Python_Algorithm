n = int(input())
h, w = map(int, input().split())

total = h * w
ans = total % n

print(ans)