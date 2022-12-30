import random
from dataclasses import dataclass
from enum import Enum, auto


class Couleur(Enum):
    COEUR = "♥️"
    CARREAU = "♦️"
    TREFLE = "♣️"
    PIQUE = "♠️"


class Figure(Enum):
    SEPT = "7", 0, 0, 0
    HUIT = "8", 1, 0, 0
    NEUF = "9", 2, 14, 0
    DIX = "10", 3, 10, 10
    VALET = "valet", 4, 20, 2
    DAME = "dame", 5, 3, 3
    ROI = "roi", 6, 4, 4
    AS = "as", 7, 11, 11

    def rang(self): return self.value[1]

    def nom(self): return self.value[0]

    def force(self, atout: bool): return self.value[2 if atout else 3]


@dataclass
class Carte:
    couleur: Couleur
    figure: Figure

    def __repr__(self):
        return f'{self.figure.nom()} de {self.couleur.value} ({self.force(atout_choisi)})'

    def force(self, atout: Couleur): return self.figure.force(self.couleur == atout)


jeu = [Carte(c, f) for f in Figure for c in Couleur]

atout_choisi = random.sample(list(Couleur), 1)[0]

print(atout_choisi)
print(jeu)
