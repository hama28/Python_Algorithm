n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)


for i in range(n):
    if words[i][-1] == 's' or words[i][-2:] == 'sh' or words[i][-2:] == 'ch' or words[i][-1] == 'o' or words[i][-1] == 'x':
        print(words[i] + 'es')
    elif words[i][-1] == 'f':
        print(words[i][:-1] + 'ves')
    elif words[i][-2:] == 'fe':
        print(words[i][:-2] + 'ves')
    elif words[i][-1] == 'y':
        if words[i][-2] != 'a' and words[i][-2] != 'i' and words[i][-2] != 'u' and words[i][-2] != 'e' and words[i][-2] != 'o':
            print(words[i][:-1] + 'ies')
        else:
            print(words[i] + 's')
    else:
        print(words[i] + 's')