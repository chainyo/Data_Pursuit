import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkfont
import random
from functools import partial
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
        self.controller.frames['Gameboard'].show_active_player()
        self.controller.frames['Gameboard'].define_position()
        self.controller.frames['Gameboard'].player_board()
        self.controller.frames['Gameboard'].set_dice()

class Gameboard(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # segmentation de la fenêtre en trois zone
        # zone pour l'affichage des joueurs et de leurs camemberts
        self.player_frame = tk.Frame(self, height=150, width=1500)
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
        self.questions_frame = tk.Frame(self.game_frame, height=650, width=620)
        self.questions_frame.grid(row=0, column=1, sticky='ns')

        # on fixe la taille mini des colonnes du .grid
        self.game_frame.grid_columnconfigure(0, minsize=880)
        self.game_frame.grid_columnconfigure(1, minsize=620)

        # création de la grille
        self.grid_cells = self.create_grid() 
    
    #Affiche les joueurs dans la Frame Playerframe
    def player_board(self):
        self.rows = []
        for i, player in enumerate(self.controller.game.players.values()):
            self.frame_joueur = tk.Frame(self.player_frame, height=150, width=295, bg=player.color)
            self.frame_joueur.grid(row=0, column=i+1, sticky='ns', padx=5)
            self.frame_camembert = tk.Frame(self.frame_joueur, height=75, width = 295)
            self.frame_camembert.pack()
            self.frame_pseudo = tk.Frame(self.frame_joueur, height=75, width = 295, bg=player.color)
            self.frame_pseudo.pack()
            self.row_cheese = []
            #affichage des camemberts
            for i in range(len(self.controller.themes)):
                self.frame_cam = tk.Frame(self.frame_camembert, borderwidth="1",relief="solid", height=75, width = 59)
                self.frame_cam.grid(row=0, column=i+1)
                self.row_cheese.append(self.frame_cam)
            self.rows.append(self.row_cheese)
            #label pseudo
            fontStyle = tkfont.Font(family="Helvetica", size=20)
            self.label = tk.Label(self.frame_pseudo, text=player.name, bg=player.color, font=fontStyle)
            self.label.place(x=148, y=35, anchor='center')

    # affichage du joueur actif
    def show_active_player(self):
        self.activ_frame = tk.Frame(self.questions_frame, width=620)
        self.activ_frame.grid(row=0, sticky="nesw")
        self.activ_frame.grid_columnconfigure(0, minsize=620)
        self.change_active_player()

    def change_active_player(self):
        pname = self.controller.game.active_player.name
        pcolor = self.controller.game.active_player.color
        self.activ_lab = tk.Label(self.activ_frame, text=f'{pname} à toi de jouer !', font=('Helvetica', 15), bg='black', fg=pcolor)
        self.activ_lab.grid(row=0, pady=25)

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
        self.bouton = tk.Button(self.dice_frame1, text='Lancer le dé',font=('Helvetica', 16), height = 5, width = 15, bd=None, relief='flat', state='normal')
        self.bouton.configure(command=lambda: self.run_turn())
        self.bouton.grid(row=0, column=0)
        # affichage du score du dé
        self.score = tk.Label(self.dice_frame1, text='', font=("Helvetica", 20), fg='black', height = 5, width = 5, bd=None)
        self.score.grid(row=0, column=1)

    # fonction pour lancement du dé et avancement pion
    def run_turn(self):
        self.state(self.bouton)
        self.roll()
        self.result = int(self.score.cget("text"))
        self.clean_frame(self.controller.game.active_player)
        self.controller.game.move_player(self.result)
        self.create_lab(self.controller.game.active_player)
        self.position = self.controller.game.active_player.position
        self.theme = self.define_theme(self.position)
        self.question = self.controller.game.set_question(self.theme)
        self.show_question(self.question.theme, self.question.label, self.theme.color)
        self.answers = self.controller.game.get_question_answers(self.question.id)
        self.show_answers(self.answers)

    # definir le thème en fonction de la couleur de bg du brackground
    def define_theme(self, position):
        cell_color = self.grid_cells[position[0]][position[1]]["bg"]
        theme = [c for c in self.controller.themes if c.color == cell_color]
        return theme[0]

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

    # créer frame question
    def show_question(self, qtheme, qlabel, color):
        label = self.check_label_size(qlabel)
        # frame pour la question
        self.lab_frame = tk.Frame(self.questions_frame, width=620)
        self.lab_frame.grid(row=1, sticky="nesw")
        self.lab_frame.grid_columnconfigure(0, minsize=620)
        # affichage du thème
        self.theme = tk.Label(self.lab_frame, text=qtheme, font=('Helvetica', 32), fg=color)
        self.theme.grid(row=0, pady=25)
        # affichage de l'intitulé de la question
        self.label = tk.Label(self.lab_frame, text=label, font=('Helvetica', 16))
        self.label.grid(row=1, pady=10)

    # créer frame des réponses
    def show_answers(self, answers):
        self.ans_frame = tk.Frame(self.questions_frame, width=620)
        self.ans_frame.grid(row=2, sticky="nesw")
        self.ans_frame.grid_columnconfigure(0, minsize=620)
        if len(answers) > 1:
            random.shuffle(answers)
            for i, ans in enumerate(answers):
                self.command = partial(self.ans_compare, (ans.label, answers))
                self.button = tk.Button(self.ans_frame, text=ans.label, bg='white', relief='flat', command=self.command)
                self.button.grid(row=i+1, pady=5)
        else:
            self.input = tk.Entry(self.ans_frame)
            self.input.grid(row=3, pady=10)
            self.validation = tk.Button(self.ans_frame, text='Valider', command=lambda: self.ans_compare((self.input.get(), answers)))
            self.validation.grid(row=4, pady=10)

    # fonction pour check la longueur du label de la question
    def check_label_size(self, label):
        new_label = ''
        if len(label) > 50:
           new_label += label[0:50]
           cut = label[50:60].find(' ')
           cut += 50
           new_label += label[50:cut]
           new_label += '\n'
           new_label += label[cut:]
        else : 
            new_label = label
        return new_label

    # fonction pour comparer la réponse
    def ans_compare(self, ans):
        self.sucess = self.controller.game.rep_compare(ans[0], ans[1])
        if self.sucess == True:
            self.remove_question(self.question)
            self.controller.game.active_player.score += 1
            if self.question.level == 1:
                self.controller.game.credit_cheese(self.controller.game.active_player, self.question)
                self.update_cheese(self.controller.game.active_player)
                self.check_cheese(self.controller.game.active_player)
        else:
            self.controller.game.active_player.turn = False
            self.controller.game.set_active_player()
            self.controller.game.active_player.score = 0
        self.state(self.bouton)
        self.clean_qr(self.questions_frame)
        self.show_active_player()
        
    # mise à jour graphique des camemberts
    def update_cheese(self, player):
        for i, theme in enumerate(player.valid):
            player_row = self.controller.game.player_cnt
            theme_color = [c.color for c in self.controller.themes if c.label == theme]
            self.rows[player_row - 2][i].configure(bg=theme_color)

    # regarde si il y a un vainqueur
    def check_cheese(self, player):
        if len(player.valid) == 5:
            self.controller.game.game_end = True
            self.end_game()

    # fenetre de fin de partie
    def end_game(self):
        messagebox.showinfo(title='Fin de partie', message=f"{self.controller.game.active_player.name} vient de gagner la partie, félicitations !!")

    # nettoyage des frames questions / réponses
    def clean_qr(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    # fonction pour retirer une question bien répondue
    def remove_question(self, question):
        self.controller.questions[question.level - 1].remove(question)

    # fonction pour changer l'état du bouton
    def state(self, button):
        if button["state"] == 'disabled':
            button["state"] = 'normal'
        else:
            button["state"] = 'disabled'

class LoadGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a game to load", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        button.pack()