while True:
    n=int(input("input the range number(n>2):"))
    if n<=2:
        print("try again")
        continue
    else:
        break
print("Perfect numbers:")

result=[]
for num in range(2,n+1):
    sum=0
    for i in range(1,num):
            if num%i==0:
                sum+=i
    if sum==num:
        result.append(sum)
print(result)
            

        