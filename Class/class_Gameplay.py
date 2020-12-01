from Class.class_Player import Player
from Class.class_Bdd import Bdd
import random


class Gameplay:

    def __init__(self, liquestions, lithemes):
        # initialisation du jeu
        self.questions = liquestions  # récupération de la liste des questions
        self.themes = lithemes  # récupération des différents thèmes
        self.game_end = False  # permet de continuer le jeu tant que cette variable n'est pas True
        self.turn_cnt = 0  # compteur de tour de jeu
        self.player_cnt = 1 # compteur pour suivre le tour des joueurs

    def choose_nb_player(self, num):
        # définir un nombre de joueur
        self.nb_player = int(num)

    def player_creation(self, linames):
        # création des joueurs en fonction du nombre, stockage dans un dictionnaire {id : objet joueur}
        self.players = {}
        pcolors = ['#caffbf', '#bdb2ff', '#9bf6ff', '#ffadad']
        for i, name in enumerate(linames):
            self.players[i + 1] = Player(name, pcolors[i])

    # initialisation des camemberts des joueurs à False
    def set_cheese_score(self):
        for p in self.players.values():
            for t in self.themes:
                p.cheese[t] = False

    def give_scores(self):
        # donner le score actuel de tous les joueurs
        for player in self.players.values():
            print(player)

    # def game_turn(self):
    #        asked_question = self.ask_question()
            # si la réponse est fausse le tour du joueur se termine
    #        if asked_question[0] == False:
    #            active_player.turn = False
    #        elif asked_question[0] == True and asked_question[1] == 2:
    #            if active_player.cheese[asked_question[2]] == False:
    #                self.credit_cheese(active_player, asked_question)
    #                active_player.score += 1
            # sinon on ajoute 1 point à son score
    #        else:
    #            active_player.score += 1
            # affichage du score actuel du joueur
    #        active_player.give_score()
        # affichage de la fin du tour
    #    print(f"Fin du tour n°{self.turn_cnt}")
        # affichage du scores de tous les joueurs à la fin du tour
    #    self.give_scores()
        # lancement du tour suivant
    #    self.game_turn()

    def init_game_turn(self):
        # check si le jeu n'est pas terminé
        if self.game_end != True:
            self.turn_cnt += 1
        self.set_active_player()
        
    def set_active_player(self):
        if self.player_cnt <= len(self.players):
            self.active_player = self.players[self.player_cnt]
            self.active_player.turn = True
            self.player_cnt += 1
        else:
            self.player_cnt = 1
            self.set_active_player()

    def move_player(self, dice):
        increment = int(dice)
        while increment > 0:
            x = int(self.active_player.position[0])
            y = int(self.active_player.position[1])
            if x == 0 and y < 10:
                self.active_player.position = (x, y + 1)
            elif x < 10 and y == 10:
                self.active_player.position = (x + 1, y)
            elif x == 10 and y > 0:
                self.active_player.position = (x, y - 1)
            elif x > 0 and y == 0:
                self.active_player.position = (x - 1, y)
            increment -= 1

    def set_question(self, theme):
        # niveau de question random
        level = self.random_level()
        # question random en fonction du niveau
        self.question = self.random_question(0, theme)
        return self.question

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
    def random_question(self, lvl, theme):
        self.question_pull = []
        for q in self.questions[lvl]:
            if str(q.theme) == str(theme):
                self.question_pull.append(q)
        return random.choice(self.question_pull)

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
                    return True
                else:
                    pass
            else:
                return False