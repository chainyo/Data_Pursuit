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

    def set_question(self, theme, cheese_position):
        # niveau de question en fonction score du joueur
        if self.active_player.position in cheese_position:
            level = 2
        else:
            if self.active_player.score < 2:
                level = 0
            elif self.active_player.score > 2:
                level = 1
        # question random en fonction du niveau
        self.question = self.random_question(level, theme)
        return self.question

    # fonction pour créditer un camembert à un joueur
    def credit_cheese(self, player, question):
        player.cheese[question.theme] = True
        player.cheese['cheese_cnt'] += 1
        player.add_valid()

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