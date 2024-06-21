v=int(input("Input velocity:"))
c=299792458
r=(((c*c)-(v*v))/c/c)**(-1/2)

p=v/(299792458)
print("Percentage of light speed =",p)

al=4.3/r
al=round(4.3/r,6)
print('Travel time to Alpha Centauri =',al)


bs=6.0/r
bs=round(6.0/r,6)
print("Travel time to  Barnard's Star=" ,bs)

be=309/r
be=round(309/r,6)
print('Travel time to Betelgeuse (in the Milky Way) =',be)

ag=2000000/r
ag=round(2000000/r,6)
print('Travel time to Andromeda Galaxy (closest galaxy) =',ag)



