# 例１
# フレーム数、ピン数、投げた数
# 10 10 18
# [3 4] [G 1] [8 2] [6 2] [10] [2 7] [G 10] [10] [10] [9 1 3]
# 145

# 例２
# 15 5 24
# [5] [5] [5] [4 G] [1 G] [5] [3 2] [1 4] [4 G] [G 1] [5] [5] [5] [2 1] [5 3 1]
# 124


a = input()
a = a.split()
a = list(map(int, a))

b = input()
b = b.replace('G','0')
b = b.split()
b = list(map(int, b))


# 分かりやすいリストに入れ直す
c = []
i = 0
while i < (len(b)-1):
    # 最終フレームかチェック
    if len(c) == (a[0]-1):
        # 最終フレームでスペアなら3投目を追加
        if (b[i] + b[i+1]) >= a[1]:
            d = [b[i], b[i+1], b[i+2]]
            c.append(d)
            break
    # ストライクなら2投目に0を入れる
    elif b[i] == a[1]:
        d = [b[i], 0]
        c.append(d)
        i+=1
    else:
        d = [b[i], b[i+1]]
        c.append(d)
        i+=2

#print(c)


# 得点計算
i = 0
point = 0
while i < len(c):
    # 最終フレームでスペアかストライクなら3投目を加算
    if i == (len(c)-1):
        if c[i][0] == a[1]:
            point += c[i][0] + (c[i][1] * 2) + (c[i][2] * 2)
            break
        elif (c[i][0] + c[i][1]) == a[1]:
            point += (c[i][0] + c[i][1]) + (c[i][2] * 2)
            break
    # 最終フレーム手前
    elif i == (len(c)-2):
        # 2連続ストライクなら次フレームの1投目を加算
        if c[i][0] == a[1] and c[i+1][0] == a[1]:
            point += sum(c[i]) + c[i+1][0] + c[i+1][1]
            i+=1
        # ストライクなら次のフレームを加算
        elif c[i][0] == a[1]:
            point += sum(c[i]) + c[i+1][0] + c[i+1][1]
            i+=1
        # スペアなら次の1投目を加算
        elif sum(c[i]) == a[1]:
            point += sum(c[i]) + c[i+1][0]
            i+=1
        else:
            point += sum(c[i])
            i+=1
    # 最終フレームでない場合
    elif i != (len(c)-1):
        # 2連続ストライクなら次フレームの1投目を加算
        if c[i][0] == a[1] and c[i+1][0] == a[1]:
            point += sum(c[i]) + sum(c[i+1]) + c[i+2][0]
            i+=1
        # ストライクなら次のフレームを加算
        elif c[i][0] == a[1]:
            point += sum(c[i]) + c[i+1][0] + c[i+1][1]
            i+=1
        # スペアなら次の1投目を加算
        elif sum(c[i]) == a[1]:
            point += sum(c[i]) + c[i+1][0]
            i+=1
        else:
            point += sum(c[i])
            i+=1

print(point)