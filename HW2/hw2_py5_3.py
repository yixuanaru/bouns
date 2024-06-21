#林宜萱B14111369統計115

Fn=int(input("The number of the requested element in Fibonacci(n)="))
s1=input("The first string for Palindromic detection(s1):").strip()
n1=len(s1)
s2=input("The first string for Palindromic detection(s2):").strip()
n2=len(s2)
word=input("The plaintext to be encrypted:").upper()
print("------extract key for encypt method-----")

#費事數列
a=0
b=1
for i in range(Fn):
    if Fn==0:
        a==0
    else:
        a,b=b,a+b
print("The %d-th Fibonacci sequence number is %d" %(Fn,a),end=" ")
print()

#s1
matrix=[[0]*n1 for _ in range(n1)] #初始化n*n的二維0陣列
count=0
max_length=1 #設定0 or 1?????

for i in range(n1):
    matrix[i][i]=True

for i in range(n1-1):
    if s1[i]==s1[i+1]:
        matrix[i][i+1]=True
        count=i
        max_length=2
        
else:
    for x in range(3,n1+1):
        for i in range(n1-x+1): #i是起始索引
            j=i+x-1
            if s1[i]==s1[j] and matrix[i+1][j-1]:
                matrix[i][j]=True
                if x>max_length:
                    count=i
                    max_length=x
print("Longest Palindrome substring within first string is:",s1[count:count+max_length])
l1=len(s1[count:count+max_length])
print("Length is:",l1)

#s2
matrix=[[0]*n2 for _ in range(n2)] #初始化n*n的二維0陣列
count=0
max_length=1 

for i in range(n2):
    matrix[i][i]=True

for i in range(n2-1):
    if s2[i]==s2[i+1]:
        matrix[i][i+1]=True
        count=i
        max_length=2
        
else:
    for x in range(3,n2+1):
        for i in range(n2-x+1): #i是起始索引
            j=i+x-1
            if s2[i]==s2[j] and matrix[i+1][j-1]:
                matrix[i][j]=True
                if x>max_length:
                    count=i
                    max_length=x
print("Longest Palindrome substring within first string is:",s2[count:count+max_length])
l2=len(s2[count:count+max_length])
print("Length is:",l2)

print("-----encryption completed-----")

#最後公視轉換
P=list(word)
asciiword=[ord(ele) for sub in P for ele in sub]
gogo = list(map(int,asciiword))
bang=[]
for z in gogo:
    z=int(z)
    y=z+a 
    yy=l1*y+l2 
    if yy>90:
        yy=(yy-65)%26+65
    elif yy<65:
        yy=(yy+65)%26+25
    else:
        yy=yy
    bang.append(yy)
string=''.join([chr(i) for i in bang])
print(string)
