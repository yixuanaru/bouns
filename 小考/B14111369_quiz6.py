import random
def inter(n):     #這個function是最後要用來計算猜測的字母在直方圖裡出現幾次的
    if abc[0]<=n<=abc[3]:    #依照區間，如果猜測的字母在那個區間裡面，次數就加1
        interval['a-d']+=1
    elif abc[4]<=n<=abc[7]:
        interval['e-h']+=1
    elif abc[8]<=n<=abc[11]:
        interval['i-l']+=1
    elif abc[12]<=n<=abc[15]:
        interval['m-p']+=1
    elif abc[16]<=n<=abc[19]:
        interval['q-t']+=1
    elif abc[20]<=n<=abc[23]:
        interval['u-x']+=1
    elif abc[23]<=n<=abc[25]:
        interval['y-z']+=1

abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
answer=random.choice(abc) #abc矩陣放26個英文字母，從裡面隨機抽一個當這次遊戲的答案
#print(answer) 
interval={"a-d":0,"e-h":0,"i-l":0,"m-p":0,"q-t":0,"u-x":0,"y-z":0} #這是我用來當直方圖的表格初始化 會透過def inter來變更裡面的數字
times=0 #猜幾次
while True: 
    global n 
    n=input("Guess the lowercase alphabet: ") 
    if n not in abc: #如果n不是小寫字母舅請重新輸入，而且次數要減一才不會多算
        print("please enter a lowercase alphabet: ")
        times-=1
    else: #判斷n大小並給出相應的回覆
        if n<answer: 
            print("The alphabet you are looking for is alphabetically higer: ")
            inter(n) #計算猜測字母出現次數
        elif n>answer:
            print("The alphabet you are looking for is alphabetically lower: ")
            inter(n)
        else:
            times+=1
            print(f"Congratulations! you gussed the alphabet \" {answer} \" in {times} tires ")
            inter(n)
            break
    times+=1 #計算總共猜幾次

print()
print("Guess Histogram: ") 
#print(interval)
for key,value in interval.items():  #用字典把interval裡面的東西一個一個取出來
    print(key,":",int(value)*"*")   #出現幾次就乘以幾次* 把數字換成*表示

