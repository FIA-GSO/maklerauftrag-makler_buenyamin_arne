Dictionary = {}


AnzahlDerRaeume = input("Wie viele Räume gibt es? ")

AnzahlDerRaeume = int(AnzahlDerRaeume)

for Raum in range(AnzahlDerRaeume + 1):
    RaumName = input("Wie soll der Raum heißen? ")
    RaumArt = input("Hat der Raum genau 4 Ecken? Ja oder Nein ")
    RaumBreite = 0
    RaumLaenge = 0
    if(RaumArt == "Ja" or RaumArt == "ja"):
        RaumLaenge = int(input("Wie lang ist der Raum? In Zentimeter "))
        RaumBreite = int(input("Wie breit ist der Raum? In Zentimeter "))
        RaumGroeße = RaumLaenge * RaumBreite
        print(RaumGroeße)
        Dictionary.setdefault(RaumName, RaumGroeße)
        print (Dictionary)

    else:   
        RaumArt = input("Kann der Raum in mehrere Vierecke geteilt werden? Ja oder Nein ")
        if(RaumArt == "Ja" or RaumArt == "ja"):
            while True:
                RaumBreite + int(input("RaumBreite: "))
                RaumLaenge + int(input("RaumLaenge: "))
                NextInput = input ("eine Weitere Länge/ Breite? Ja oder Nein ")
                if (NextInput == "Nein" or NextInput == "nein" ):
                    break
            # in dict speichern
        else:
            