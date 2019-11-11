#Funktionen bounce(n)
def bounce(n):
    if n == 0:      #Kollar om n = 0, skriver isåfall ut n.
        print(n)
        
        
    else:           #Om inte n = 0, skriver den ut n.
        print(n)
        bounce(n-1) #Går sedan in i funktionen bounce(n-1) som subtraherar 1 från n
        print(n)    #går ur subtraheringen automatiskt och skriver ut n i spegelvänt format.
    
    
#Funktionen bounce2(n)
def bounce2(n):
    for x in range(n ,-n-1 ,-1): #for-loop som kollar x, i n spannet mellan (start: n, stop: -n-1,steg: -1)
        print(abs(x))            #Skriver ut det absoluta värdet av x, gör negativt värde till positivt.


#test av bounce(n) funktionen
def x(n):
    print(n)
    bounce(n-1)
    print(n)


#x(0)
import bounceTest
