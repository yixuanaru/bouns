
def imfine(matrix,x,y,k):
    oc=matrix[x][y]  #座標原本的顏色
    if oc==k:        #如果輸入的k直接等於初始座標就直接回傳
        return matrix 
    row=len(matrix)
    col=len(matrix[0])
    xyxy=[(x, y)]       #用來存需要改的座標，起始座標也要加進去
    while xyxy:
        i,j=xyxy.pop()  #每次都處理新的座標
        if matrix[i][j]!=oc: #如果這個顏色跟座標的顏色不同我就跳過然後繼續找
            continue
        matrix[i][j]=k 
        for xx,yy in [(1,0),(0,1),(-1,0),(0,-1)]: #檢查像素相鄰的座標
            ii=i+xx 
            jj=j+yy
            if 0<=ii<row and 0<=jj<col: #如果座標都在矩陣裡
                if matrix[ii][jj]==oc:  #如果他跟初始座標的顏色依樣就加進我處存座標的陣列裡面
                    xyxy.append((ii,jj))

    return matrix


n=list(map(int,input("Enter index x,y,k(seperate by whitespace):").split(" ")))
x,y,k=n[0],n[1],n[2]
print("Enter the matrix by multiple lines:")
matrix=[] #用來存使用者輸入的矩陣的矩陣
while True:
    i=input()
    if i=='q':
        break
    matrix.append(list(map(int,i.split())))

#跑function更新矩陣
result=imfine(matrix,x,y,k)

#輸出新的矩陣
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if j==len(matrix[0])-1:
           print(matrix[i][j])
           break
        print(matrix[i][j],end=" ")