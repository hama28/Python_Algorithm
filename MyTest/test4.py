s = input()

print(s.translate(str.maketrans({'A': '4',
                                'E': '3',
                                'G': '6',
                                'I': '1',
                                'O': '0',
                                'S': '5',
                                'Z': '2'})))