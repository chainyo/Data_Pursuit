from class_Player import Player

class Gameplay():

    def __init__(self):
        # Début de la partie
        self.nb_player = int(input("Choisissez un nombre de joueur: "))
        # Création des joueurs
        players = {}
        for i in range(0, self.nb_player):
            players[i+1] = Player(input(f"Quel est le nom du joueur {i+1}? : "))
        
