from Class.class_Bdd import Bdd
from Class.class_Gameplay import Gameplay

# stockage des données
questions_1, questions_2, questions_3 = Bdd.get_question_1(), Bdd.get_question_2(), Bdd.get_question_3()
questions = (questions_1, questions_2, questions_3)

# stockage des différents thèmes et de leurs couleurs
themes = Bdd.get_theme(['#e76f51', '#f4a261', '#e9c46a', '#2a9d8f', '#264653'])

# création de la partie
game = Gameplay(questions, themes)