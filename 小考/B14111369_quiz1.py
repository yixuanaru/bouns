s=float(input("Please input a Richter scale value:")) #令變數s為使用者輸入的小數格式(float)的芮氏規模
print("Richter scale value:",s) #輸出Richter scale value

J=10**((1.5*s)+4.8) #令變數J表示Richter scale value等於多少焦耳，套用公式算出

T=J/(4.184e+9) #令變數T表示J焦耳等於多少噸TNT，換算一下，4.184*10的9次方用科學記號表示

L=J/2930200 #令變數L表示J焦耳等於多少份營養午餐，換算一下，一頓等於2930200焦耳，J焦耳會有幾頓
 
print("Equivalence in Joules:",J) #輸出結果Richter scale value等於多少焦耳
print("Equivalence in tons of TNT:",T) #輸出結果Richter scale value等於多少噸TNT
print("Equivalence in the number of nutritious lunches:",L) #輸出結果Richter scale value等於多少份營養午餐
