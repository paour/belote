import random
from dataclasses import dataclass
from enum import Enum


class Couleur(Enum):
    COEUR = "♥️", 0
    CARREAU = "♦️", 1
    TREFLE = "♣️", 2
    PIQUE = "♠️", 3

    def nom(self): return self.value[0]

    def __lt__(self, other): return self.value[1] < other.value[1]


class Figure(Enum):
    # nom, rang, rang_atout, valeur, valeur_atout #
    SEPT = "7", 0, 0, 0, 0
    HUIT = "8", 1, 1, 0, 0
    NEUF = "9", 2, 6, 14, 0
    DIX = "10", 3, 4, 10, 10
    VALET = "valet", 4, 7, 20, 2
    DAME = "dame", 5, 2, 3, 3
    ROI = "roi", 6, 3, 4, 4
    AS = "as", 7, 5, 11, 11

    def rang(self): return self.value[1]

    def nom(self): return self.value[0]

    def valeur(self, atout: bool): return self.value[3 if atout else 4]

    def force(self, atout: bool): return self.value[3 if atout else 2] + (10 if atout else 0)

    def __lt__(self, other): return self.rang() < other.rang()


@dataclass
class Carte:
    couleur: Couleur
    figure: Figure

    def __repr__(self):
        return f'{self.figure.nom()} {self.couleur.value} ({self.valeur(atout_choisi)})'

    def valeur(self, atout: Couleur): return self.figure.valeur(self.couleur == atout)

    def force(self, atout: Couleur): return self.figure.force(self.couleur == atout)

    def __lt__(self, other): return self.couleur < other.couleur if self.figure == other.figure else self.figure < other.figure


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


atout_choisi = random.choice(list(Couleur))


def main():
    jeu = Jeu()

    joueurs = [Joueur("Magnien"), Joueur("Luc"), Joueur("Angèle"), Joueur("Papilou")]

    print("Battu", jeu)

    print("Trié par rang", sorted(jeu.cartes))

    print("Trié par force", sorted(jeu.cartes, key=lambda carte: carte.force(atout_choisi)))

    for num_cartes in [3, 2]:
        for joueur in joueurs:
            jeu.distribuer(num_cartes, joueur)

    print(joueurs)

    print("Atout choisi", atout_choisi.nom())


main()
