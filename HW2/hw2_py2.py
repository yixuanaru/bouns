#林宜萱B14111369統計115

n=int(input("input the range number:")) #user輸入n值
print("Perfect numbers:") #輸出一句話

if n<2:                   #假如n小於2則告知使用者n必須大於2
    print("n>2")
    
else: #n<2以外的情況
    
    for num in range(2,n+1):   #for迴圈num的範圍從2~n(打n+1)，尋找範圍內的完美數有哪些
        sum=0                  #此時加總值為0
        for i in range(1,num): #for迴圈i值從1到num，要用來找某數除了自己外所有因數之和剛好等於某數的情況，從1開始慢慢找有哪些是num的因數
            if num%i==0:       #找num的因數=>可整除者
                sum+=i         #找到num的因數之後把這些因數加總起來
        if sum==num:           #如果加總到num之前的值恰好等於num時，滿足perfect number的條件
            print(sum,end=" ")         #輸出在range(2,n+1)之間的完美數!
