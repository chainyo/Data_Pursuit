from Class.class_Bdd import Bdd
from Class.class_Gameplay import Gameplay

# Stockage des données
questions_1, questions_2, questions_3 = Bdd.get_question_1(), Bdd.get_question_2(), Bdd.get_question_3()
questions = (questions_1, questions_2, questions_3)

# Création de la partie
game = Gameplay(questions)