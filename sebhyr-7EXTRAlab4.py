#klassen phonebook
class phonebook:
    #variabel dictList som är en dictionary
    dictList = {}
    #konstruktor
    def __init__(self,name):
        self.name = name
        
    #metoden add som lägger till en ny person i dictionaryn
    def add(self,name,number):
        p = phonebook(name) #skapa ett objekt av klassen
        if number in self.dictList: #om det inslagna nummret finns i dictionaryn
            print("nummret finns redan")    #skriv ut att det redan finns.
        else:   #annars
            self.dictList[number] = [p] #lägg till argumenten number som key och objektet p i en list i en dict
            print("Ny person sparad")#skriv ut att ny person är sparad
            
    #metoden lookup för att kolla om
    def lookup(self,name):
        self.checkIfNameExist(name)#kollar om namnet finns
        if self.checkIfNameExist(name) == None: #om det inte finns skriv ut att det inte finns
            print("finns ingen med det namnet.")
        else:
            self.getNumberFromName(name) #annars skriv ut nummrerna som finns på det sökta namnet
            
        
        
            
            
            
    #metoden alias skapar ett alias av ett befintligt namn
    def alias(self,name,newName,number = None):
        self.checkIfNameExist(name)#kolla om namnet finns 
        if self.checkIfNameExist(name) == None:#om det inte finns, skriv ut felmeddelande
            print("telebok> finns ingen med det namnet")
        else:#annars
            self.isNameMoreThenOne(name)    #kolla om fler än en heter samma
            if self.isNameMoreThenOne(name) == 1: #om bara en person har det namnet
                number = self.returnNumberFromName(name)#hämta nummret från personen
                name = newName #sätt namn till det nya aliaset
                p = phonebook(name) # skapa ett objekt av klassen phonebook
                #save object with append
                self.dictList[number].append(p)
                print("telebok> nytt alias skapat")
            elif self.isNameMoreThenOne(name) > 1: #annars om det finns fler än en som har det namnet
                if number:#om nummer == true
                    name = newName #namn blir det nya aliaset
                    p = phonebook(name)#skapa ny instans av phonebook
                    self.dictList[number].append(p)#lägg till namnet i listan inuti dict
                    print("telebok> nytt alias har skapats")
                else:
                    print("Det finns flera med samma namn, skriv in numret")#om number == None
                    
    #metoden change som ändrar ett nummer till ett annat
    def change(self,name,number,oldNumber=None):
        self.checkIfNameExist(name)#kolla om namnet finns
        if self.checkIfNameExist(name) == None:#om namnet inte finns
            print("telebok> finns inget med det namnet")#printa att det inte finns
        else:#annars
            self.isNameMoreThenOne(name)#kolla om namnet finns på flera personer
            if self.isNameMoreThenOne(name) == 1:#om namnet bara finns på en
                if number in self.dictList:#om nummret finns redan, skriv ut felmeddelande
                    print("telebok> nummret finns redan.. försök igen..")
                else:
                    p = phonebook(name) #skapa instans av phonebook
                    oldNumber = self.returnNumberFromName(name)#hämta det gamla nummret
                    self.dictList[number] = self.dictList[oldNumber] #gör en kopia av innehållet i det gamla nummret
                    del self.dictList[oldNumber] #radera det gamla nummret med tillhörande namn/alias
                    print("nummret har ändrats.")
            if self.isNameMoreThenOne(name) > 1: #om flera heter likadant
                if oldNumber:#om oldnummer är inskrivet
                    self.dictList[number] = self.dictList[oldNumber]#gör en kopia av det gamla numrets innehåll till det nya
                    del self.dictList[oldNumber]#radera keyn med gamla nummret och innehåll
                    print("nummret har ändrats")
                else:   #felmeddelande om det finns flera med samma namn och gamla nummret inte är inskrivet
                    print("det finns flera personer med samma namn, skriv in numret")
            
                    
    #tabort funktion som tar bort nummer och alla namn som hör till
    def remove(self,name,number=None):
        self.checkIfNameExist(name) #kolla om namnet finns
        if self.checkIfNameExist(name) == None:#om det inte finns skriv ut felmeddelande
            print("telebok> Det finns ingen med det namnet")
        else:
            self.isNameMoreThenOne(name)#kolla om flera heter likadant
            #if self.isNameMoreThenOne(name) == None:
                #print("Finns ingen med det nummret")
            if self.isNameMoreThenOne(name) == 1:   #kolla om bara en har namnet
                number = self.returnNumberFromName(name)#hämta nummret
                del self.dictList[number]#radera key med tillhörande values
                print("Nummer: " +number+" har raderats")
            elif self.isNameMoreThenOne(name) > 1:#om det finns flera som heter likadant
                if number:#om nummret är inskrivet av användaren
                    del self.dictList[number]#radera key med tillhörande values
                    print("Nummer: " +number+" har raderats")
                else:#skriv ut felmeddelande om det finns flera personer med samma namn och ett nummer är inte inskrivet
                    print("Fler än en person har det här namnet, mata in nummer")
    #metod som sparar datan från dictionaryn till en textfil
    def save(self,filename):
        f = open(filename,"w")#öppna filen i writemode
        for number in self.dictList:#för varje nummer(key) i dictionaryn
            printNumber = (str(number + ";"))#bestämmer vad som är nummer
            f.write(printNumber)#skriv ut nummer till filen
            keys = self.dictList[number]#sätt keys till dict keys
            for name in keys:#för varje namn i objekten som finns i listan inne i dict dict
                printName = str(name.name + ";")#bestämmer vad som är namn
                print(printName)
                f.write(printName)#skriv ut namnen till filen
            f.write("\n")#hoppa till ny rad när det är slut objekt i en lista
        f.close()#stäng filen

    #metoden load som laddar upp data från en fil in i dictionaryn
    def load(self,filename):
        self.dictList = {}  #gör dictionaryn tom
        f = open(filename,"r")#öppnar upp filen i readmode
        for readLine in f:  #för varje linje i filen
            readLine = readLine.split(";")#splitta orden till strings.
            number = readLine[0]#nummer är på index 0
            #skapa en dictionary innehållande phonebook objekt i en lista för varje namn mellan index 1 till sista index
            self.dictList[number] = [phonebook(name) for name in readLine[1:-1]]
        f.close()#stäng filen
        
    #metod som returnerar nummret av ett namn       
    def returnNumberFromName(self,name):
        for x in self.dictList:
            for y in self.dictList[x]:
                if name in y.name:
                    return x
            

           
                
    #testfunktion
    def s(self):
        for x in self.dictList:
            for y in self.dictList[x]:
                print(x,y.name)
        

    #printa ut nummer som till hör ett namn    
    def getNumberFromName(self,name):
        for x in self.dictList:
                lista = self.dictList[x]
                for y in lista:
                    if name == y.name:
                        print(x)
    

        
    #kolla hur många som har ett namn   
    def isNameMoreThenOne(self,name):
        nameCount = []
        for x in self.dictList:
            key = self.dictList[x]
            for y in key:
                if name == y.name:
                    nameCount.append(y.name)
        return len(nameCount)
            
    #test funktion(används ej)
    def printKeyForNames(self,name):
        keyList = []
        for x in self.dictList:
            key = self.dictList[x]
            for y in key:
                if name == y.name:
                    print(y.name)
                    keyList.append(x)
        for i in keyList:
            print("telebok> "+i)

     #kolla om ett namn existerar i dictionaryn       
    def checkIfNameExist(self,name):
        nameList = []
        for x in self.dictList:
            key = self.dictList[x]
            for y in key:
                if name in y.name:
                    return True
        
    #test funktion
    def t(self):
        for x in self.dictList:
            key = x
            lista = self.dictList[x]
            for y in lista:
                    print(x,y.name)
                    
