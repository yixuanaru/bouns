#林宜萱B14111369統計115

#三角形
layer=int(input("Enter the number of layers(2 to 5)="))
topside=int(input("Enter the side length of the top layers(2 to 6)="))
growth=int(input("Enter the growth of each year(1 to 5)="))
#樹幹
twide=int(input("Enter the trunk width(odd number, 3 to 9)="))
thight=int(input("Enter the trunk hight(4 to 10)="))

#頂部三角形
n=topside
x=growth*layer+topside #我用X來算要預留的空格，用每次增加的邊長乘有幾個三角形再加上最上面的三角形的邊長 就能預留好空格
if n<2 or n>5: #頂三角邊長2 to 5 
    print("try again")
else:
    print(" "*(x-1)+"#") 
    for i in range(2,n+1):
        if i==n:
            print(" "*(x-i)+"#"*(2*i-1))
        else:
            print(' '*(x-i)+"#"+'@'*(2*i-3)+"#")
#其他的三角形
    for j in range(1,layer):
        n+=growth
        for i in range(2,n+1):
            if i==n:
                print(" "*(x-i)+"#"*(2*i-1))
            else:
                print(' '*(x-i)+"#"+'@'*(2*i-3)+"#")
            
        
#樹幹|
if twide<3 or twide%2==0:
    print("try again")
else:
    for i in range(thight):
        print(" "*(x-int(twide/2)-1)+"|"*twide)
