#Instansvariabler
wordsList = []  #en lista
descriptionsList = []   #en till lista
wordTuple = () #en tom tuple
wordList = []  #en tom list som tuplerna ska ligga i.
dictionaryMap = {} #en tom dictionary


#Printar ut start menyn.
def printStartMenu():
    print("1.List")
    print("2.Tuple")
    print("3.Dictionary")
    print("4.Exit program")

#kör menyn och tar inputs.
def runStart():
    running = True
    printStartMenu()
    #Så länge running = True kör loopen
    while running:
        choice = input("Choose alternative: ") #användarens val
        if choice == "1":   #kollar om valet == 1
            runMenuForLists()
        elif choice == "2": #kollar om valet == 2
            runMenu()               #kör tuplefunktionen
        elif choice == "3": #kollar om valet == 3
            runMenuDictionary()     #kör dictionaryfunktionen
        elif choice == "4": #kollar om valet == 4
            break #hoppa ur loopen
        else:               #om inget av ovanstående alternativ               
            printStartMenu()                           #visa start menyn igen
            print("Choose a valid option between 1-4") #printa ut ett felmeddelande
            

            
#printar menyn.
def printMenu():
    print("*" * 80)
    print("1. Insert: ")
    print("2. Lookup: ")
    print("3. Exit program")
    print("*" * 80)

#------------------------List--------------------------------------------------

#funktionen runMenuFromLists() som kör menyn.
def runMenuForLists():
    running = True
    printMenu()     #printar ut menyn
    while running:      #loopar menyn
        userInput = input("Choose alternative: ")   #tar input från användaren
        if userInput == "1":
            insertForLists()    #om input är 1 så kör insert funktionen
            printMenu()         #printa ut menyn igen.
        elif userInput == "2":
            lookupWordInList()  #om input är 2 så kör lookup funktionen
            printMenu()         #printa ut menyn igen.
        elif userInput == "3":
            raise SystemExit
        else:
            print("\n")     #om användaren matar in ett ogiltigt val, skriv ut felmeddelande
            print("Ett fel uppstod, försök igen!") 
            print("\n")
            printMenu()

#funktion för att lägga till nya ord och beskrivningar
def insertForLists():
    newWordInput = input("Word to insert: ") #input från användare
    searchForWordInList(newWordInput)       #kolla om ordet redan finns.
    if searchForWordInList(newWordInput) == True: #om searchForWordInList(word) funktionen returnerar true, printa ut ett felmeddelande.
        print("The word","'",newWordInput,"'"," already exists in the dictionary!")
    else:   #Annars lägg till det nya ordet och definition i dem olika listorna.
        wordsList.append(newWordInput) #lägg till i wordsList
        newDescriptionInput = input("Description of word: ") #input från användaren om beskrivningen av ordet
        descriptionsList.append(newDescriptionInput) #lägg till i descriptionsList

#funktion som kollar om ett ord finns i ordlistan och visar definitionen     
def lookupWordInList():
    searchWord = input("Word to lookup: ") #input från användaren
    searchForWordInList(searchWord) #går in i en funktion som returnerar true eller false om ordet redan finns
    if searchForWordInList(searchWord) == False: #Om ordet inte finns så skriv ut att det inte finns
        print("The word","'",searchWord,"' doesn't exist in the dictionary!")
    else:   #annars hämta index och printa ut ord och definition
        findIndex = getIndexOfWordFromList(searchWord) #går in i en funktion som returnerar index på ordet från wordsList
        print("Description for",searchWord,":",getDescriptionFromList(findIndex)) # skriver ut ordet och definitionen som den hämtar från en annan funktion som returnar definitionen beroende på index.

#funktion som kollar om ett ord finns i wordsList och returnerar true eller false              
def searchForWordInList(word):
    if word in wordsList:
        return True
    else:
        return False

#funktion som hämtar index av ett ord i wordsList och returnerar indexet.    
def getIndexOfWordFromList(word):
    return wordsList.index(word)

#funktion som returnerar definitionen beroende på index.
def getDescriptionFromList(index):
        return descriptionsList[index]

