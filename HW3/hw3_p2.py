p=input("Input polynomial:").replace("-","+-").split("+")
x=int(input("Input the value of X:"))
if p[0]=='':
    p.remove('')

i=0 #判斷是否有次方 
while i<len(p):
    p[i]=p[i].split("^")
    i=i+1

sign=1 #0代表負號 若為1則正
result=0

i=0
while i<len(p):
    if len(p[i])==1:      #次方<=1
        if "-" in p[i][0]:
            sign=0
            p[i][0] = p[i][0].replace("-X", "X")
        if "X" not in p[i][0]: #代表是constant
            if sign==1:
                result+=int(p[i][0])
            else:
                result-=int(p[i][0])
        elif p[i][0].replace("X","")=="":
            if sign ==1:
                result+=x
            else:
                result-=x
        else:
            if p[i][0].replace("*","")=="XX":
                coef=x
                sign = 1
            elif "*X" in p[i][0]:
                coef=int(p[i][0].replace("*X",""))
            else:
                coef=1
            if sign==1:
                result+=coef*int(x) 
            else:
                result-=coef*int(x) 
    else: #次方>1
        if "-" in p[i][0]:
            sign=0
            p[i][0] = p[i][0].replace("-","")
        if p[i][0]=="X":
            coef=1
        else:
            coef=int(p[i][0].replace("*X",""))
        if p[i][1]=="X":
            power=x
        else:
            power=int(p[i][1])

        if sign==1 :
            result+=coef*int(x)**power
        else:
            result-=coef*int(x)**power
        sign=1
    i+=1
print("Evaluated Result:", result)
