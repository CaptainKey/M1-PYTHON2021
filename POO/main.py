class Voiture:
    def __init__(self,nom):
        self.nom = nom
        self.vitesse = 0
    def acc(self):
        self.vitesse += 10

class Twingo(Voiture):
    def __init__(self,nom):
        super().__init__(nom)
        self.nom = nom

voiture1 = Voiture('Voiture 1')
voiture2 = Voiture('Voiture 2')


print('Voiture 1 nom ',voiture1.nom)
print('Voiture 2 nom ',voiture2.nom)

voiture1.acc()

print('Voiture 1 vitesse ',voiture1.vitesse)
print('Voiture 2 vitesse ',voiture2.vitesse)

twingo1 = Twingo('Twingo 1')

print(twingo1.nom)
print(twingo1.vitesse)

twingo1.acc()

print('Nouvelle vitesse',twingo1.vitesse)
