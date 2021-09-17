#Autoquartett
#

class Autoquartettkarte(object):
    '''
    Geschwindigkeit={'VW Phaeton':250,
                     'VW New Beetle':185,
                     'VW Touareg':225,}
    Leistung={'VW Phaeton':309,
              'VW New Beetle':85,
              'VW Touareg':230}
    Verbrauch={'VW Phaeton':15.7,
               'VW New Beetle':8.7,
               'VW Touareg':12.2}
    Zylinder={'VW Phaeton':12,
              'VW New Beetle':4,
              'VW Touareg':10}
    Hubraum={'VW Phaeton':6.0,
             'VW New Beetle':2.0,
             'VW Touareg':4.9}
    Beschleunigung={'VW Phaeton':6.7,
                    'VW New Beetle':10.9,
                    'VW Touareg':7.8}
    Zuladung={'VW Phaeton':600,
              'VW New Beetle':419,
              'VW Touareg': 500}
    Ladevolumen={'VW Phaeton':500,
                 'VW New Beetle':527,
                 'VW Touareg':555}
    '''

    def __init__(self, Name, Geschwindigkeit, Leistung, Verbrauch, Zylinder, Hubraum, Beschleunigung, Zuladung, Ladevolumen):
        self.Name=Name
        self.Geschwindigkeit=Geschwindigkeit
        self.Leistung=Leistung
        self.Verbrauch=Verbrauch
        self.Zylinder=Zylinder
        self.Hubraum=Hubraum
        self.Beschleunigung=Beschleunigung
        self.Zuladung=Zuladung
        self.Ladevolumen=Ladevolumen

    def vergleich(self, Geschwindigkeit, Leistung, Verbrauch, Zylinder, Hubraum, Beschleunigung, Zuladung, Ladevolumen):
        Geschwindigkeit>=Geschwindigkeit


VW_Phaeton={}
