'''def modify_collection(col):
    for i in range(len(col)):
        col[i-1] = col[i-1] + col[i//2]
    print(col)

def modify_collection(col):
    new_col = {}
    for i in range(1, len(col)):
        new_col[i-1] = col[i-1] + col[i//2]
    print(new_col)'''

def modify_collection(col): 
    new_col = {} 
    for i in range(len(col)): 
        new_col[col[i-1]] = col[i-1] + col[i//2] 
    print(new_col) 


modify_collection([1, 2, 3, 4]) 
modify_collection(["a", "b", "c", "d"]) 
modify_collection("abcd") 
modify_collection({-1:"z", 0:"a", 1:"b", 2:"c"}) 
modify_collection({-1:[-1,0], 0:[0,1], 1:[1,2], 2:[2,3]})

