#Strings ingredienser
def recept(antal):
    ägg = "Ägg"
    socker = "Strösocker"
    vaniljsocker = "Vaniljsocker"
    bakpulver = "Bakpulver"
    vetemjöl = "Vetemjöl"
    smör = "Smör"
    vatten = "Vatten"

#antal ingredienser
    äggAntal = 0.75*antal
    sockerAntal = 0.75*antal
    vaniljsockerAntal = 0.5*antal
    bakpulverAntal = 0.5*antal
    vetemjölAntal = 0.75*antal
    smörAntal = 18.75*antal
    vattenAntal = 0.25*antal

#printar ut ingredienserna
    print(int(äggAntal),"st",ägg)
    print(sockerAntal,"dl",socker)
    print(vaniljsockerAntal,"tsk",vaniljsocker)
    print(bakpulverAntal,"tsk",bakpulver)
    print(vetemjölAntal,"dl",vetemjöl)
    print(int(smörAntal),"g",smör)
    print(vattenAntal,"dl",vatten)

#funktion som räknar ut totala tiden för att blanda
def tidblanda(antal):
    tidsåtgång = 10
    totalTid = tidsåtgång+antal
    return totalTid

#funktion som räknar ut totala tiden för att grädda
def tidgradda(antal):
    tidsåtgång = 30
    totalTid = tidsåtgång + (antal * 3)
    return totalTid

#funktion som räknar ut
def sockerkaka(antal):
    print("Ingredienser för",antal,"personer.")
    recept(antal)
    tidsåtgång = tidblanda(antal) + tidgradda(antal)
    print("Tid: ",tidsåtgång,"min")
    
    
    


