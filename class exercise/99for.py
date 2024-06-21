def for99(v):
    for i in range(3):
        for j in range(1,10):
            for k in range(0,3):
                print(v[i][k],"x",j,"=",v[i][k]*j,end="\t")
            print()
        print()
    
v=[[1,2,3],[4,5,6],[7,8,9]]
for99(v)