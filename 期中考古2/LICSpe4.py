n=input("Enter a sequence of integers separated by whitespace:").split(" ") #輸入陣列
#n=[int(num) for num in ]
n=list(map(int,n))
temp_LICS=[n[0]]
LICS=[] #最後的結果


for ele in n[1:]:
    if ele>temp_LICS[-1]:
        temp_LICS.append(ele)
    else:
        if len(temp_LICS)>len(LICS):
            LICS=temp_LICS
            temp_LICS=[ele]

if len(temp_LICS)>len(LICS):
    LICS=temp_LICS

print("Length:",len(LICS))  #輸出最大數字
print("LICS:",LICS)   #我想要輸出到最大數前的那個等差數列


