n=int(input("Enter a positive integer:"))
plist=[]
count=2
while count<n:
    prime=True
    i=2
    while i<count:
        if count%i==0:
            prime=False
            break
        i+=1
    if prime:
        plist=plist+[count]
    count+=1
print(plist)


#7
n=int(input("Enter a positive number(>=2):"))
plist=[]
c=2
while c<=n:
    if (2**(c-1))%c==1 or c==2:
        plist.append(c)
    c=c+1
print(f"prime list 2-{n}={plist}")