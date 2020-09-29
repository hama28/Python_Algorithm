h, w, x = map(int, input().split())
text = ''

for i in range(h):
    text += input()

for i in range(0,len(text),x):
    print(text[i:(i+x)])