#林宜萱B14111369統計115

s=input("Enter a string:").strip()
n=len(s)

matrix=[[0]*n for _ in range(n)] #初始化n*n的二維0陣列
count=0
max_length=1 #設定0 or 1?????

#n==1的時候
for i in range(n):
    matrix[i][i]=True
#n==2的時候
for i in range(n-1):
    if s[i]==s[i+1]:
        matrix[i][i+1]=True
        count=i
        max_length=2
#n>2的時候        
else:
    for x in range(3,n+1): #x從第3個字元開始找有沒有回文
        for i in range(n-x+1): #i是起始索引
            j=i+x-1
            if s[i]==s[j] and matrix[i+1][j-1]:
                matrix[i][j]=True
                if x>max_length:
                    count=i
                    max_length=x
print("LPS is:",s[count:count+max_length])
print("Length is:",len(s[count:count+max_length]))
