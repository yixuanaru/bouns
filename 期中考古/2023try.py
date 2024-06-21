'''
#6
n=input("Enter a time:")
t=n.split(":")
h,m,s=int(t[0]),int(t[1]),int(t[2])
if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
    print("seconds in a day=",h*3600+m*60+s)'''

#7
n=int(input("Enter a positive number(>=2):"))
plist=[]
c=2
while c<=n:
    if (2**(c-1))%c==1 or c==2:
        plist.append(c)
    c=c+1
print(f"prime list 2-{n}={plist}")