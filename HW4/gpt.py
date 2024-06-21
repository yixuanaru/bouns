import random
import time

matrix = [[" " for _ in range(9)] for _ in range(9)]

def printboard():  # 輸出遊戲背景
    a = "    a  " + " b  " + " c  " + " d  " + " e  " + " f  " + " g  " + " h  " + " i"
    b = "  " + "+---" * 9 + "+"
    print(a)
    print(b)
    for i in range(9):
        print(i + 1, "", end="")
        for j in range(9):
            if j == 8:
                print("| %s |" % (matrix[i][j]))
                print(b)
                continue
            print("| %s " % (matrix[i][j]), end="")

mine = []

def mines():  # 設置地雷
    global mine
    while len(mine) < 10:
        m = [random.randint(0, 8), random.randint(0, 8)]
        if m != first_move and m not in mine:
            mine.append(m)

def find(i, j):
    count = 0
    if [i + 1, j + 1] in mine:
        count += 1
    if [i + 1, j] in mine:
        count += 1
    if [i, j + 1] in mine:
        count += 1
    if [i - 1, j - 1] in mine:
        count += 1
    if [i - 1, j] in mine:
        count += 1
    if [i, j - 1] in mine:
        count += 1
    if [i + 1, j - 1] in mine:
        count += 1
    if [i - 1, j + 1] in mine:
        count += 1
    return count

def dive(i, j):
    if i < 0 or i > 8 or j < 0 or j > 8:
        return
    if matrix[i][j] == "0":
        return
    count = find(i, j)
    if count != 0:
        matrix[i][j] = "%s" % (count)
        return
    else:  # 如果count=0 matrix[i][j]顯示0
        matrix[i][j] = "0"
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dive(i + dx, j + dy)
    return count

def flag(i, j):
    if matrix[i][j] == " ":
        matrix[i][j] = "F"
        if [i, j] in mine:
            flen -= 1
        return
    if matrix[i][j] == "F":
        if [i, j] in mine:
            flen += 1
        matrix[i][j] = " "
        return
    print("Cannot put a flag there")

def loser():
    for i in mine:
        matrix[i[0]][i[1]] = 'X'  # 顯示所有地雷位置
    print("\n游戲結束\n")
    time.sleep(1)  # 暫停1秒,給玩家看結果
    printboard()
    again()

def again():
    a = input("Play again?(y/n): ")
    if a == "n":
        quit()
    global matrix
    for i in range(9):
        for j in range(9):
            matrix[i][j] = " "
    global start, mine, flen
    start = time.time()
    mine = []
    flen = 10

def check_win():
    global matrix, start
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == " ":
                return False
    for i in mine:
        matrix[i[0]][i[1]] = 'X'
    t = int(time.time() - start)
    if t % 60 == 0:
        print(f"\nYou Win. It took you {t // 60} minutes.\n")
    else:
        print(f"\nYou Win. It took you {t // 60} minutes and {t % 60} seconds.\n")
    printboard()
    print()
    again()
    return True

def check(n):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    if n not in abc:
        return -1
    return abc.index(n)

def check_input(e):  # 確認輸入的座標有無問題
    if len(e) < 2 or len(e) > 3:
        return False
    if not e[0].isalpha() or e[0] not in "abcdefghi":
        return False
    if not e[1].isdigit() or int(e[1]) < 1 or int(e[1]) > 9:
        return False
    if len(e) == 3 and e[2] != "f":
        return False
    return True

def trans(e):  # 把英文字母轉成索引 #數字索引要減一
    row, col = check(e[0]), int(e[1]) - 1
    return row, col

invalid = "\nInvalid cell. Enter the column followed by the row (ex:a5). To add or remove a flag, add \'f\' to the cell (ex:a5f)."
flen = 10
help = 1  # 是否需要幫助
start = time.time()

first_move = get_first_move()  # 獲取玩家第一步輸入
mines(first_move)  # 根據第一步輸入生成地雷

while True:
    printboard()
    if help == 1:
        help = 0
        print('\nEnter the column followed by the row (ex:a5). To add or remove a flag,')
        print("add \'f\' to the cell (ex: a5f).Type \'help\' to show this message again")
    user_input = input(f"\nEnter the cell ({flen} mines left): ").lower()
    if user_input == "help":
        help = 1
        continue
    if not check_input(user_input):
        print(invalid)
        continue
    row, col = trans(user_input)

    if len(user_input) == 3:  # 插入旗幟
        flag(row, col)
    current_cell = [row, col]
    if matrix[current_cell[0]][current_cell[1]] == "F":
        print("\nThere is a flag there.")
        continue
    if matrix[current_cell[0]][current_cell[1]] != " ":
        print("\nThat cell is already shown.")
        continue
    if [current_cell[0], current_cell[1]] in mine:
        loser()
        continue
    dive(current_cell[0], current_cell[1])
    if check_win():
        break

def get_first_move():
    while True:
        user_input = input("請輸入你的第一步座標 (例如 a5): ").lower()
        if check_input(user_input):
            row, col = trans(user_input)
            return [row, col]
        else:
            print(invalid)