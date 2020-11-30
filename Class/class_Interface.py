import tkinter as tk
from tkinter import font as tkfont
import random


colors = ['#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1500x820")
        self.maxsize(1500, 820)
        self.minsize(1500, 820)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

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
        lab_title = tk.Label(self, text="Data Pursuit", font=controller.title_font)
        lab_title.pack(side="top", fill="x", pady=10)

        button_new = tk.Button(self, text="New Game", command=lambda: controller.show_frame("PlayerSelection"))
        button_load = tk.Button(self, text="Load Game", command=lambda: controller.show_frame("LoadGame"))
        button_new.pack()
        button_load.pack()

class PlayerSelection(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #titre fenêtre
        label = tk.Label(self, text="Player Selection", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        #liste nombre de joueurs
        OptionList = [
        "1",
        "2",
        "3",
        "4"
        ] 

        variable = tk.StringVar(self)
        variable.set(OptionList[0])

        label_joueur = tk.Label(self, text="Choisissez le nombre de joueurs", font=controller.title_font)
        label_joueur.pack(side="top", fill="x", pady=10)


        #menu déroulant
        opt = tk.OptionMenu(self, variable, *OptionList)
        opt.config(width=30, font=('Helvetica', 12))
        opt.pack(side="top")

        frame_entry = tk.Frame(self)
        frame_entry.pack()

        #fonction callback permettant de mettre à jour l'affichage via le choix sur le menu déroulant 
        def callback(*args):
            loulou = variable.get()
            for widget in frame_entry.winfo_children():
                widget.destroy()
            def entry():
                tk.Label(frame_entry, text=f"joueur {i+1} : ").grid(row = i+1, column = 0, pady=10)
                tk.Entry(frame_entry, width=10, justify="center", font=("Helvetica", 10), bg="white", fg="black").grid(row = i+1, column = 1, pady=10)
            for i in range(int(loulou)):
                entry()

        variable.trace("w", callback)

        #bouton retour en arrière
        button_back = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        button_back.pack()

        # bouton pour lancer la partie
        button_launch = tk.Button(self, text="Launch Game", command=lambda: controller.show_frame("Gameboard"))
        button_launch.pack()


class Gameboard(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # segmentation de la fenêtre en trois zone
        # zone pour l'affichage des joueurs et de leurs camemberts
        self.player_frame = tk.Frame(self, bg="red", height=150, width=1500)
        self.player_frame.grid(row=0)
        #frame qui contient le dé et l'affichage
        self.dice_frame1 = tk.Frame(self.player_frame, height=150, width=300, bg='yellow')
        self.dice_frame1.grid(row=0, column=0, sticky='ns')
        self.dice_frame = tk.Frame(self.player_frame, height=150, width=300, bg='red')
        self.dice_frame.grid(row=0, column=1, sticky='ns')
        self.dice_frame = tk.Frame(self.player_frame, height=150, width=300, bg='blue')
        self.dice_frame.grid(row=0, column=2, sticky='ns')
        self.dice_frame = tk.Frame(self.player_frame, height=150, width=300, bg='green')
        self.dice_frame.grid(row=0, column=3, sticky='ns')
        self.dice_frame = tk.Frame(self.player_frame, height=150, width=300, bg='pink')
        self.dice_frame.grid(row=0, column=4, sticky='ns')
        # zone qui regroupe deux autres frames (Plateau & Questions)
        self.game_frame = tk.Frame(self, height=650, width=1500)
        self.game_frame.grid(row=1)
        # frame qui contient le plateau de jeu
        self.gameboard_frame = tk.Frame(self.game_frame, height=650, width=880)
        self.gameboard_frame.grid(row=0, column=0, sticky='ns')
        # frame qui contient les questions et choix de réponses
        self.questions_frame = tk.Frame(self.game_frame, bg='green', height=650, width=620)
        self.questions_frame.grid(row=0, column=1, sticky='ns')
        # création de la grille
        grid_cells = self.create_grid()
        #affichage du score
        self.score = tk.Label(self.dice_frame1, text='rien', font=("Helvetica", 20), bg='orange', fg='white', height = 5, width = 10, bd=None)
        self.score.grid(row=0, column=1) 
        #création du bouton
        self.bouton = tk.Button(self.dice_frame1, text='Lancer le dé', height = 5, width = 15, bd=None, relief='flat')
        self.bouton.configure(command=lambda: self.roll())
        self.bouton.grid(row=0, column=0)

    # création de la grille
    def create_grid(self):
        self.full_grid = {}
        color_cnt = 0
        for i in range(0, 11):
            row = set()
            for j in range(0, 11):
                cell = tk.Frame(self.gameboard_frame, height=59, width=80, bg='white', borderwidth=1, relief="solid")
                if i == 0 or i == 10 or j == 0 or j == 10:
                    cell.configure(bg=colors[color_cnt])
                    color_cnt += 1
                cell.grid(row=i, column=j)
                row.add(cell)
                if color_cnt > 4:
                    color_cnt = 0
            self.full_grid[i] = row
        return self.full_grid
    
    # création du dé
    def roll(self):
        x = random.randint(1,6)
        self.score.configure(text=x)


class LoadGame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a game to load", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()