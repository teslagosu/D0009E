#funktionen derivative
def derivative(f,x,h):
    derivate = (1/(2*h))*(f(x+h)-f(x-h)) #räkna ut derivatan.
    return float(derivate)               #returnera den uträknade derivatan

#testfunktion 1: x^4
def f1(x):
    return (x**4)
#testfunktion 2: x^2+x^4
def f2(x):
    return (x**2+x**4)
#testfunktion 3: x^4-5-x^2+5
def f3(x):
    return (x**4)-5-(x**2)+5

#funktionen solve: f = funktionen, x0 = startvärde, h = marginalen
def solve(f,x0,h):
    print("x0 Före while = ",x0)
        #sätter ett värde på previousNumber för att kunna köra loopen
    previousNumber =  1 
        #abs för att x0-previous inte ska bli negativt.
        # loopa tills x0-previous inte är större än h.
    while abs(x0 - previousNumber) > h:
            #sätter previousNumber till x0
        previousNumber = x0
        print("x0 = ",x0)
            #Beräknar x0-(f(x0)/derivative(f,x0,h))
            #Om f(10) = 10-(f(10)/derivative(f,10,h)) = ett steg närmare slutet.
            #T.ex. f(10) ger ett resultat nära 5. f(5) ger ett resultat nära 2.6 osv.
        x0 = x0 -(f(x0)/derivative(f,x0,h))
    print("slutresultat",x0)
    return float(x0) #returnera x0 i ett floatvärde.


#testfunktion x^2-1 ska bli nära 1
def testSolve1(x):
    return (x**2)-1

#testfunktion 2^x-1
def testSolve2(x):
    return(2**x)-1

#testfunktion x^3 + 1 - 2^x ska bli nära 0.7
def testSolve3(x):
    return (2*(x**2))-1

#testfunktion för x-e^-x = 0
#def testSolve4(x):
    #return x-

    
#solve(testSolve3,2,0.0001)
solve(testSolve1,10,0.1)

#import solveTest
        


    
