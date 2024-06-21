def for99(v):
    for i in range(3):
        for j in range(9,0,-1):
            for k in range(3):
                print(f"{j} x {v[i][k]} = {j*v[i][k]}",end="\t")
            print()
        print()


vector=[
    [9,8,7],[6,5,4],[3,2,1]
]

for99(vector)