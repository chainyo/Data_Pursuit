from Class.class_Bdd import Bdd
from Class.class_Gameplay import Gameplay
from Class.class_Interface import App

# stockage des données
questions_1, questions_2, questions_3 = Bdd.get_question_1(), Bdd.get_question_2(), Bdd.get_question_3()
questions = (questions_1, questions_2, questions_3)

# stockage des différents thèmes
themes = Bdd.get_theme()

# affichage de la fenêtre de l'appli
if __name__ == "__main__":
    app = App()
    app.mainloop()

# création de la partie
game = Gameplay(questions, themes)