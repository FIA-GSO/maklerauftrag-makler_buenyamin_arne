Dictionary = {} #dictionary in welhem die Räumen + Größen gespeichert werden

AnzahlDerRaeume = input("Wie viele Räume gibt es? ") 

AnzahlDerRaeume = int(AnzahlDerRaeume) # anzahl der räume in ein integer konvertieren

RaumArt = str # eine variable die später benöigt wird

for Raum in range(AnzahlDerRaeume):
        RaumBreite = 0
        RaumLaenge = 0
        RaumGroeße = 0 # um Fehler zu umgehen variablen am anfang des algorithmus auf 0 setzen
        RaumName = input("Wie soll der Raum heißen? ")
        while (True):
            RaumArt = input("Hat der Raum genau 4 Ecken? Ja oder Nein ")
            if (RaumArt == "ja" or RaumArt == "Ja" or RaumArt == "Nein" or RaumArt == "nein"): # sicher gehen das man nur ein richtigen input eingeben kann
                break
        if(RaumArt == "Ja" or RaumArt == "ja"): #falls der raum 4 ecken hat wird hier die abfrage zu diesem gemacht
            RaumBreite = int(input("RaumBreite in cm: "))
            RaumLaenge = int(input("RaumLaenge in cm: "))
            RaumGroeße = RaumLaenge * RaumBreite
            Dictionary.setdefault(RaumName, RaumGroeße) #die variabelen werden hier gespeichert
            print("Raum wurde hinzugefügt")

        if(RaumArt == "Nein" or RaumArt == "nein"):
            RaumArt = input("Kann der Raum in mehrere Vierecke geteilt werden? Ja oder Nein ") # falls der raum mehr als 4 ecken hat werden hier die weitern abfragen getätigt
            if(RaumArt == "Ja" or RaumArt == "ja"):
                while True:
                    RaumBreite = RaumBreite + int(input("RaumBreite in cm: "))
                    RaumLaenge = RaumLaenge + int(input("RaumLaenge in cm: "))
                    NextInput = input ("eine Weitere Länge / Breite? Ja oder Nein ")# falls man weitere längen / breiten eingeben will wird dies hier abgefragt
                    if (NextInput == "Nein" or NextInput == "nein" ):
                        RaumGroeße = RaumLaenge * RaumBreite
                        Dictionary.setdefault(RaumName, RaumGroeße)# hier wird der raum gespeichert
                        print("Raum wurde hinzugefügt")
                        break
                    
            if(RaumArt == "Nein" or RaumArt == "nein"):
                NextInput("wollen Sie die Raum Größe selbstständig berechnen? Ja oder Nein")
                if (NextInput == "Nein" or NextInput == "nein" ):# falls man den raum nicht eingeben will wird hier gemacht
                    break
                else:
                    RaumGroeße = input ("geben sie die Größe ihres Raums ein.")
                    Dictionary.setdefault(RaumName, RaumGroeße)# der eigene raum wird hier bespeichert
                    print("Raum wurde hinzugefügt") 
        


for wert in Dictionary:
    print (f"{wert} : {Dictionary.get(wert)}cm²")# die inhalte des dictionary werden hier ausgegeben

Wohnungsfläche = 0 

for wert in Dictionary:
    Wohnungsfläche = Wohnungsfläche + Dictionary.get(wert)

print (f"insgesamte Wohnungsfläche {Wohnungsfläche}cm²")# die insgesamt wohnfläche wird hier ausgegeben
