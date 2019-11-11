#funktionen tvarsumman(n)
def tvarsumman(n):
    if n == 0:      #Om n är == 0, returnera 0
        print(n)
        return 0
    else:           #Annars, utför ekvationen på n
        print("n före ekvation:",n)
        n = n%10 + tvarsumman(n//10)    #Stegar neråt sen uppåt när den nått 0.        
        print("n efter ekvation: ",n)   #Ex: om n = 123. 0+1+2+3 = 6
    return n      #returnera n
            
#funktionen tvarsumman2(n)        
def tvarsumman2(n):
    result = 0          #Variabel result som är 0.
    while n > 0:        #Loop som körs sålänge n är större än 0
        result = result + n%10      #result + n%10 sparas i result
        print("result + n%10 = ",result)
        n = n // 10                 #n // 10 sparas i n
        print("n = n // 10 = ",n)
    return result       #returnera result som plussats på.
    
    

#tvarsumman2(123)
        

import sumTest
