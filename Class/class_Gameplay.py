from Class.class_Player import Player

class Gameplay():

    def __init__(self):
        # Initialisation du jeu
        self.game_end = False # permet de continuer le jeu tant que cette variable n'est pas True
        self.choose_nb_player() # demande du nombre de joueur
        self.player_creation() # création des joueurs en fct du nombre
        self.game_turn() # lancement de la partie
        
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

    def game_turn(self):
        # check si le jeu n'est pas terminé
        if self.game_end != True:
            # enchainement des tours du joueur 1 à 4
            for i in range(0, len(self.players)):
                # On définit le joueur dont c'est le tour
                active_player = self.players[i+1]
                print(f"{active_player.name}, c'est ton tour !")
                active_player.turn = True
                # Tant que joueur.turn est vrai le joueur va pouvoir jouer (tant qu'il ne fait pas d'erreur)
                while active_player.turn == True:
                    self.ask_question()
                    active_player.turn = False
            
    # fonction pour poser une question
    def ask_question(self):
        pass