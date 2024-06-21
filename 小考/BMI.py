tomh,tomw,toma=1.8,120,50

def BMI(h,w):
    bmi=w/(h**2)
    return bmi

def risk(bmi,age):
    table=[["medium",'high'],['low','medium']]
    young=age<45
    heavy=bmi>=22.0
    risk=table[young][heavy]
    return risk

tombmi=BMI(tomh,tomw)
print("Tom: BMI=%.2f,Risk=%s"%(tombmi,risk(tombmi,toma)))