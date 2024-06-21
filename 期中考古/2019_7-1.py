while True:
    n=int(input("Enter a range number>1:"))
    if n<=1:
        continue
    break
result=[]
num=2
while num<=n:
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum+=i
        i+=1
    if sum==num:
        result.append(sum)
    num+=1

print("the perfect number:",result)