
#klassen telephonebook
class Telephonebook:

    #konstruktorn
    def __init__(self):
        self.telephoneDictionary = {}   #tom dictionary
        

        
    #funktionen add som tar två argument: name och number
    def add(self,name,number):
        
        self.findName(name)     #söker efter namnet.
        if self.findName(name) == True: #om namnet finns i dictionaryn
            print("namnet finns redan i telefonboken")  #printa ut att det finns
        
        else:       #annars forsätt med att söka rätt på nummer..
            self.findNumber(number)     #kolla om nummret finns.
            if self.findNumber(number) == True: #om nummret redan finns
                print("nummret finns redan")    #printa ut att det redan finns..
            else:
                k = self.telephoneDictionary[name] = number #spara namn som key, och nummer som value i dictionaryn.
                print("Sparat")
                #print(self.telephoneDictionary)
                #print(k)
        
    #funktionen lookup som letar upp personen man söker på.
    def lookup(self,name):
        self.findName(name)
        if self.findName(name) == False:
            print("Det finns inget nummer tillhörande "+name)
        else:
            self.getNumber(name) #hämtar nummret.

    #funktionen getNumber som söker igenom dictionaryn        
    def getNumber(self,name):
        for x,y in self.telephoneDictionary.items(): #för varje x,y i dict.
            if name in x:
                print(y)    
                return y
            
            
    def findNumber(self,number):
        for x,y in self.telephoneDictionary.items():
            if number in y:
                return True
        return False
    
    #funktionen findName kollar om namnet finns som key i dict.        
    def findName(self,name):
        for x in self.telephoneDictionary.items():
            if name in x:
                return True
        return False

    
    #testfunktion
    def showAll(self,name):
        for x in self.telephoneDictionary.items():
            print(x)
            print(type(x))
            print(self.telephoneDictionary.items())
            print(type(self.telephoneDictionary.items()))
        
            
    #tarbort alla mellanslag och gör om dem till en tomsträng.
    def removeWhiteSpaces(self,name):
        r = name
        n = r.replace(" ","")
        return n
    
    #funktion som sparar all data i dictionaryn till en fil.        
    def saveToFile(self, filename):
        f = open(filename,"w")
        for name,number in self.telephoneDictionary.items():
            newItem = number+";"+name+ ";"+"\n"
            f.write(newItem)
        print(filename + "är nu sparat")
        f.close()
            
    #funktion som laddar data in till dictionaryn.        
    def loadFromFile(self,filename):
        #self.telephoneDictionary.clear() #rensar nuvarande dictionary.
        #print("inne i load")

        f = open(filename,"r")
        for line in f:
            line = line.split(";")  #tarbort ; och ersätter det med en tom sträng
            name = line[1]  #den andra strängen på raden blir name
            number = line[0]    #den första strängen på raden blir number
            self.telephoneDictionary[name] = number #lägger till namn som key och number som value.
            
        #print(self.telephoneDictionary)
        print("Data från "+filename+" har nu laddats upp!")    
        f.close()
            
    #funktionen alias lägger till ett alias på ett befintligt namn.        
    def alias(self,name,newName):
        self.findName(name) #går in i funktionen och söker efternamnet.
        if self.findName(name) == False:    #om funktionen returnerar false så printar den ut att namnet inte finns.
            print("namnet finns inte")

        else: #annars..
            number = self.getNumber(name) #hämtar nummret för personen som fanns.
            self.telephoneDictionary[newName] = number #lägger till en ny person(alias) i dictionaryn med samma nummer som personen man skrev in namnet på.
            #print(self.telephoneDictionary.items())
            
    #funktionen change som ändrar ett namn till ett nytt.
    def change(self,name,number):
        self.findName(name)
        if self.findName(name) == False:
            print("finns ingen med det namnet")
        
        else:
            self.findNumber(number)
            if self.findNumber(number) == True:
                print("nummret finns redan")
            else:     
                self.updateNumber(name,number) #går in i funktionen som uppdaterar nummret.
                #print(self.telephoneDictionary)
                print("nummret har ändrats")

    def updateNumber(self, name,number):
        newNumber = number #deklararer newNumber som number.
        currentNumber = self.getNumber(name) #hämtar nummret
        for name, number in self.telephoneDictionary.items(): #för varje namn,nummer i dict.
            if number == currentNumber: #om nummret är samma som nummret som finns i dict.
                self.telephoneDictionary[name] = newNumber #ändra keyn till nya nummret.

    
            
        
                  
            
t = Telephonebook() #skapar ett objekt av klassen telephonebook.

running = True

while running:
            
    
    
            userInput = input("telebok>") #ändrar prompt istället för standard >>>
            rw = userInput.split()

            try:
                
                if userInput.split()[0] == "add": #om första ordet är "add"
                    try:
                        t.add(t.removeWhiteSpaces(rw[1]),t.removeWhiteSpaces(rw[2]))
                    except IndexError:
                            print("kontrollera att du skrivit in namn och nummer")

                            
                elif userInput.split()[0] == "lookup": #om första ordet är lookup
                    try:
                        t.lookup(userInput.split()[1])
                    except IndexError:
                            print("kontrollera att du skrivit in namn")

                    
                elif userInput.split()[0] == "alias": #om första ordet är alias
                    try:
                        t.alias(t.removeWhiteSpaces(rw[1]),t.removeWhiteSpaces(rw[2]))
                    except IndexError:
                        print("kontrollera att du skrivit in namn och alias")

                elif userInput.split()[0] == "change": #om första ordet är change
                    try:
                        t.change(t.removeWhiteSpaces(rw[1]),t.removeWhiteSpaces(rw[2]))
                    except IndexError:
                        print("kontrollera att du skrivit in 'namn' och 'nytt namn'")


                elif userInput.split()[0] == "save": # om första ordet är save
                    try:
                        t.saveToFile(t.removeWhiteSpaces(rw[1]))
                    except IndexError:
                        print("kontrollera att du skrivit in ett filnamn") #gå in i funktionen savetofie med filnamnet från andra ordet
                    
                elif userInput.split()[0] == "load": #om första ordet är load
                    try:
                        t.loadFromFile(t.removeWhiteSpaces(rw[1])) #gå in i funktionen loadfromfie med filnamnet från andra ordet
                    except:
                        print("kontrollera att du skrivit in ett filnamn")

                elif userInput.split()[0] == "quit": # om första ordet är quit
                    print("Avslutar programmet...")
                    running = False
                    
            
            except:
                print("**Kommandon**")
                print("'add [namn] [nummer]' för att lägga till en ny person i telefonboken")
                print("'lookup [namn]' för att leta upp en person i telefonboken")
                print("'alias [namn] [nytt namn]' för att lägga till ett alias")
                print("'change [namn] [nummer]' för att ändra nummer på en person inkl alias")
                print("'save [filnamn]' sparar telefonboken till en fil.")
                print("'load [filnamn]' laddar in sparade nummer in i programmet.")
                print("'quit' Avslutar programmet")

            
            
                      

                            
                
####Kvar att göra:

####
