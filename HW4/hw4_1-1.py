import random
import time

matrix=[[" " for i in range(9)] for j in range(9)]
def printboard(): #輸出遊戲背景
    a="    a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i"
    b="  "+"+---"*9+"+"
    print(a)
    print(b)
    for i in range(9):
        print(i+1,"",end="")
        for j in range(9):
            if j==8:
                print("| %s |"%(matrix[i][j]))
                print(b)
                continue
            print("| %s "%(matrix[i][j]),end="")
    return matrix

mine=[]
def mines(): #設炸彈
    global c
    while len(mine)!=10:
        m=[random.randint(0,8),random.randint(0,8)]
        if m!=c and not m in mine:
            mine.append(m)

def find(i,j):
    count=0
    if [i+1,j+1] in mine:
        count+=1
    if [i+1,j] in mine:
        count+=1
    if [i,j+1] in mine:
        count+=1
    if [i-1,j-1] in mine:
        count+=1
    if [i-1,j] in mine:
        count+=1
    if [i,j-1] in mine:
        count+=1
    if [i+1,j-1] in mine:
        count+=1
    if [i-1,j+1] in mine:
        count+=1
    return count

def dive(i,j):
    if i<0 or i>8 or j<0 or j>8:
        return
    if matrix[i][j]=="0":
        return
    count=find(i,j)
    if count!=0:
        matrix[i][j]="%s"%(count)
        return
    else: #如果count=0 matrix[i][j]顯示0
        matrix[i][j]="0"
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            dive(i+dx,j+dy)

def flag(i,j):
    global matrix,flen
    if matrix[i][j]==" ":
        matrix[i][j]="F"
        if [i,j] in mine:
            flen=flen-1
        return
    if matrix[i][j]=="F":
        if [i,j] in mine:
            flen=flen+1
        matrix[i][j]=" "
        return
    print("Cannot put a flag there")

def loser():
    for i in mine:
        matrix[i[0]][i[1]]="X"
    print("\ngame over\n")
    time.time()
    printboard()
    again()

def again():
    a=input("Play again?(y/n): ")
    if a=="n":
        quit()
    for i in range(9):
        for j in range(9):
            matrix[i][j]=" "
    global start,mine,flen,mineee,help
    help=1
    start=time.time()
    mine=[]
    flen=10
    mineee=1

def win():
    for i in range(9):
        for j in range(9):
            if matrix[i][j]==" ":
                return
    for i in mine:
        matrix[i[0]][i[1]]='X'
    t=int(time.time()-start)
    if t%60==0:
        print(f"You win. It took you {t} minutes.",end="\n")
    else:
        print(f"You Win. It took you {t//60} minutes and {t%60} seconds.",end="\n")
    printboard()
    print()
    again()

def check(n):
    global abc
    abc=["a","b","c","d","e","f","g","h","i"]
    if n not in abc:
        return -1
    return abc.index(n)

invalid="\nInvalid cell. Enter the column followed by the row (ex:a5). To add or remove a flag, add \'f\' to the cell (ex:a5f)."
flen=10
c=[0,0]
help=1 #是否需要幫助
start=time.time()
e=0
mineee=1

while True:
    if e==0:
        printboard()
    if help==1:
        help=0
        print('\nEnter the column followed by the row (ex:a5). To add or remove a flag,')
        print("add \'f\' to the cell (ex: a5f).Type \'help\' th show this message again")
    e=input(f"\nEnter the cell ({flen} mines left): ")
    if e=="help":
        help=1
        e=1
        printboard()
        continue
    if len(e)==3: #要插旗子
        if e[2]!='f':
            printboard()
            e=1
            print(invalid)
            continue
        if not e[1].isnumeric():
            printboard()
            e=1
            print(invalid)
            continue
        if int(e[1])<1 or int(e[1])>9:
            printboard()
            e=1
            print(invalid)
            continue
        if check(e[0])==-1:
            printboard()
            e=1
            print(invalid)
            continue
        c=int(e[1])-1,check(e[0])
        flag(c[0],c[1])
        e=0
        continue
    if len(e)==2:
        if not e[1].isnumeric():
            printboard()
            e=1
            print(invalid)
            continue
        if int(e[1])<1 or int(e[1])>9:
            printboard()
            e=1
            print(invalid)
            continue
        if check(e[0])==-1:
            printboard()
            e=1
            print(invalid)
            continue
        c=int(e[1])-1,check(e[0])
    if len(e)==1 or len(e)>2:
        e=1
        printboard()
        print(invalid)
        continue

    if matrix[c[0]][c[1]]=="F":
        printboard()
        print("\nThere is a flag there.")
        e=1
        continue
    if matrix[c[0]][c[1]]!=" ":
        printboard()
        print("\nThat cell is already shown.")
        e=1
        continue
    if mineee==1:
        mineee=0
        mines()
    e=0
    if [c[0],c[1]] in mine:
        loser()
        continue
    dive(c[0],c[1])
    win()