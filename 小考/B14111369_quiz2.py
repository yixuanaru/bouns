a1=int(input("Enter the shopping amount:")) #用a1變數當作消費金額
a2=input("Enter the membership level(Regular or Gold):") #用a2變數當作會員等級

if a2=="Regular":
    if 1000>a1:
        print(a2,"$",a1)
    elif 2000>=a1>1000: 
        a1=a1*0.9
        print(a2,"$",a1)
    elif 3000>=a1>2000:
        a1=a1*0.85
        print(a2,"$",a1)
    elif a1>3000:
        a1=a1*0.8
        print(a2,"$",a1)
elif a2=="Gold":
    if 1000>a1:
        print(a2,"$",a1)
    elif 2000>=a1>1000:
        a1=a1*0.85
        print(a2,"$",a1)
    elif 3000>=a1>2000:
        a1=a1*0.8
        print(a2,"$",a1)
    elif a1>3000:
        a1=a1*0.75
        print(a2,"$",a1)
else:
    print("Invalid member level")
