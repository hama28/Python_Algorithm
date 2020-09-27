num1 = 0
num2 = 0
a = ''
b = ''
c = ''

count = int(input())

for i in range(count):
    x = input()
    j = x.split()
    if len(j) == 3:
        a = j[0]
        b = j[1]
        c = j[2]
    else:
        a = j[0]
        b = j[1]
    if a == 'SET':
        if b == '1':
            num1 = int(c)
        if b == '2':
            num2 = int(c)
    elif a == 'ADD':
        num2 = num1 + int(b)
    elif a == 'SUB':
        num2 = num1 - int(b)

print(str(num1) + ' ' + str(num2))