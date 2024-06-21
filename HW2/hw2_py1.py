s1="spam"
s2="ni!"

'''problem1
#a
print("The Knights who say,",s2) 
#b
print(s1*3+s2*2)
#c
c=s1[1]
print(c)
#d
d=s1[1:3]
print(d)
#e
e=s1[2]+s2[:2]
print(e)
#f
f=s1+s2[-1]
print(f)
#g
g=s2[len(s2)//2]
print(g)

problem2
#a
print(s2[0:2].upper())

#b
print(s2+s1+s2)

#c
print((s1.title()+s2.title()+' ')*3)

#d
print(s1.replace("m","n"))

#e
print(s1.replace("a",''))

'''
'''
#a
print("Looks like %s and %s for breakfast" %("spam", "eggs"))

#b
print("There is %d %s %d %s" % (1, "spam", 4, "you"))

#c
print("Hello %s %s" % ("Suzie", "Programmer"))

#d
print("%0.2f %0.2f" % (2.3, 2.3468))

#e
print("%7.5f %7.5f" % (2.3, 2.3468))

#f
print("Time left %02d:%05.2f" % (1, 37.374))

#g
print("%2d" %(14))
'''


phrase = "python" 
vowels = "aeiou" 
count = 0 
while (not phrase[count] in vowels): 
    count = count + 1 
print(count)
