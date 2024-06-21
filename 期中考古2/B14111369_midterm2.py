import random

def generate_path(N, M):
    # Goal: Generate a maze with a clear path from the starting point to the bottom-right cell using a brute-force approach.
    # Detailed Instructions:
    # 1. Create a 2D list of zeros representing the maze map with dimensions N rows by M columns.
    # 2. Start at the top-left cell of the maze map and add it to the path list.
    # 3. While not at the bottom-right cell of the maze map:
    #     a. If at the bottom row of the maze map, move right.
    #     b. If at the rightmost column of the maze map, move down.
    #     c. Otherwise, randomly choose to move right or down.
    #     d. Mark the chosen cell as part of the path and add it to the path list.
    # 4. Mark the bottom-right cell of the maze map as part of the path and add it to the path list.
    # 5. Return the updated maze map with the path.

        # your code here
    i,j=[0,0] #起點
    maze = []
    path=[] #經過路線
    for i in range(N):
        row = []
        for j in range(M):
            row.append(0)
        maze.append(row)
    path+=[i,j] #add 起點 to the path list

    while [N-1,M-1] not in path:   #While not at the bottom-right cell of the maze map:
        if j<M and j!=M-1:         #If at the bottom row of the maze map, move right.
            j+=1  #往右但不往下
            i+=0
        if j==M-1:                 #If at the rightmost column of the maze map, move down.
            i+=1  #往下且不能往右
            j+=0
        else:                     #隨機選擇要往右或往下
            ran=[[1,0],[0,1]] #可以i+1或是j+1
            move=random.choice(ran)
            if move==ran[0]: #如果選到[1,0] 就是往右但不往下
                j+=1
                i+=0
            if move==ran[1]:#如果選到[0,1] 就是往下但不往右
                i+=1
                j+=0
        path.append([i,j])      #把移動的路徑新增到path裡面
    #print(path)
        for i in path:          #用for迴圈循環那些在path裡面的每個座標 如[0,0],[0,1]......
            maze[i[0]][i[1]]="2" #把這些座標在地圖上更改成2 
    return maze    #回傳地圖
    
def add_obstacles(maze, num_obstacles):
    # Goal: Add a number of obstacles randomly to the maze.
    # Detailed Instructions:
    # 1. While the number of obstacles in the maze is less than num_obstacles:
        # a. Choose a random cell in the maze that is not part of the path or already an obstacle.
        # b. Mark the cell as an obstacle.
    # 2. Return the updated maze map with the obstacles.

    # your code here
    mine=[] #儲存地雷
    
    while len(mine)<num_obstacles:  #如果地雷的數量少於指定地雷的數 #提示1.
        m=[random.randint(0,N),random.randint(0,M)] #隨機生成地雷
        if m!=[0,0] and not m in mine: #地雷不可等於起點[0,0] 且不重複生成在同一個座標
            mine.append(m) #把座標儲存進mine
            maze[m[0]][m[1]]="1" #Mark the cell as an obstacle.
    return maze #提示2.


def generate_maze(N, M, num_obstacles):
    # Goal: Generate a maze with a clear path from the starting point to the bottom-right cell and a number of obstacles using a brute-force approach.
    # Detailed Instructions:
    # 1. Call the generate_path function with the arguments N and M to generate a maze with a clear path.
    # 2. Call the add_obstacles function with the generated maze map and the argument num_obstacles to add a number of obstacles randomly to the maze.
    # 3. Return the updated maze map.


    # generate a maze with a clear path from the starting point to the bottom-right cell
    maze = generate_path(N, M)

    # add the number of obstacles randomly to the maze
    maze = add_obstacles(maze, num_obstacles)

    return maze



def print_maze(maze):
    # Goal: Print the maze map as a grid to the console using boundaries with "-", "|", and "+" symbols.
    # Detailed Instructions:
    # 1. For each row in the maze map:
    #   a. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them.
    #   b. For each cell in the row:
    #       If the cell is an obstacle, print an "X" symbol.
    #       Otherwise, print a space character.
    #   c. Print a vertical boundary line with "|" symbols at the ends.
    # 2. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them at the bottom of the maze map.
    
    print("+" + "---+" * len(maze[0]))
    for i in range(len(maze)):
        row_str = "|"
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                row_str += "   "
            elif maze[i][j] == 1:
                row_str += " X "
            elif maze[i][j] == 2:
                row_str += "   "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * len(maze[0]))

# prompt the user to input the values of N, M, and num_obstacles
N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N*M-(N+M-1)
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))

# generate the maze using the user-specified values
maze = generate_maze(N, M, num_obstacles)

# print the generated maze as a grid to the console
print("Generated Maze Map:")
print_maze(maze)
