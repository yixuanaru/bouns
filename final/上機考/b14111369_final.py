def get_matrix(name):
    print(f"Enter matrix {name}: ", end='')
    rows = input().split('|')  #用|分開
    matrix = {}

    #用,再分開每個數字而且把他們都轉換成整數，並把索引當作key數字當作值存進字典裡
    for i in range(len(rows)):
        elements = [int(x) for x in rows[i].split(',')]
        matrix[i] = elements
    return matrix

#乘法的計算
def matrix_multiply(U, V):
    #range 
    if len(U[0]) != len(V):
        raise ValueError("ERROR,Cannot multiply matrices")
    
    M = {}
    for i in range(len(U)):
        M[i] = [0] * len(V[0]) 
        for j in range(len(V[0])):
            for k in range(len(V)):
                M[i][j] += U[i][k] * V[k][j]
    return M

#用for跑字典並輸出結果
def print_matrix(M):
    for row in M.values():
        print(row)

#使用者輸入U、V矩陣
U = get_matrix('U')
V = get_matrix('V')

#乘法時間
M = matrix_multiply(U, V)

#輸出最後的結果
print("M = U x V")
print_matrix(M)