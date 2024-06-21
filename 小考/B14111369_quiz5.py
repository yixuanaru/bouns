n=int(input("Enter the size of the grid:"))

matrix=[["_" for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()

while True:
    coord=input("Enter the cell coordinates to edit:")
    if coord=="done":
        break
    else:
        row,col=map(int,coord.split(","))
        value=input("Enter the new value for the cell:")
        matrix[row][col]=value
    
    for i in range(n):
        print(" ".join(matrix[i]))