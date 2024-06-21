def imfine(matrix, x, y, k):
    oc = matrix[x][y]
    if oc == k:
        return matrix

    row, col = len(matrix), len(matrix[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(i, j):
        if not (0 <= i < row and 0 <= j < col) or matrix[i][j] != oc:
            return
        matrix[i][j] = k
        for dx, dy in directions:
            dfs(i + dx, j + dy)

    dfs(x, y)
    return matrix