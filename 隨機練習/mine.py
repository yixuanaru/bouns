import random
# 設定棋盤大小
size = 10
# 初始化棋盤
board = [[0 for x in range(size)] for y in range(size)]
# 產生10個隨機地雷位置
mines = [(random.randint(0, size - 1), random.randint(0, size - 1)) for _ in range(10)]
# 在棋盤上標示地雷位置
for mine in mines:
    board[mine[0]][mine[1]] = 'X'
# 輸出棋盤和地雷位置
for row in board:
    print(" ".join([str(cell) for cell in row]))

#print("\n地雷位置:")
#for mine in mines:
#    print(f"({mine[0]}, {mine[1]})")