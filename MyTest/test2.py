import math,time

n = int(input("素数チェック："))

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 計算する範囲を絞る
    m = math.floor(math.sqrt(n)) + 1 # nの平方根まで
    for p in range(3, m, 2): # 奇数のみチェック
        if n % p == 0:
            return False
    return True

start_time = time.time()

if isPrime(n):
    print("素数です")
else:
    print("素数ではありません")

end_time = time.time() - start_time

print("実行時間：{}秒".format(end_time))