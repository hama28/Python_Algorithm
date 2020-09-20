import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for i in range(200):
    if is_prime(i):
        print(i, end=" ")

# エラトステネスの篩
def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    # 奇数リスト
    data = [i + 1 for i in range(2,n,2)]
    while limit > data[0]:
        prime.append(data[0])
        # 割り切れない数だけ取り出す
        data = [j for j in data if j % data[0] != 0]
    return prime + data

print(get_prime(200))