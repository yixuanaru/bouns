n=int(input("Enter the size of the grid:"))
matrix=[["_" for _ in range(n)] for _ in range(n)]

for i in matrix:
    print(" ".join(i))

while True:
    coord=input("Enter the cell coordinates to edit:")
    if coord=="done":
        break
    else:
        row,col=map(int,coord.split(","))
        value=input("Enter the new value for the cell:")
        if 0<=i<n and 0<=j<n:
            matrix[row][col]=value
    
    for i in matrix:
        print(" ".join(i))