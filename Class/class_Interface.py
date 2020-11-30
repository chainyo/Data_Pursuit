import tkinter as tk
from tkinter import font as tkfont
import random
from class_Gameplay import Gameplay

colors = ['#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653']

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1500x800")
        self.maxsize(1500, 800)
        self.minsize(1500, 800)

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
        label = tk.Label(self, text="Player Selection", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
        button.pack()
        button = tk.Button(self, text="Launch Game", command=lambda: controller.show_frame("Gameboard"))
        button.pack()

class Gameboard(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # segmentation de la fenêtre en trois zone
        # zone pour l'affichage des joueurs et de leurs camemberts
        self.player_frame = tk.Frame(self, bg="red", height=150, width=1500)
        self.player_frame.grid(row=0)
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


class LoadGame(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose a game to load", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()