# a (+ or -) b = c どこか1つがx
a, op, b, eq, c = map(str, input().split())

if c == "x":
    if op == "+":
        print(int(a) + int(b))
    elif op == "-":
        print(int(a) - int(b))
elif b == "x":
    if op == "+":
        print(int(c) - int(a))
    elif op == "-":
        print(int(a) - int(c))
elif a == "x":
    if op == "+":
        print(int(c) - int(b))
    elif op == "-":
        print(int(b) + int(c))