layer=int(input("Enter the number of layers(2 to 5)="))
topside=int(input("Enter the side length of the top layers(2 to 6)="))
growth=int(input("Enter the growth of each year(1 to 5)="))
twide=int(input("Enter the trunk width(odd number, 3 to 9)="))
thight=int(input("Enter the trunk height(4 to 10)="))

#最頂的三角形
n=topside
x=growth*layer+topside
if n<2 or n>5:
    print("try again")
else:
    print(" "*(x-1)+"#")
    i=2
    while i<=n:
        if i==n:
            print(" "*(x-i)+"#"*(2*i-1))
        else:
            print(' '*(x-i)+"#"+'@'*(2*i-3)+"#")
        i+=1

#其他ㄉ三角形
j=1
while j<layer:
    n+=growth
    i=2
    while i<=n:
        if i==n:
            print(" "*(x-i)+"#"*(2*i-1))
        else:
            print(' '*(x-i)+"#"+'@'*(2*i-3)+"#")
        i+=1
    j+=1

#樹幹||||
if twide<3 or twide%2==0:
    print("try again")
else:
    i=0
    while i<thight:
        print(" "*(x-int(twide/2)-1)+"|"*twide)
        i+=1
