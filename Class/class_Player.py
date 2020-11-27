# Classe joueur
class Player:

    def __init__(self, name):
        # Définition des variables du joueur
        # Son nom
        self.name = name
        # Son score initial
        self.score = 0
        # Variable qui permet de dire si c'est son tour ou non
        self.turn = False
    
    def __str__(self):
        return f"{self.name} à pour le moment {self.score} points."

    # Pour récupérer nom du joueur
    def give_name(self):
        return str(self.name)
    
    # Pour récupérer score du joueur
    def give_score(self):
        return str(self.score)

