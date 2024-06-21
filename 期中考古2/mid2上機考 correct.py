import random

def generate_path(N, M):
    # 1. Create a 2D list of zeros representing the maze map with dimensions N rows by M columns.
    maze = [[0] * M for _ in range(N)]
    
    # 2. Start at the top-left cell of the maze map and add it to the path list.
    i, j = 0, 0  # Start at the top-left cell (0, 0)
    path = [[i, j]]  # Add the starting cell to the path list

    # 3. While not at the bottom-right cell of the maze map:
    while [N - 1, M - 1] not in path:
        # a. If at the bottom row of the maze map, move right.
        if i == N - 1:
            j += 1
        # b. If at the rightmost column of the maze map, move down.
        elif j == M - 1:
            i += 1
        # c. Otherwise, randomly choose to move right or down.
        else:
            move = random.choice([(0, 1), (1, 0)])
            i += move[0]
            j += move[1]
        # d. Mark the chosen cell as part of the path and add it to the path list.
        path.append([i, j])

    # 4. Mark the bottom-right cell of the maze map as part of the path and add it to the path list.
    # (Already done in the previous step)

    # 5. Return the updated maze map with the path.
    for i, j in path:
        maze[i][j] = 2  # Mark the path cells as 2

    return maze

def add_obstacles(maze, num_obstacles):
    # 1. While the number of obstacles in the maze is less than num_obstacles:
    N, M = len(maze), len(maze[0])
    obstacles = set()  # Set to store the obstacle coordinates
    path_cells = set((i, j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == 2)  # Set of path cells

    while len(obstacles) < num_obstacles:
        # a. Choose a random cell in the maze that is not part of the path or already an obstacle.
        i, j = random.randint(0, N - 1), random.randint(0, M - 1)
        if (i, j) not in path_cells and (i, j) not in obstacles:
            # b. Mark the cell as an obstacle.
            obstacles.add((i, j))
            maze[i][j] = 1  # Mark the cell as an obstacle

    # 2. Return the updated maze map with the obstacles.
    return maze

def generate_maze(N, M, num_obstacles):
    # 1. Call the generate_path function with the arguments N and M to generate a maze with a clear path.
    maze = generate_path(N, M)

    # 2. Call the add_obstacles function with the generated maze map and the argument num_obstacles to add a number of obstacles randomly to the maze.
    maze = add_obstacles(maze, num_obstacles)

    # 3. Return the updated maze map.
    return maze

def print_maze(maze):
    # 1. For each row in the maze map:
    N, M = len(maze), len(maze[0])

    # Print the top boundary
    print("+" + "---+" * M)

    for i in range(N):
        row = "|"
        # b. For each cell in the row:
        for j in range(M):
            #    If the cell is an obstacle, print an "X" symbol.
            if maze[i][j] == 1:
                row += " X |"
            #    Otherwise, print a space character.
            else:
                row += "   |"
        # c. Print a vertical boundary line with "|" symbols at the ends.
        print(row)
        print("+" + "---+" * M)

    # 2. Print a horizontal boundary line with "+" symbols at the intersections and "-" symbols between them at the bottom of the maze map.
    # (Already done in the previous step)

# prompt the user to input the values of N, M, and num_obstacles
N = int(input("Enter the number of rows (N): "))
M = int(input("Enter the number of columns (M): "))
max_possible_obs = N * M - (N + M - 1)
num_obstacles = int(input("Enter the number of obstacles (0-" + str(max_possible_obs) + "): "))
while num_obstacles < 0 or num_obstacles > max_possible_obs:
    num_obstacles = int(input("Re-enter again (0-" + str(max_possible_obs) + "): "))

# generate the maze using the user-specified values
maze = generate_maze(N, M, num_obstacles)

# print the generated maze as a grid to the console
print("Generated Maze Map:")
print_maze(maze)