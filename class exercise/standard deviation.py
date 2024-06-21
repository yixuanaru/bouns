#standard deviation

v=[82,74,80,78,86]
mean=sum(v)/len(v)

i=0
y=0
for i in range(len(v)):
    a=(v[i]-mean)**2
    y+=a
    i+=1
SD=(y/(len(v)-1)**0.5)
print("SD= %0.2f " % SD)