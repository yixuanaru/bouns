s=input("Enter a positive integer:")
l=[]
i=0
#先創空陣列放輸入的數字的陣列
while i<len(s):
    l+=[int(s[i])]
    i+=1
print(l)

#相鄰數字相加
result=[]
i=0
while i <len(l):
    if i==0:
        result=result+[sum(l[0:2])]
    elif i==len(l)-1:
        result=result+[sum(l[len(l)-2:len(l)-1])]
    else:
        result=result+[sum(l[i-1:i+2])]
    i+=1
print(result)