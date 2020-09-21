memo = {1: 1, 2: 1}
def fibonacci(n):
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return memo[n]

print(fibonacci(6))

a = 1
b = 1
print(a)
print(b)
a = a + b
print(a)

while a < 10000:
    x = a
    a = a + b
    print(a)
    b = a
    a = a + x
    print(a)
