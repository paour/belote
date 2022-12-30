import random
from dataclasses import dataclass
from enum import Enum


class Couleur(Enum):
    COEUR = "♥️"
    CARREAU = "♦️"
    TREFLE = "♣️"
    PIQUE = "♠️"

    def nom(self): return self.value


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
        return f'{self.figure.nom()} {self.couleur.value} ({self.force(atout_choisi)})'

    def force(self, atout: Couleur): return self.figure.force(self.couleur == atout)


@dataclass
class Joueur:
    nom: str
    main: list[Carte]

    def __init__(self, nom: str) -> None:
        super().__init__()
        self.nom = nom
        self.main = []


class Jeu:
    cartes: list[Carte]

    def __init__(self):
        self.cartes = [Carte(c, f) for f in Figure for c in Couleur]
        random.shuffle(self.cartes)

    def distribuer(self, num_cartes: int, joueur: Joueur):
        joueur.main += self.cartes[0:num_cartes]
        del self.cartes[0:num_cartes]

    def __repr__(self): return self.cartes.__repr__()


atout_choisi = random.sample(list(Couleur), 1)[0]


def main():
    jeu = Jeu()

    joueurs = [Joueur("Magnien"), Joueur("Luc"), Joueur("Angèle"), Joueur("Papilou")]

    print(jeu)

    for num_cartes in [3, 2]:
        for joueur in joueurs:
            jeu.distribuer(num_cartes, joueur)

    print(joueurs)

    print("Atout choisi", atout_choisi.nom())


main()
