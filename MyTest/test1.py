num = int(input("入力された数値が素数かチェックします："))
check = True

for i in range(1,num-1):
    if not (i**num) % num == i:
        check = False

if check:
    print("素数です")
else:
    print("素数ではないようです")