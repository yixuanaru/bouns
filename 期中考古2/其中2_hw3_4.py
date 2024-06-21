def imfine(matrix, x, y, k):
    oc = matrix[x][y]
    if oc == k:
        return matrix
    
    def dfs(i, j):
        if not (0 <= i < len(matrix) and 0 <= j < len(matrix[0])) or matrix[i][j] != oc:
            return
        matrix[i][j] = k
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dfs(i + dx, j + dy)

    dfs(x, y)
    return matrix

def get_matrix():
    matrix = []
    print("Enter the matrix by multiple lines (press 'q' to quit):")
    while True:
        row = input().strip()
        if row == 'q':
            break
        matrix.append(list(map(int, row.split())))
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))



x, y, k = map(int, input("Enter index x, y, k (separated by whitespace): ").split())
matrix = get_matrix()
result = imfine(matrix, x, y, k)

print_matrix(result)