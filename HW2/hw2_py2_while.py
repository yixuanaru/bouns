n=int(input("input the range number:"))  
print("Perfect numbers:") 

if n<2:                   
    print("n>2")
else:
    num=2
    while num<=n:
        sum=0
        i=1
        while i<num:
            if num%i==0:
                sum+=i
            i+=1
        if sum==num:
            print(sum,end=" ")
        num+=1
