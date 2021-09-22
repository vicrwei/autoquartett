"""
Autoquartett
IS 119
Übung OOP 01
VW
"""
import random
from enum import Enum


class Attribute(Enum):
    Geschwindigkeit = 0
    Leistung = 1
    Verbrauch = 2
    Zylinder = 3
    Hubraum = 4
    Beschleunigung = 5
    Zuladung = 6
    Ladevolumen = 7


# Erstellen einer Klasse für die Autoquartettkarte
class Autoquartettkarte(object):

    # Instantierung der Klasse mit den zugehörigen Werten und ihrer Typen
    def __init__(self, Name, Geschwindigkeit, Leistung, Verbrauch, Zylinder, Hubraum, Beschleunigung, Zuladung,
                 Ladevolumen):
        self.Name = Name
        self.Geschwindigkeit = max(min(int(Geschwindigkeit), 250),
                                   10)  # Min/Max Limitierung der  Höchstgeschwindigkeit (Traktor)
        self.Leistung = int(Leistung)
        self.Verbrauch = float(Verbrauch)
        self.Zylinder = int(Zylinder)
        self.Hubraum = float(Hubraum)
        self.Beschleunigung = float(Beschleunigung)
        self.Zuladung = int(Zuladung)
        self.Ladevolumen = int(Ladevolumen)

    # Vorgabe, wie verglichen werden soll
    def vergleich(self, Attribut, karte):
        attr = Attribute(Attribut)
        if attr == Attribute.Geschwindigkeit:
            return self.Geschwindigkeit > karte.Geschwindigkeit
        if attr == Attribute.Hubraum:
            return self.Hubraum > karte.Hubraum
        if attr == Attribute.Zylinder:
            return self.Zylinder > karte.Zylinder
        if attr == Attribute.Zuladung:
            return self.Zuladung > karte.Zuladung
        if attr == Attribute.Ladevolumen:
            return self.Ladevolumen > karte.Ladevolumen
        if attr == Attribute.Leistung:
            return self.Leistung > karte.Leistung

        # Öko
        if attr == Attribute.Verbrauch:
            return self.Verbrauch < karte.Verbrauch

        if attr == Attribute.Beschleunigung:
            return self.Beschleunigung < karte.Beschleunigung

    # Erzeugen einer Ausgabe für den Spieler bei Gewinn der Karte
    def __str__(self):
        tmp = ("Name:" + str(self.Name)) + "\r\n"
        tmp += ("Geschwindigkeit:" + str(self.Geschwindigkeit)) + "\r\n"
        tmp += ("Leistung:" + str(self.Leistung)) + "\r\n"
        tmp += ("Verbrauch:" + str(self.Verbrauch)) + "\r\n"
        tmp += ("Zylinder:" + str(self.Zylinder)) + "\r\n"
        tmp += ("Hubraum:" + str(self.Hubraum)) + "\r\n"
        tmp += ("Beschleunigung:" + str(self.Beschleunigung)) + "\r\n"
        tmp += ("Zuladung:" + str(self.Zuladung)) + "\r\n"
        tmp += ("Ladevolumen:" + str(self.Ladevolumen)) + "\r\n"
        return tmp


# Anlegen einer Klasse Autoquartettspiel
class Autoquartettspiel:

    # Initialisierung des Arrays mit den ersten vorgegebenen Karten
    def __init__(self, karte):
        autos = [Autoquartettkarte('VW Phaeton', 249, 309, 15.7, 12, 6.0, 6.7, 600, 500),
                 Autoquartettkarte('VW New Beetle', 185, 85, 8.7, 4, 2.0, 10.9, 419, 527),
                 Autoquartettkarte('VW Touareg', 225, 230, 12.2, 10, 4.9, 7.8, 500, 555)]
        self.autos = autos
        self.Userkarte = karte

    """
    Anlegen einer Spielfunktion, der Benutzer spielt gegen den Computer mit einer selbsterstellten Karte,
    die er über Input eingibt. Es wird so lange gespielt, wie das Array des Computers noch Karten beinhaltet bzw. der Benutzer
    noch nicht verloren hat.
    """

    def spielen(self):
        rnd = random.Random()
        while len(self.autos) > 0 and self.Userkarte is not None:
            for i in Attribute:
                print("[" + str(i.value) + "]\t" + i.name)
            inp = int(input("Bitte geben sie ein Attribut zum Vergleich an:"))
            rndKarte = self.autos[rnd.randint(0, len(self.autos) - 1)]
            if self.Userkarte.vergleich(inp, rndKarte):
                print("Gewonnen, Sie besitzen diese Karte nun")
                print(rndKarte)
                self.autos.remove(rndKarte)
            else:
                print("Verloren...")
                self.Userkarte = None


Userkarte = Autoquartettkarte(input("Name:"), input("Geschwindigkeit (km/h):"), input("Leistung(kW):"),
                              input("Verbrauch(L/100km):"), input("Zylinder(Anzahl):"), input("Hubraum(Liter):"),
                              input("Beschleunigung(s):"),
                              input("Zuladung(kg):"), input("Ladevolumen(Liter):"))

Spiel = Autoquartettspiel(Userkarte)
Spiel.spielen()
