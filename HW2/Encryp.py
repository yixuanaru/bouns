word=input("The plaintext to be encrypted:")
P=list(word)
#use loop+ord

asciiword=[ord(char) for char in P]
gogo = list(map(int,asciiword))
bang=[]
for z in gogo:
    z=int(z)
    y=z+10 
    yy=1*y+2 
    if yy>90:
        yy=(yy-65)%26+65
    elif yy<65:
        yy=(yy+65)%26+25
    bang.append(yy)

print(bang)
string=''.join([chr(i) for i in bang])
print(string)
