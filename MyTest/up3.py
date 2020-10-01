h, w = map(int, input().split())

board = []
for i in range(h):
    j = input()
    board.append(j)
print(board)

for i in board:
    ch = i.find('#')
    print(ch)