#----------------------------------Tuple--------------------------------------------    

# kör menyn och tar inputs.
def runMenu():
    running = True
    printMenu()
    while running:
        userChoice = input("Choose alternative: ")
        if(userChoice == "1"):
            insertTuple()
        elif(userChoice == "2"):
            lookupTuple()
        elif(userChoice == "3"):
            print("Shutting down....")
            raise SystemExit
        else:
            printMenu()
            print("Choose a valid option between 1-3")

            
#lägger till ord och definition av ordet i en tuple
#lägger även till själva tuplen i en lista.
def insertTuple():
    wordInput = input("Word to insert: ")   #input från användaren för ordet
    checkIfWordExist(wordInput)             #går in i en annan funktion och kollar om ordet finns
    if checkIfWordExist(wordInput) == True: #om ordet är == True skriv ut ett felmeddelande
        print("The word '"+wordInput+"' already exist!")
        printMenu()
    else:
        descriptionInput = input("Description of word: ")   #input från användaren för definitionen
        wordTuple = (wordInput,descriptionInput)    #spara inputsen i en tuple    
        wordList.append(wordTuple)  #spara tuplen i en lista
        printMenu() #printa ut menyn igen

#kollar om ordet finns/inte finns och utför en operation beroende på True/False     
def lookupTuple():
    userSearchInput = input("Word to lookup: ") #användarens input för ordet
    checkIfWordExist(userSearchInput)   #kolla om ordet finns
    if checkIfWordExist(userSearchInput) == False:  #om ordet == False, skriv ut felmeddelande
        print("The word '"+userSearchInput+"' dont exist in the dictionary!")
        printMenu()
        
         
    else:   #Annars gå in i funktionen som söker det valda ordet.
        oneWord = getSelectedWord(userSearchInput)
        print("Description for",oneWord)    #printa ut ord + definition
        printMenu() #printa ut menyn igen

#kollar om ett ord finns i listan, finns den returnar den True
#Annars returnar den False.
def checkIfWordExist(word):
    for x in wordList:  #för varje x i listan
        if word in x:       #om ordet finns i x returnera True
            return True
    return False
    

#returnar sökt ord och definition.
def getSelectedWord(word):
    for x,y in wordList:    #för varje x,y i listan
        if word in x:           #om ordet är == x returnera både x och y
            return x+" : "+y
        
        
#-------------------------------------Dictionary---------------------------------------



#kör menyn och tar inputs.
def runMenuDictionary():
    running = True
    printMenu()
    while running:
        choice = input("Choose alternative: ")
        if choice == "1":
            inputDictionary()
        elif choice == "2":
            lookupDictionary()
        elif choice == "3":
            raise SystemExit
        else:
            printMenu()
            print("Choose a valid option between 1-3")

#funktion som kör input delen i programmet        
def inputDictionary():
    wordInput = input("Word to insert: ")
    checkIfWordIsInDictionaryMap(wordInput)
    if checkIfWordIsInDictionaryMap(wordInput) == True:
       print("The word '"+wordInput+"' already exist!")
       printMenu()
       
    else:
       descriptionInput = input("Description of word: ")
       dictionaryMap[wordInput] = descriptionInput
       printMenu()
       

#kollar om ett ord finns i dictionaryn och utför operation beroende på True/False
def lookupDictionary():
    searchInput = input("Word to lookup: ")
    checkIfWordIsInDictionaryMap(searchInput)
    if checkIfWordIsInDictionaryMap(searchInput) == False:
        print("The word '"+searchInput+"' dont exist in the dictionary!")
        printMenu()
        
    else:
        getDescriptionFromDictionary(searchInput)
        print("Description for",searchInput+getDescriptionFromDictionary(searchInput))
        printMenu()
        
             

#funktion som kollar om ett ord finns i dictionaryn.
def checkIfWordIsInDictionaryMap(word):
    for x in dictionaryMap:
        if word in dictionaryMap:
            return True
    return False

#returnar beskrivningen av ordet.
def getDescriptionFromDictionary(word):
        return " : "+dictionaryMap[word]
        
        
        
runStart()

        


    
    
    
