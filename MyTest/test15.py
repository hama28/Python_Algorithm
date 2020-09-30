# 鬼(スタート地点、速度)
a, v = map(int, input().split())
# 逃走(スタート地点、速度)
b, w = map(int, input().split())
# 追いかける時間
t = int(input())

# 鬼が追いつくかどうか
if a < b:
    if (a+v*t) >= (b+w*t):
        print("YES")
    else:
        print("NO")
else:
    if (a-v*t) <= (b-w*t):
        print("YES")
    else:
        print("NO")