name = ""
number = ""
##
p = phonebook(name)
running = True
while running:
    userInput = input("telebok>").split()#splitta upp ord och ta bort whitespaces
    
    try:#försök köra dessa kommandon
        if userInput[0] == "add":#om add: sätt index1 som variabel och sätt  allt annat från index2 som variabler med i funktionen
            p.add(userInput[1],(*userInput[2:]))
        elif userInput[0] == "lookup":#annars om lookup: sätt index1 som variabel i funktionen
            p.lookup(userInput[1])
        elif userInput[0] == "alias":#-||-
            p.alias(userInput[1],(*userInput[2:]))#-||-
        elif userInput[0] == "change":
            p.change(userInput[1],(*userInput[2:]))#-||-
        elif userInput[0] == "remove":
            p.remove(userInput[1],(*userInput[2:]))#-||-
        elif userInput[0] == "save":
            p.save(userInput[1])#-||-
        elif userInput[0] == "load":
            p.load(userInput[1])#-||-
        elif userInput[0] == "quit":
            raise SystemExit()#avsluta
        else:
            print("ogiltig syntax")
            
    except TypeError:#fånga upp om användaren skrivit in fel antal argument
        print("Fel inmatning av argument")
    except KeyError:#fånga upp om användaren skrivit in fel nummer(key)
        print("kontrollera att du skrivit in rätt nummer")
    except IndexError:#ifall något index error från listan skulle komma up
        print("ogiltigt val")

#kvar att göra:
#kommentera
    
                      
