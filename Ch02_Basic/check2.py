def seireki(n):
    if n < 1912:
        print("明治" + str(n - 1867) + "年")
    elif n < 1926:
        print("大正" + str(n - 1911) + "年")
    elif n < 1989:
        print("昭和" + str(n - 1925) + "年")
    elif n < 2019:
        print("平成" + str(n - 1988) + "年")
    else:
        print("令和" + str(n - 2018) + "年")

n = int(input())
seireki(n)