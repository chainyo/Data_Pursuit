# Classe joueur
class Player():

    def __init__(self, name):
        # Définition des variables du joueur
        # Son nom
        self.name = name
        # Son score initial
        self.score = 0
        # Variable qui permet de dire si c'est son tour ou non
        self.turn = False