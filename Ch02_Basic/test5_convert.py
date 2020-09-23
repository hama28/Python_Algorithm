# 10進数 --> 2進数
n = int(input("10進数："))
reslut = ""

while n > 0:
    reslut = str(n % 2) + reslut
    n //= 2

print("2進数：" + reslut)


# 2進数 --> 10進数
n = input("2進数：")
reslut = 0

for i in range(len(n)):
    reslut += int(n[i]) * (2 ** (len(n) - i - 1))

print("10進数：" + str(reslut))


# 便利な関数
n = int(input())
print(bin(n))

n = input()
print(int(n,2))

n = 0b1111
print(n)