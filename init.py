from Class.class_Bdd import Bdd
from Class.class_Gameplay import Gameplay
from Class.class_Player import Player
from Class.class_QR import Questions

# Stockage des données
questions = Bdd.get_question()

# Création de la partie
game = Gameplay()