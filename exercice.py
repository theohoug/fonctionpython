class Adversaire:
    pass

import random

class Personnage:
    def __init__(self, nom, force, points):
        self.nom = nom
        self.force = random.randint(25, 50)
        self.points = random.randint(95, 250)
        print(f"Le personnage {self.nom} vient d\'être créé.")

    def frapper(self, adversaire):
        print(f"{self.nom} frappe {adversaire.nom} ")        
        if random.randint(1, 5) == 4:
            print(f"{adversaire.nom} a esquivé l'attaque");
        else:
            adversaire.points = adversaire.points - self.force
        print(f'Points de vie de {self.nom} :  "{self.points}"')
        print(f'Points de vie de {adversaire.nom} :  "{adversaire.points}"')
        if adversaire.points <= 0:
            print(f"{adversaire.nom} est mort ")
        print("-------------------------------")

    def victoire(self, mort, vivant):
        pass
 
perso1 = Personnage("Daisy", 100, 30)
perso2 = Personnage("Mario", 100, 30)
perso3 = Personnage("Luigi", 100, 30)
perso4 = Personnage("Peach", 100, 30)
perso5 = Personnage("Yoshi", 100, 30)
perso6 = Personnage("Waluigi", 100, 30)
perso7 = Personnage("Bowser", 100, 30)

while perso1.points > 0 and perso2.points > 0:
    perso1.frapper(perso2)
    if perso1.points > 0 and perso2.points > 0:
        perso2.frapper(perso1)

