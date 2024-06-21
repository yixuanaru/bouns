#難產
n=input("input sequence of seats:").split(" ")
if len(n)<3:        #至少需要三個石頭才能存水
    print("water:0")
    exit()

i=0  #算跟左邊石頭幾顆
j=len(n)-1  #算右邊石頭幾顆
lmax=n[i] #用來計目前的石頭最多幾顆
rmax=n[j]
water=0 #算水多少
while i<j: #每次都會比較左右兩邊石頭的高度
    if int(lmax)<int(rmax): #左邊矮
        lmax=max(int(n[i]),int(lmax)) #更新左邊石頭的高度
        water+=int(lmax)-int(n[i]) #水量等於石頭高度-旁邊比她小的石頭的高度
        i+=1
    else: #如果又邊矮
        rmax=max(int(n[j]),int(rmax)) #更新右邊石頭高度((最高
        water+=int(rmax)-int(n[j]) #水等於右邊石頭跟現在高度ㄉ查差值
        j-=1
print(f"water:{water}")



