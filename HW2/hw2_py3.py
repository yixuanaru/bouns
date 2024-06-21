#林宜萱B14111369統計115

year=int(input("Please input Year:")) #輸入年
month=int(input("Please input month:")) #輸入月
basey,besem,based=1900,1,1 #以1900年1月1日星期一為基準年月日
days_in_m=[31,28,31,30,31,30,31,31,30,31,30,31] #平年1~12月的天數

passdays=0  #設passdays為自基準年經過的總天數
sign=1 #7~9行:如果輸入年小於基準年的話需要變號往回扣，所以用sign當作一個f(x)的概念
if year<basey:
    sign=-1
for y in range(basey,year,sign):  #11~15行:用for圈 變數y計算從基準年到輸入年之間經過的總天數，目標將年份從基準年調整成跟輸入年一樣
    if y%4==0 and (y%100!=0 or y%400==0): #閏年的定義是四年和四百年潤，但是百年不潤
        passdays+=366 #如果基準年到輸入年之間遇到閏年等於經過366天
    else:
        passdays+=365 #如果基準年到輸入年之間遇到平年等於經過365天
       
        
for m in range(1,month): #17~20行:目標用for迴圈讓m從1月(基準月)開始跑到輸入月的1號(所以不能加輸入的那個月的天數) m就是幾月的意思
    passdays+=sign*days_in_m[m-1]    #加減跑到輸入月前所有月份的天數
    if m==2 and year%4==0 and (year%100!=0 or year%400==0): #要注意如果是閏年的時候二月要再加一天變成29天
        passdays+=sign
#解決完年跟月要來解決到底輸入月的1號在禮拜幾了
weekday=(passdays+1)%7  #把所有的天數拿去除以七看會餘多少，這邊passdays+1是因為要把星期一設定成index的1號位置然後讓星期天是餘0的比較符合直覺
weekdays=['Sun', 'Mon', 'Tue','Wed', 'Thu', 'Fri', 'Sat'] #星期一到星期日字串
ans=weekdays[weekday] #ans是我終於算出來輸入月的1號在禮拜幾
#print(ans) 這一行我是來幫助自己確認最後的月曆有沒有出問題

#以下開始輸出月曆格式
for i in weekdays:  #27~29行:目標把星期一到星期日的字串print出來
    print(i,end=" ")
print() #換行後輸出每個月的日期

months=days_in_m[month-1] #months是用來找出輸入月在平年的時候會有幾天，也是用index的概念去找，而month-1是因為index要從零開始
if month==2 and year%4==0 and (year%100!=0 or year%400==0): #如果是閏年的話2月就會有29天，所以我把months+1天
    months+=1
#解決完需要輸出的數字到多少以後就要來把數字對齊格式了

for v in range(1,weekday+1):  #讓v去跑在01號開始前我都要保留空格
    print("    ",end="") #對齊格式四個字元
for j in range(1,months+1): #讓j去跑我這個月有幾天要，也就是輸出的日期們
    if (v+j-1)%7==0:       #禮拜六之後就要換行，所以空格跟日期加起來不能超過七，這邊會-1是因為這樣會剩六個數字，我需要保留七天，也就是第八格的時候換行
       print()            #換到下一行
    print("{0:02d}".format(j),end="  ") #把所有數字都調整呈二位數
