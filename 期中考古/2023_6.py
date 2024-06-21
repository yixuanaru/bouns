while True:
    t=input("Enter a time(h:m:s):")
    h,m,s=t.split(':')
    if 0<=int(h)<=23 and 0<=int(m)<=59 and 0<=int(s)<=59:
        seconds=int(h)*3600+int(m)*60+int(s)
        print(seconds)
        break
    else:
        print("Invalid time format. Please try again.")
