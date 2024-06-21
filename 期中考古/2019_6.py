while True:
    x=int(input("Input a number(>1):"))
    if x<=1:
        print("try again!")
        continue
    break
count=3
a=0
b=1 
while True:
    a,b=b,(a+b)
    if x==b:
        print(count,"th")
        break
    elif x<b:
        print("not")
        break
    count+=1

n=2
number=0
while True:
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
            break
    if prime:
        number+=1
    if number==x:
        print(n)
        break
    n+=1