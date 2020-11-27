from Class.class_Player import Player
from Class.class_Bdd import Bdd
import random

class Gameplay():

    def __init__(self, liquestions):
        # Initialisation du jeu
        self.questions = liquestions # récupération de la liste des questions
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
                    sucess = self.ask_question()
                    if sucess == False:
                        active_player.turn = False
    
    # fonction pour poser une question
    def ask_question(self):
        # fonction rand pour le choix de la question
        question = self.random_question()
        # affichage du label de la question au joueur
        print(question)
        # stockage des réponses possibles pour la question choisie
        reponses = self.get_question_answers(question.id)
        # affichage des réponses pour le joueur
        # et stockage de la réponse du joueur
        rep = self.show_reponses(len(reponses), reponses)
        # comparaison de la valeur de la réponse
        sucess = self.rep_compare(rep, reponses)
        return sucess

    # fonction random question
    def random_question(self):
        random.shuffle(self.questions)
        return self.questions[0]

    # fonction pour obtenir les réponses liées à la question (id)
    def get_question_answers(self, qid):
        reponses = Bdd.get_answer(qid)
        return reponses

    # fonction pour présenter les choix possibles liés à la question en fonction de la longueur de ses réponses
    def show_reponses(self, length, reponses):
        # Question QCM
        if length == 3:
            for rep in reponses:
                print(f"- {rep}")
        # Question Vrai/faux
        elif length == 2:
            for rep in reponses:
                print(f"- {rep}")
        # Dans tous les cas on veut un input du joueur
        rep = input("Ta réponse: ")
        return rep

    # fonction pour comparer la réponse
    def rep_compare(self, rep, li):
        for obj in li:
            if obj.label == rep:
                if obj.value == str(1):
                    print("Bonne réponse !")
                    return True
                else:
                    pass
            else:
                print("Mauvaise réponse")
                return False