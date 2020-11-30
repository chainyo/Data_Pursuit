from tkinter import Label

# Classe joueur
class Player():

    def __init__(self, name, color):
        # Définition des variables du joueur
        # Son nom
        self.name = name
        # Couleur du joueur
        self.color = color
        # Variable qui permet de dire si c'est son tour ou non
        self.turn = False
        # Compteur de bonnes réponses
        self.score = 0
        # Variable pour stocker les camemberts du joueur
        self.cheese = {"cheese_cnt":0}
        # Thèmes validés
        self.valid = set()
        self.valid_formatting = ""
        # Position sur le plateau de jeu
        self.position = (0, 0)
    
    def __str__(self):
        return f"{self.name} à pour le moment {self.cheese['cheese_cnt']} camemberts."

    # Pour récupérer nom du joueur
    def give_name(self):
        return str(self.name)
    
    # Pour récupérer score du joueur
    def give_score(self):
        print(f"{self.name} a répondu juste à {self.score} questions,")
        if self.cheese["cheese_cnt"] == 1:
            print(f"Tu as validé le camembert: {self.valid_formatting}")
        elif self.cheese["cheese_cnt"] > 1:
            print(f"Tu as validé les camemberts: {self.valid_formatting}")

    # ajout des thèmes validés dans le set self.valid
    def add_valid(self):
        for k, v in self.cheese.items():
            if v == True and k != 'cheese_cnt':
                self.valid.add(k)

    # ajout des thèmes validés par le joueur pour présentation écrite
    def valid_theme_formatting(self, tset):
            self.valid_formatting = ", ".join(self.valid)