force=int(input("Input the force:"))
m1=int(input("Input the mass of m1:"))
dis=int(input("Input the distance:"))

m2=(force*dis*dis)/(m1*6.67e-11)
print("The mass of m2 =",m2)

energy=m2*(299792458)*(299792458)
print("The energy of m2 =",energy)
