def mult(v):
    i = 1
    while i < 10:
        j = 0
        while j < 3:
            print(v[j], "*", i, "=", v[j] * i, end='\t')
            j += 1
        #print()
        i += 1
    print()


i=0
vectors = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
while i<len(vectors):
    mult(vectors[i])
    i+=1


'''for v in vectors:
    mult(v)'''

