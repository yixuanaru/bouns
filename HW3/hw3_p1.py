while True:
    n=int(input("Input the total number of students(n>0):"))
    if n>0:
        break
    else:
        continue

student=list(range(1,n+1))
#print(student)
count=0 
while len(student)>1:         #當列表中有多於1個學生時就一直循環
    i=0                       #索引0
    while i<len(student):
        count+=1
        if count%3==0:        #如果計數器可以被學生整除，那就把那個學生踢調，直到不能被三整除
            student.pop(i)
        else:
            i+=1
    
print("the last ID is :",student[0])

