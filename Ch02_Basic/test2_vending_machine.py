import sys

money = input("投入金額：")
if not money.isdecimal():
    print("整数を入力してください")
    sys.exit()

price = input("商品価格：")
if not money.isdecimal():
    print("整数を入力してください")
    sys.exit()

change = int(money) - int(price)

if change < 0:
    print("金額が不足しています")
    sys.exit()

coin = [5000,1000,500,100,50,10,5,1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ": " + str(r))