# 人数
n = int(input())
man = input().split()

# 計算用
buy = []
for i in range(n):
    buy.append(0)

# 入力回数
m = int(input())
for i in range(m):
    # 名前、費用
    a, b = map(str,input().split())
    j = man.index(a)
    buy[j] += int(b)

# 費用順
for i in range(n):
    max_value = max(buy)
    max_index = buy.index(max_value)
    print(man[max_index])
    buy.pop(max_index)
    man.pop(max_index)