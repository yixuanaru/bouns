row=int(input("Enter the number of rows:"))
col=int(input("Enter the number of columns:"))
rseat=input("Enter the reserved seats:").split("|") #我要預約的座位

matrix = [["A" for _ in range(col)] for _ in range(row)]
#reserved=[]
outseat=[]
for seat in rseat:
    i,j=map(int,seat.split(','))
    i,j=i-1,j-1 #座位藥檢1 因為索引其實是從零開始
    if 0<=i<row and 0<=j<col:
        matrix[i][j]="R"
        #reserved.append(seat)
    else:
        outseat.append(seat)

if outseat:
    print("Out-of-range reserved seats:","|".join(outseat))

for i in matrix:
    print(" ".join(i))

