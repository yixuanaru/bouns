def imfine(matrix, x, y, k):
    original_color = matrix[x][y]
    if original_color == k:
        return matrix
    
    def dfs(i, j):
        if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])) or matrix[i][j] != original_color:
            return
        matrix[i][j] = k
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dfs(i + dx, j + dy)

    dfs(x, y)
    return matrix

def get_matrix():
    print("Enter the matrix by multiple lines (press 'q' to quit):")
    matrix = []
    while (row == input().strip()) != 'q':
        matrix.append(list(map(int, row.split())))
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    x, y, k = map(int, input("Enter index x, y, k (separated by whitespace): ").split())
    matrix = get_matrix()
    result = imfine(matrix, x, y, k)
    print_matrix(result)
