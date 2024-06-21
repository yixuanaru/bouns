#林宜萱B14111369統計115

'''n=int(input("Input an integer number:"))
a=0
b=1
for i in range(n):
    if n==0:
        a==0
    else:
        a,b=b,a+b
print(a,end=" ")
'''

n = int(input("Input an integer number:"))
a = 0
b = 1
i = 0
while i < n:
    if n == 0:
        a = 0
    else:
        a, b = b, a + b
    i += 1
print(a, end=" ")
