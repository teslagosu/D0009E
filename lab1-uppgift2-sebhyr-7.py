# k = P + (a+1)Pr/2
def kostnad(p,r,a):
    totalKostnad = p + (a + 1)*((p*r)/2)
    print("Den totala kostnaden efter",a,"år är",int(totalKostnad),"kr.")


