import random
def game():
    global p,d,deck
    ranks=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits=['-CLUB','-DIAMOND','-HEART','-SPADE',]
    deck=[]
    #洗牌
    for s in suits:
        for r in ranks:
            deck.append(r+s)
    random.shuffle(deck)
    #print(deck)

    d=[] #處存莊家手組
    p=[] #處存玩家手牌
    #發牌給莊家和玩家各兩張
    for i in range(2):
        dealer=deck.pop(0) #莊家的
        d.append(dealer)
        player=deck.pop(0) #玩家的
        p.append(player)



#計算手牌數字
def compute(hand):
    values={'A':11,'K':10,'Q':10,"J":10,'1':10} #A預設11 KQJ為10
    sum=0 #加總初始化
    ace=0 #計算抽到幾張A
    for card in hand:              #這個迴圈要用來加總手牌數自
            rank = card[0:1]       #rank的部分 不包含花色 
            if rank in values:  
                sum+=values[rank]
            else:
                sum+=int(rank)     #不適AKQJ就直接加他們的數字
            if rank=='A':          
                ace+=1             
    while sum > 21 and ace > 0:    #如果手牌數值超過21而且至少有1張A
        sum-= 10  #把A的值判斷成1(11-10=1)
        ace-= 1   #把ace手牌數輛-1，因為已經把一個看作1了
    return sum
#print(compute(d))


while True:
    game()
    pvalue=compute(p) #輸出玩家目前手牌及手牌數值
    print(f"Your current value is {pvalue}\nwith the hand: {', '.join(p)}") 

    while pvalue < 21: #如果玩家手牌數字<21
        print()
        choice=input("hit or stay? (hit=1,stay=0): ") #要步要繼續玩
        if choice=='1':
            #print(deck.pop(0)) 新抽到ㄉ牌                              
            new_card=deck.pop(0)                      
            p.append(new_card)
            print(f"You draw {new_card}\n")
            pvalue=compute(p)
            if pvalue==21:
                print(f"Your current value is Blackjack! ({pvalue})\nwith the hand: {', '.join(p)}")
            else:
                print(f"Your current value is {pvalue}\nwith the hand: {', '.join(p)}")
        
        elif choice=="0":
            break
        else:
            print("try again")
    if pvalue > 21:
        print()
        print("*** Dealer wins! ***")
    else : #莊家的回合    
        dvalue=compute(d)
        print(f"\nDealer's current value is {dvalue}\nwith the hand: {', '.join(d)}\n")
        while dvalue < 17:
            new_card = deck.pop(0)
            d.append(new_card)
            print(f"Dealer draws {new_card}\n")
            dvalue = compute(d)
            print(f"Dealer's current value is {dvalue}\nwith the hand: {', '.join(d)}\n")

        if dvalue > 21:
            print("Dealer's current value is Bust! (>21)")
            print(f"with the hand: {', '.join(d)}\n")
            print("*** You beat the dealer! ***")
        elif dvalue > pvalue:
            print("*** Dealer wins! ***")
        elif dvalue < pvalue:
            print("*** You beat the dealer! ***")
        else:
            print("*** You tied the dealer, nobody wins. ***")
    again=True
    a=input("\nWant to play again? (y/n): ")
    if a!="y":
        again=False
        break
    else:
        again=True
