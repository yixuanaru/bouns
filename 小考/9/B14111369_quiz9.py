import random

def generate_path(maze, N, M):
    # Initialize the starting cell (0, 0) as the path
    maze[(0, 0)] = 2
    current_row, current_col = 0, 0

    while current_row != N - 1 or current_col != M - 1:
        # If we haven't reached the bottom-right cell
        if current_row == N - 1:
            # If we're on the last row, move right
            current_col += 1
            maze[(current_row, current_col)] = 2
        elif current_col == M - 1:
            # If we're on the last column, move down
            current_row += 1
            maze[(current_row, current_col)] = 2
        else:
            # Otherwise, randomly choose to move down or right
            direction = random.choice(['down', 'right'])
            if direction == 'down':
                current_row += 1
            else:
                current_col += 1
            maze[(current_row, current_col)] = 2


def add_obstacles(maze, min_obstacles, N, M):
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze.get((i, j), 0) == 0]
    obstacles_added = 0

    while obstacles_added < min_obstacles:
        if not empty_cells:
            print("No more empty cells available to add obstacles.")
            break

        row, col = random.choice(empty_cells)
        try:
            maze[(row, col)] = 1
            empty_cells.remove((row, col))
            obstacles_added += 1
        except KeyError:
            print(f"Error: Unable to set obstacle at ({row}, {col})")
    

def set_obstacle(maze, N, M):
    while True:
        try:
            n=input("Enter the coordinate to set an obstacle, e.g. i,j: ")
            if len(n.split(","))!=2:
                print("ValueError in set_obstale function. Need to be coordinates")
                continue
            else:
                row,col=n.split(",")
                if row < 0 or row >= N or col < 0 or col >= M:
                    print("ValueError in set_obstale function. Need to be coordinates")
                    continue
                
                if maze.get((row, col), 0) == 2:
                    print("Cannot set an obstacle on the path. Please try again.")
                    continue
                elif maze.get((row, col), 0) == 1:
                    print("An obstacle already exists at this location. Please try again.")
                    continue
            
            maze[(row, col)] = 1
            print("Obstacle set successfully.")
            break
        
        except ValueError:
            print("ValueError in set_obstale function. Need to be coordinates")


def remove_obstacle(maze, N, M):
    while True:
        try:
            n=input("Enter the coordinate to remove an obstacle, e.g. i,j: ")
            row,col=n.split(",")

            if row < 0 or row >= N or col < 0 or col >= M:
                print("Invalid coordinates. Please try again.")
                continue

            if maze.get((row, col), 0) == 2:
                print("Cannot remove an obstacle from the path. Please try again.")
                continue
            elif maze.get((row, col), 0) == 0:
                print("There is no obstacle at this location. Please try again.")
                continue

            maze[(row, col)] = 0
            print("Obstacle removed successfully.")
            break

        except ValueError:
            print("ValueError in remove_obstacle function. Need to be coordinates")

def print_maze(maze, N, M):
    with open(file_name, 'w') as file:
        for i in range(N):
            line = []
            for j in range(M):
                if maze[(i, j)] == 0:
                    line.append(' ')
                elif maze[(i, j)] == 1:
                    line.append('X')
                elif maze[(i, j)] == 2:
                    line.append('O')
            file.write('|' + '|'.join(line) + '|\n')

def main():
    # Load the maze grid from a file
    while True:
        try:
            global file_name
            file_name = input("Enter the name of the file containing the maze grid: ")
            with open(file_name, 'r') as file:
                grid = file.readlines()
            break
        except IOError:
            print("Error: File not found. Please try again.")

# Parse the maze dimensions from the file
    N = len(grid)
    M = 0
    for row in grid:
        row = row.strip()
        if '+' in row:
            M = max(M, len(row.split('+')) - 1)

    # Initialize the maze dictionary
    maze = {}

    # Populate the maze with obstacles from the file
    for row in range(N):
        row_str = grid[row].strip()
        for col in range(M):
            if 2 + 4 * col < len(row_str):
                if row_str[2 + 4 * col] == 'X':
                    maze[(row, col)] = 1
                else:
                    maze[(row, col)] = 0
            else:
                # Handle cases where the index is out of range
                maze[(row, col)] = 0

    # Ask the user for the minimum number of obstacles to add
    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
            if min_obstacles < 0:
                print("Invalid input. The number of obstacles must be non-negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Generate the path and add obstacles
    generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)

    # User interaction loop
    while True:
        print("\nOptions:")
        print("1. Set an obstacle")
        print("2. Remove an obstacle")
        print("3. Print the maze")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                set_obstacle(maze, N, M)
            elif choice == 2:
                remove_obstacle(maze, N, M)
            elif choice == 3:
                print_maze(maze, N, M)
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
        except NameError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()