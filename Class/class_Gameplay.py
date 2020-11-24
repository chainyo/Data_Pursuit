from class_Player import Player

class Gameplay():

    def __init__(self):
        # Initialisation du jeu
        self.game_end = False # permet de continuer le jeu tant que cette variable n'est pas True
        self.choose_nb_player() # demande du nombre de joueur
        self.player_creation() # création des joueurs en fct du nombre
        
    def choose_nb_player(self):
        # Définir un nombre de joueur
        self.nb_player = int(input("Choisissez un nombre de joueur: "))

    def player_creation(self):
        # Création des joueurs en fonction du nombre, stockage dans un dictionnaire {id : objet joueur}
        self.players = {}
        for i in range(0, self.nb_player):
            self.players[i+1] = Player(input(f"Quel est le nom du joueur {i+1}? : "))

    def give_scores(self):
        # Donner le score actuel de tous les joueurs
        for player in self.players.values():
            print(player)

jeu = Gameplay()