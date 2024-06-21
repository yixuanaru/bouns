print("Welcome to the simple calculator program!")

while True:
    n1=float(input("Enter the first number:"))
    n2=float(input("Enter the second number:"))
    op=input("Select an arithmetic operation(+,-,*,/):")
    if op=="+":
            ans=n1+n2
    elif op=="-":
            ans=n1-n2
    elif op=="*":
            ans=n1*n2
    elif op=="/":
        if n2!=0:
            ans=n1/n2
        else:
            print("Division by zero!")
            continue
    print("Result",ans)

    while True:
        gogo=input("Do you want to perform another calculation? (yes or no):").lower()
        if gogo=="yes":
            while True:
                n1=float(input("Enter the first number:"))
                n2=float(input("Enter the second number:"))
                op=input("Select an arithmetic operation(+,-,*,/):")
                if op=="+":
                        ans=n1+n2
                elif op=="-":
                        ans=n1-n2
                elif op=="*":
                        ans=n1*n2
                elif op=="/":
                    if n2!=0:
                        ans=n1/n2
                    else:
                        print("Division by zero!")
                        continue
                print("Result",ans)
                break
        elif gogo=="no":
            print("Goodbye!")
            break
        else:
            continue
    break
