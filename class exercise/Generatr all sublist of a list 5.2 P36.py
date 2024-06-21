L=["a","b","c","d","e"]
i=0
while i<len(L):
    j=i+1
    while j<=len(L):
        print(L[i:j])
        j+=1
    i+=1
