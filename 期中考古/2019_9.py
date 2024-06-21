n=input("input list:")
low=input("input low:")
high=input("input high:")
nlist=[int(num) for num in n.split(" ")]
num=0
start=int(low)
result=[]
for num in nlist:
    if num>start:
        if num-start==1:
            result.append(start)
        else:
            result.append(f"{start}->{num-1}")
    start=num+1

if num<int(high):
    result.append(f"{start}->{high}")

print(result)
