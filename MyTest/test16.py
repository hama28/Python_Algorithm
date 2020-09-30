# 入力回数
q = int(input())
num = []

# 数値を格納
for i in range(q):
    j = int(input())
    num.append(abs(j))

# 入力された数値が完全数かチェック
def divisor(q): 
    i = 1
    table = []
    ans = 0
    while i * i <= q:
        if q%i == 0:
            table.append(i)
            table.append(q//i)
        i += 1
    table = list(set(table))
    for i in range(len(table)):
        if q != table[i]:
            ans += table[i]
    # 完全数
    if q == ans:
        print("perfect")
    # 完全数+1
    elif (q - ans) == 1:
        print("nearly")
    # それ以外
    else:
        print("neither")  
    return table

for i in range(q):
    divisor(num[i])