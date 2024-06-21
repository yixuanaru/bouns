year=int(input("Please input Year:"))
month=int(input("Please input month:"))

basey,besem,based=1900,1,1 #星期1
days_in_m=[31,28,31,30,31,30,31,31,30,31,30,31]

passdays=0
sign=1
if year<basey:
    sign=-1

for y in range(basey,year,sign):
    if y%4==0 and (y%100!=0 or y%400==0):
        passdays+=366
    else:
        passdays+=365

for m in range(1,month):
    passdays+=sign*days_in_m[m-1]    
    if m==2 and year%4==0 and (year%100!=0 or year%400==0):
        passdays+=sign

weekday=(passdays+1)%7
weekdays=['Sun', 'Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat']
ans=weekdays[weekday]
print(ans)


for i in weekdays:
    print(i,end=" ")
print()

months=days_in_m[month-1]
if month==2 and year%4==0 and (year%100!=0 or year%400==0):
    months+=1
for v in range(1,weekday+1):
    print("    ",end="")
for j in range(1,months+1):
    if (v+j-1)%7==0:
        print()
    print("{0:02d}".format(j),end="  ")
