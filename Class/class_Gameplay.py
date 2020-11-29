from Class.class_Player import Player
from Class.class_Bdd import Bdd
import random

class Gameplay():

    def __init__(self, liquestions, lithemes):
        # initialisation du jeu
        self.questions = liquestions # récupération de la liste des questions
        self.themes = lithemes # récupération des différents thèmes
        self.game_end = False # permet de continuer le jeu tant que cette variable n'est pas True
        self.choose_nb_player() # demande du nombre de joueur
        self.player_creation() # création des joueurs en fct du nombre
        self.set_cheese_score() # attribution des camemberts vides à chaque joueur
        self.turn_cnt = 0 # compteur de tour de jeu
        self.game_turn() # lancement de la partie
        
    def choose_nb_player(self):
        # définir un nombre de joueur
        self.nb_player = int(input("Choisissez un nombre de joueur: "))

    def player_creation(self):
        # création des joueurs en fonction du nombre, stockage dans un dictionnaire {id : objet joueur}
        self.players = {}
        for i in range(0, self.nb_player):
            self.players[i+1] = Player(input(f"Quel est le nom du joueur {i+1}? : "))
    
    def set_cheese_score(self):
        for p in self.players.values():
            for t in self.themes:
                p.cheese[t] = False

    def give_scores(self):
        # donner le score actuel de tous les joueurs
        for player in self.players.values():
            print(player)

    def game_turn(self):
        # check si le jeu n'est pas terminé
        if self.game_end != True:
            self.turn_cnt += 1
            # enchainement des tours du joueur 1 à 4
            for i in range(0, len(self.players)):
                print(f"Début du tour n°{self.turn_cnt}")
                # on définit le joueur dont c'est le tour
                active_player = self.players[i+1]
                print(f"{active_player.name}, c'est ton tour !")
                active_player.turn = True
                # tant que joueur.turn est vrai le joueur va pouvoir jouer (tant qu'il ne donne pas de mauvaise réponse)
                while active_player.turn == True:
                    asked_question = self.ask_question()
                    # si la réponse est fausse le tour du joueur se termine
                    if asked_question[0] == False:
                        active_player.turn = False
                    elif asked_question[0] == True and asked_question[1] == 2:
                        if active_player.cheese[asked_question[2]] == False:
                            self.credit_cheese(active_player, asked_question)
                            active_player.score += 1
                    # sinon on ajoute 1 point à son score
                    else :
                        active_player.score += 1
                    # affichage du score actuel du joueur
                    active_player.give_score()
        # affichage de la fin du tour
        print(f"Fin du tour n°{self.turn_cnt}")
        # affichage du scores de tous les joueurs à la fin du tour
        self.give_scores()
        # lancement du tour suivant
        self.game_turn()
    
    # fonction pour poser une question
    def ask_question(self):
        # niveau de question random
        level = self.random_level()
        # question random en fonction du niveau
        question = self.random_question(level)
        # affichage du label de la question au joueur
        print(question)
        # stockage du theme de la question
        theme = question.theme
        # stockage des réponses possibles pour la question choisie
        reponses = self.get_question_answers(question.id)
        # affichage des réponses pour le joueur
        # et stockage de la réponse du joueur
        rep = self.show_reponses(len(reponses), reponses)
        # comparaison de la valeur de la réponse
        sucess = self.rep_compare(rep, reponses)
        # on retire la question de la liste des questions disponibles si la réponse est juste
        if sucess == True:
            self.remove_question(level)
        return sucess, level, theme

    # fonction pour créditer un camembert à un joueur
    def credit_cheese(self, player, question):
        player.cheese[question[2]] = True
        player.cheese['cheese_cnt'] += 1
        player.add_valid()
        player.valid_theme_formatting(player.valid)

    # fonction random question level 
    def random_level(self):
        x = random.randrange(0, 3)
        return x

    # fonction random question
    def random_question(self, lvl):
        random.shuffle(self.questions[lvl])
        return self.questions[lvl][0]

    # fonction pour obtenir les réponses liées à la question (id)
    def get_question_answers(self, qid):
        reponses = Bdd.get_answer(qid)
        return reponses

    # fonction pour présenter les choix possibles liés à la question en fonction de la longueur de ses réponses
    def show_reponses(self, length, reponses):
        # question QCM
        if length == 3:
            for rep in reponses:
                print(f"- {rep}")
        # question Vrai/faux
        elif length == 2:
            for rep in reponses:
                print(f"- {rep}")
        # dans tous les cas on veut un input du joueur
        rep = input("Ta réponse: ")
        return rep

    # fonction pour comparer la réponse
    def rep_compare(self, rep, li):
        for obj in li:
            if obj.label.lower() == rep.lower():
                if obj.value == str(1):
                    print("Bonne réponse !")
                    return True
                else:
                    pass
            else:
                print("Mauvaise réponse")
                return False
    
    # fonction pour retirer une question bien répondue
    def remove_question(self, lvl):
        del self.questions[lvl][0]