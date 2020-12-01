import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
import random
from Class.class_Bdd import Bdd
from Class.class_Gameplay import Gameplay

colors = ['#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1500x820")
        self.maxsize(1500, 820)
        self.minsize(1500, 820)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
         # stockage des données
        questions_1, questions_2, questions_3 = Bdd.get_question_1(), Bdd.get_question_2(), Bdd.get_question_3()
        self.questions = (questions_1, questions_2, questions_3)
        # stockage des différents thèmes et de leurs couleurs
        self.themes = Bdd.get_theme(colors)
        # création de la partie
        self.game = Gameplay(self.questions, self.themes)

        container = tk.Frame(self)
        container.pack(side="top", fil="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LoadGame, PlayerSelection, Gameboard):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # titre
        lab_title = tk.Label(self, text="Data Pursuit", font=controller.title_font)
        lab_title.pack(side="top", fill="x", pady=10)
        # boutons
        button_new = tk.Button(self, text="New Game", command=lambda: controller.show_frame("PlayerSelection"))
        button_load = tk.Button(self, text="Load Game", command=lambda: controller.show_frame("LoadGame"))
        button_new.pack()
        button_load.pack()


class PlayerSelection(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # titre fenêtre
        label = tk.Label(self, text="Player Selection", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        # liste nombre de joueurs
        OptionList = ["1", "2", "3", "4"]
        self.variable = tk.StringVar(self)
        self.variable.set(OptionList[0])
        self.variable.trace("w", self.callback)
        # label du titre du menu déroulant
        label_joueur = tk.Label(self, text="Choisissez le nombre de joueurs", font=controller.title_font)
        label_joueur.pack(side="top", fill="x", pady=10)
        # menu déroulant
        opt = tk.OptionMenu(self, self.variable, *OptionList)
        opt.config(width=30, font=('Helvetica', 12))
        opt.pack(side="top")
        # frame pour les entry
        self.frame_entry = tk.Frame(self)
        self.frame_entry.pack()
        # bouton retour en arrière
        button_back = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        button_back.pack()
        # bouton pour lancer la partie
        button_launch = tk.Button(self, text="Launch Game", command=lambda: [controller.show_frame("Gameboard"), self.launch_game()])
        button_launch.pack()

    # fonction callback permettant de mettre à jour l'affichage via le choix sur le menu déroulant 
    def callback(self, *args):
        num = self.variable.get()
        for widget in self.frame_entry.winfo_children():
            widget.destroy()

        def entry():
            tk.Label(self.frame_entry, text=f"joueur {i + 1} : ").grid(row=i + 1, column=0, pady=10)
            tk.Entry(self.frame_entry, width=10, justify="center", font=("Helvetica", 10), bg="white", fg="black").grid(
                row=i + 1, column=1, pady=10)

        for i in range(int(num)):
            entry()

    # fonction pour stocker toutes les entryes des noms des joueurs
    def get_players_names(self, frame):
        self.names_li = []
        for widget in self.frame_entry.winfo_children():
            if widget.winfo_class() == 'Entry':
                self.names_li.append(widget.get())

    def launch_game(self):
        self.controller.game.choose_nb_player(self.variable.get())
        self.get_players_names(self.frame_entry)
        self.controller.game.player_creation(self.names_li)
        self.controller.game.set_cheese_score()
        self.controller.game.init_game_turn()
        self.controller.frames['Gameboard'].define_position()
        self.controller.frames['Gameboard'].player_board()
        self.controller.frames['Gameboard'].set_dice()


class Gameboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # segmentation de la fenêtre en trois zone
        # zone pour l'affichage des joueurs et de leurs camemberts
        self.player_frame = tk.Frame(self, bg="red", height=150, width=1500)
        self.player_frame.grid(row=0)
        #frame qui contient le dé et l'affichage
        self.dice_frame1 = tk.Frame(self.player_frame, height=150, width=300)
        self.dice_frame1.grid(row=0, column=0, sticky='ns')
        

        # zone qui regroupe deux autres frames (Plateau & Questions)
        self.game_frame = tk.Frame(self, height=650, width=1500)
        self.game_frame.grid(row=1)
        # frame qui contient le plateau de jeu
        self.gameboard_frame = tk.Frame(self.game_frame, height=650, width=880)
        self.gameboard_frame.grid(row=0, column=0, sticky='ns')

        # frame qui contient les questions et choix de réponses
        self.questions_frame = tk.Frame(self.game_frame, bg='yellow', height=650, width=620)
        self.questions_frame.grid(row=0, column=1, sticky='ns')

        #self.label_question = tk.Label(self.game_frame, bg='green',
        #                               text=f"{self.controller.game.ask_questions.question}", height=650, width=620)
        #self.label_question.grid()

        # création de la grille
        self.grid_cells = self.create_grid() 
    
    #Affiche les joueurs dans la Frame Playername
    def player_board(self):
        for i, player in enumerate(self.controller.game.players.values()):
            self.frame_jojo = tk.Frame(self.player_frame, height=150, width=300, bg=player.color)
            self.frame_jojo.grid(row=0, column=i+1, sticky='ns')
            self.frame_camembert = tk.Frame(self.frame_jojo, bg="red", height=75, width = 300)
            self.frame_camembert.pack()
            self.frame_pseudo = tk.Frame(self.frame_jojo, bg="green", height=75, width = 300)
            self.frame_pseudo.pack()
            #affichage des camemberts
            for i in range(len(self.controller.themes)):
                self.frame_cam = tk.Frame(self.frame_camembert, borderwidth="1",relief="solid", height=75, width = 60)
                self.frame_cam.grid(row=0, column=i+1)
            #label pseudo
            self.label = tk.Label(self.frame_pseudo, text=player.name)
            self.label.place(x=150, y=35, anchor='center')

    # définir les positions initiales des joueurs
    def define_position(self):
        for k, player in self.controller.game.players.items():
            # joueur 1
            if k == 1:
                player.position = (0, 0)
            # joueur 2
            if k == 2:
                player.position = (0, 10)
            # joueur 3
            if k == 3:
                player.position = (10, 10)
            # joueur 4
            if k == 4:
                player.position = (10, 0)
            self.create_lab(player)

    # fonction pour la création d'un pion pour un joueur
    def create_lab(self, player):
        player.lab = tk.Label(self.grid_cells[player.position[0]][player.position[1]], text=player.name, bg=player.color)
        player.lab.place(x=40, y=30, anchor='center')

    # fonction pour nettoyer la frame d'un emplacement passé d'un joueur
    def clean_frame(self, player):
        for widget in self.grid_cells[player.position[0]][player.position[1]].winfo_children():
            if widget == player.lab:
                widget.destroy()
                
    # création du bouton du dé
    def set_dice(self):
        # création du bouton dé
        self.bouton = tk.Button(self.dice_frame1, text='Lancer le dé', height = 5, width = 15, bd=None, relief='flat')
        self.bouton.configure(command=lambda: self.run_turn())
        self.bouton.grid(row=0, column=0)
        # affichage du score du dé
        self.score = tk.Label(self.dice_frame1, text='', font=("Helvetica", 20), fg='black', height = 5, width = 10, bd=None)
        self.score.grid(row=0, column=1)

    # fonction pour lancement du dé et avancement pion
    def run_turn(self):
        self.roll()
        self.result = int(self.score.cget("text"))
        self.position = self.controller.game.active_player.position
        self.clean_frame(self.controller.game.active_player)
        self.controller.game.move_player(self.result)
        self.create_lab(self.controller.game.active_player)

    # création de la grille
    def create_grid(self):
        self.full_grid = []
        color_cnt = 0
        for i in range(0, 11):
            row = []
            for j in range(0, 11):
                cell = tk.Frame(self.gameboard_frame, height=59, width=80, bg='white', borderwidth=1, relief="solid")
                if i == 0 or i == 10 or j == 0 or j == 10:
                    cell.configure(bg=colors[color_cnt])
                    color_cnt += 1
                cell.grid(row=i, column=j)
                row.append(cell)
                if color_cnt > 4:
                    color_cnt = 0
            self.full_grid.append(row)
        return self.full_grid

    # fonction pour lancer le dé
    def roll(self):
        x = random.randint(1, 6)
        self.score.configure(text=x)

    def button_reponses(self):
        # choix de réponses
        if len(self.controller.game.show_reponses) > 1:
            for l in range(len(self.controller.game.show_reponses)):
                self.controller.button_rep = tk.Button(self.game_frame, text="f{self.controller.game.show_reponses}",
                                                       command=lambda: self.controller.game.ask_questions.rep_compare)
                self.controller.button_rep.grid()
        else:
            entry = tk.Entry(self.game_frame, font=40)
            entry.grid()

    def affiche_rep(self):
        label_reponse = tk.Label(self.game_frame, text="f{self.controller.game.ask_questions.reponses}", font=("Helvetica", 20), bg='orange', fg='white', height=5,
                              width=10, bd=None)
        label_reponse.grid()


class LoadGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a game to load", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        button.pack()