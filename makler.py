dictionary = {}  # Noch leeres Wörterbuch um Größen und Raumnamen zu speichern.

anzahl_der_raeume = input("Wie viele Räume gibt es? (Bitte eine ganze Zahl eingeben!) ")
anzahl_der_raeume = int(anzahl_der_raeume)  # Anzahl der Räume in Integer konvertieren
raum_art = str  # Eine Variable die später benötigt wird als String

for Raum in range(anzahl_der_raeume):
    raum_breite = 0
    raum_laenge = 0
    raum_groeße = 0  # Um Fehler umzugehen, Variablen am anfang des Algorithmus auf 0 setzen
    raum_name = input("Wie soll der Raum heißen? ")

    while True:
        raum_art = input("Hat der Raum genau 4 Ecken? Ja oder Nein ")
        if raum_art in ["ja", "Ja", "nein", "Nein"]:
            #Sicher gehen das der Input nur: ja/Ja/nein/Nein sein darf!
            break
        else:
            print("Fehlerhafte Eingabe! Bitte versuchen Sie es nochmal!")

    if raum_art in ["ja", "Ja"]:  # Falls der Raum 4 ecken hat wird hier die abfrage für den Fall gemacht
        raum_breite = int(input("RaumBreite in cm: "))
        raum_laenge = int(input("RaumLaenge in cm: "))
        raum_groeße = raum_laenge * raum_breite
        dictionary.setdefault(raum_name, raum_groeße)  # Die Variablen werden hier gespeichert
        print("Raum wurde hinzugefügt")

    # Falls der Raum mehr als 4 ecken hat werden hier die weitern Abfragen getätigt
    if raum_art == "Nein" or raum_art == "nein":
        raum_art = input("Kann der Raum in mehrere Vierecke geteilt werden? Ja oder Nein ")
        if raum_art == "Ja" or raum_art == "ja":
            while True:
                raum_breite = raum_breite + int(input("RaumBreite in cm: "))
                raum_laenge = raum_laenge + int(input("RaumLaenge in cm: "))
                # Falls man weitere längen / breiten eingeben will wird dies hier abgefragt
                next_input = input("Eine weitere Länge / Breite hinzufügen? Ja oder Nein ")
                if next_input == "Nein" or next_input == "nein":
                    raum_groeße = raum_laenge * raum_breite
                    dictionary.setdefault(raum_name, raum_groeße)  # Hier werden die Rauminformationen gespeichert
                    print("Raum wurde hinzugefügt")
                    break

        if raum_art == "Nein" or raum_art == "nein":
            next_input = input("Wollen Sie die Raum Größe selbstständig berechnen? Ja oder Nein")
            if next_input == "Nein" or next_input == "nein":  # Falls: Raum nicht eingegeben wird : Schleife beenden
                break
            else:
                raum_groeße = input("Geben sie die Größe ihres Raums ein.")
                dictionary.setdefault(raum_name, raum_groeße)  # Der Eigene Raum wird hier gespeichert
                print("Raum wurde hinzugefügt")

# Ausgabe der Namen und Größen der Räume im Dictionary
for wert in dictionary:
    print(f"{wert} : {dictionary.get(wert)}cm²")  # Die Inhalte des Dictionary werden hier ausgegeben

wohnungsfläche = 0
# Berechnung und Ausgabe der kompletten Wohnfläche
for wert in dictionary:
    wohnungsfläche = wohnungsfläche + dictionary.get(wert)

print(f"Die gesamte Wohnungsfläche beträgt {wohnungsfläche}cm²")  # Die gesamte Wohnfläche wird hier ausgegeben
