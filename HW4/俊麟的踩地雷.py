def ming():#mine generator
    global mine
    while len(mine)!=10:
        mi=[random.randint(0,8),random.randint(0,8)]
        if mi!=o and not mi in mine:
            mine+=[mi]
def disp():#to display
    a="    a  "+" b  "+" c  "+" d  "+" e  "+" f  "+" g  "+" h  "+" i"
    b="  "+"+---"*9+"+"
    print(a)
    print(b)
    for i in range(9):
        print(i+1,"",end="")
        for j in range(9):
            if j==8:
                print("| %s |"%(matr[i][j]))
                print(b)
                continue
            print("| %s "%(matr[i][j]),end="")
def tran(a):#to translate
    q=['a','b','c','d','e','f','g','h','i']
    if not a in q:
        return -1
    return q.index(a)
def ddive(i,j):# to detect the mine in a given area
    c=0
    if [i-1,j-1] in mine:
        c+=1
    if [i-1,j] in mine:
        c+=1
    if [i-1,j+1] in mine:
        c+=1
    if [i,j-1] in mine:
        c+=1
    if [i,j+1] in mine:
        c+=1
    if [i+1,j-1] in mine:
        c+=1
    if [i+1,j] in mine:
        c+=1
    if [i+1,j+1] in mine:
        c+=1
    return c
def dive(i,j):#dive in every direction to konw what coordinate should be displayed
    if i<0 or i>8 or j<0 or j>8:
        return
    global matr
    if matr[i][j]=="0":
        return
    c=ddive(i,j)
    if c!=0:
        matr[i][j]="%s"%(c)
        return
    else:
        matr[i][j]="0"
        dive(i+1,j)
        dive(i,j+1)
        dive(i-1,j)
        dive(i,j-1)
        dive(i+1,j+1)
        dive(i-1,j-1)
        dive(i-1,j+1)
        dive(i+1,j-1)
def flag(i,j):#to do the flag function
    global matr
    global l
    if matr[i][j]==" ":
        matr[i][j]="F"
        if [i,j] in mine:
            l=l-1
        return
    if matr[i][j]=="F":
        if [i,j] in mine:
            l=l+1
        matr[i][j]=" "
        return
    print("Cannot put a flag there")
def final():#executed when the player failed
    print("\n")
    global matr
    for i in mine:
        matr[i[0]][i[1]]='X'
    print("Game Over\n")
    time.time()
    disp()
    print(" ")
    retry()
def retry():#to konw if the game would be played again, if so, reset some variables
    o=input("Play again? (y/n):")
    if o=='n':
        quit()
    global matr
    for i in range(9):
        for j in range(9):
            matr[i][j]=" "
    global s
    s=time.time()
    global t
    t=1
    global mine
    mine=[]
    global kk
    kk=1
    global l
    l=10
def fwin():#to detect if the player wins at each round
    global matr
    global s
    for i in range(9):
        for j in range(9):
            if matr[i][j]==" ":
                return
    for i in mine:
        matr[i[0]][i[1]]='X'
    t=int(time.time()-s)
    if t%60==0:
        print("\nYou Win. It took you %d minutes.\n"%(t/60))
    else:
        print("\nYou Win. It took you %d minutes and %d seconds.\n"%(t/60,t%60))
    disp()
    print(" ")
    retry()
import random
import time
matr=[[" " for i in range(9)] for j in range(9)]#the matrix
inval="\nInvalid cell. Enter the column followed by the row (ex:a5). To add or remove a flag, add \'f\' to the cell (ex:a5f)."
kk=1#variable determining if the mine should be generated
l=10#how many mines left
mine=[]#the mine coordinate
o=[0,2]#the first gussed coordinate
t=1#to show if it's ended at a normal situation
s=time.time()
k=0#variable containing the input
while 1:#the game
    if k==0:
        disp()
    if t==1:
        t=0
        print('\nEnter the column followed by the row (ex:a5). To add or remove a flag,')
        print("add \'f\' to the cell (ex: a5f).Type \'help\' th show this message again")
    k=input('\nEnter the cell (%d mines left):'%(l))
    if k=="help":
        t=1
        k=1
        disp()
        continue
    if len(k)==3:#to know if the input is legal and get the input
        if not k[2]=='f':
            disp()
            k=1
            print(inval)
            continue
        if not k[1].isnumeric():
            disp()
            k=1
            print(inval)
            continue
        if int(k[1])<1 or int(k[1])>9:
            disp()
            k=1
            print(inval)
            continue
        if tran(k[0])==-1:
            disp()
            k=1
            print(inval)
            continue
        o=[int(k[1])-1,tran(k[0])]
        flag(o[0],o[1])
        k=0
        continue
    if len(k)==2:#to know if the input is legal and get the input
        if not k[1].isnumeric():
            disp()
            k=1
            print(inval)
            continue
        if int(k[1])<1 or int(k[1])>9:
            disp()
            k=1
            print(inval)
            continue
        if tran(k[0])==-1:
            disp()
            k=1
            print(inval)
            continue
        o=[int(k[1])-1,tran(k[0])]
    if len(k)==1 or len(k)>2:#to know if the input is illegal
        k=1
        disp()
        print(inval)
        continue
    if matr[o[0]][o[1]]=='F':
        disp()
        print('\nThere is a flag there')
        k=1
        continue
    if matr[o[0]][o[1]]!=" ":
        disp()
        print('\nThat cell is already shown')
        k=1
        continue
    if kk==1:
        kk=0
        ming()
    k=0
    if [o[0],o[1]] in mine:
        final()
        continue
    dive(o[0],o[1])
    fwin()