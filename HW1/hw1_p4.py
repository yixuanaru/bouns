h1=int(input("Input the height of the 1st ball:"))
m1=int(input("Input the mass of the 1st ball:"))
m2=int(input("Input the mass of the 2nd ball:"))

g=9.8

u1=(2*g*h1)**(1/2)
v2=((2*m1)/(m1+m2))*u1


print("The velocity of the 1st ball after slide:",u1,"m/s")
print("The velocity of the 1st ball after slide:",v2,"m/s")
