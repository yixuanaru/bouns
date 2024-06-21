
#看有沒有連縣
def check(line):
    return all(x == line[0] and x != 0 for x in line) #所有元素都相同且不為0

def checkwinner():
    r=1
    #水平
    for i in range(6):
        for j in range(4):
            if check(bb[i][j:j+4]):
                if bb[i][j] == 1:
                    bb[i][j:j+4] = [3] * 4
                else:
                    bb[i][j:j+4] = [4] * 4
                r=0
    #垂直
    for i in range(3):
        for j in range(7):
            if check([bb[i+k][j] for k in range(4)]):
                if bb[i][j] == 2:
                    for k in range(4):
                        bb[i+k][j] = 4
                else:
                    for k in range(4):
                        bb[i+k][j] = 3
                r=0
    #右下左上
    for i in range(6 - 3):
        for j in range(4):
            if check([bb[i+k][j+k] for k in range(4)]):
                if bb[i][j] == 1:
                    for k in range(4):
                        bb[i+k][j+k] = 3
                else:
                    for k in range(4):
                        bb[i+k][j+k] = 4
                r=0
    #右上左下
    for i in range(3, 6):
        for j in range(4):
            if check([bb[i-k][j+k] for k in range(4)]):
                if bb[i][j] == 1:
                    for k in range(4):
                        bb[i-k][j+k] = 3
                else:
                    for k in range(4):
                        bb[i-k][j+k] = 4
                r=0
    return r


'''
#確認輸入的只有數字且範圍在0到6之間的function
def valid(inputt):
    if len(inputt) == 1 and inputt.isdigit():
        num = int(inputt)
        if 0 <= num <= 6:
            return True
        else:
            print("Out of range. Try again [0-6]")
    else:
        print("Invalid input. Try again [0-6]")
    return False我真的快瘋了'''


#確認col是不是滿了
def colfull(i,player):
    if player==0:
        for j in range(6):
            if bb[5-j][i]==0:
                bb[5-j][i]=1
                return 1
        print("This column is full. Try another column")
        return 0
    else:
        for j in range(6):
            if bb[5-j][i]==0:
                bb[5-j][i]=2
                return 1
        print("This column is full. Try another column")
        return 0

#判斷和局
def boardfull():
    for i in range(7):
        if bb[0][i]==0:
            break
        if i==6 and not bb[0][6]==0:
            print("Draw")
            quit()


#用來計框框裡面的值
symbols = [' ', 'X', 'O', 'x', 'o']
def gogo(i):
    return symbols[i]
#遊戲ㄉ格子們
def printboard(): 
       print("+---"*7+"+")
       for i in range(6):
              for j in range(7):
                     print("| %s "%(gogo(bb[i][j])), end='')
              print("|")
              print("+---" * 7 + "+")
       print("  0   1   2   3   4   5   6")

       
#bb是棋盤戰況
bb = [[0 for _ in range(7)] for _ in range(6)]
ok=0 #如果正常 就是1 異常就是0
x=1 # 如果x=1就代表遊戲還沒結束
player=0 #0代表先攻的X 1則是O 
while x:
    if ok==0:
        printboard()
    if player==0:
        a=input("Player X >> ")
    else:
        a=input("Player O >> ")


    if not a.isdigit(): #如果輸入非0-6的值
        print("Invalid input, try again [0-6].")
        ok=1
        continue
    else:
        if int(a)>6 or int(a)<0:#是數字 阿但是如果超出0-6的範圍
            ok=1
            print("Out of range,try again")
            continue

    if not colfull(int(a),player): 
        ok=1
        boardfull() 
        continue
    else:
        ok=0
    player = 1 - player
    if checkwinner() == 1:
        x = 1
    else:
        x = 0

player = 1 - player
if player==0:
    printboard()
    print("Winner: X")
else:
    printboard()
    print("Winner: O")

