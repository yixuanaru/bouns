ninput=input("Enter a subsquence of numbers separated by whitespace:")
n=[int(num) for num in ninput.split()] #把使用者輸入的字串變成list的形式

dp = [1]*len(n)     #用動態規劃來寫。dp[i]代表以序列中的第i個數字結尾的最長遞增子序列的長度
                    #把dp陣列的所有元素初始化為1，因為每個數字本身就是長度為1的遞增子序列
prev = [-1]*len(n)  #初始化長度n的陣列prev,裡面全部都是-1。
                    #為了在重建最長遞增子序列時可以去找後面有沒有小於目前序列最大值

if len(n)<=1:       #如果數列的長度小於等於1
    print("The Longest increasing subsequence is:",n[0])  #輸出它自己

for i in range(1,len(n)): #從1開始是因為第一個元素已經有初始化過了
    for j in range(0,i):  #j用來循環找
        if n[i]>n[j] and dp[j]+1>dp[i]: #第一個條件是確認子序列是遞增的，第二個條件是確認子序列的長度 更新過的會更長
            dp[i]=dp[j]+1 #以n[i]結尾的子序列長度是n[j]對應的子序列長度+1
            prev[i]=j     #紀錄最長子序列中前一個元素的索引，之後要用它重新列出子序列
max_len=max(dp) #dp裡面的最大值代表這個數列的長度
result=[]       #用來儲存最後結果的空陣列
for i in range(len(n)-1,-1,-1): #從最後一個元素往前看
    if dp[i]==max_len:          #如果它是最長遞增子序列的一部分，就把它+到Result裡面
            result.append(n[i])
            max_len-=1          #把值加進去result的時候，整個子序列的長度要跟著減一
            i=prev[i]           #用prev去找剛剛已經找好的子序列的值的索引

print("The Longest increasing subsequence is:",result[::-1])  #因為是反向增加，所以本來最後的結果會是大到小，要把它改成小到大
