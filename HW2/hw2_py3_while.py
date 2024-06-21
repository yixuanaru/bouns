year=int(input("Please input Year:"))  
month=int(input("Please input month:"))  
basey,besem,based=1900,1,1  
dayyy=[31,28,31,30,31,30,31,31,30,31,30,31]  

passdays=0  
sign=1  
if year<basey:
    sign=-1

y=basey
while y!=year:
    if y%4==0 and (y%100!=0 or y%400==0):
        passdays+=366
    else:
        passdays+=365
    y+=sign

m=besem
while m<month:
    passdays+=sign*dayyy[m-1]
    if m==2 and year%4==0 and (year%100!=0 or year%400==0):
        passdays+=sign
    m+=1

weekday=(passdays+1)%7  
weekdays=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
ans=weekdays[weekday]

for i in weekdays:
    print(i,end=" ")
print() 

months=dayyy[month-1]  
if month==2 and year%4==0 and (year%100!=0 or year%400==0): 
    months+=1

for v in range(1,weekday+1):  
    print("    ", end="")  

j=1
while j<=months:
    if (v+j-1)%7==0:
        print()
    print("{0:02d}".format(j),end="  ")
    j+=1
