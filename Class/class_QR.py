class Questions():

    def __init__(self, qlabel, qanswer, qtheme, qtype, qlevel):
        # l'énoncé de la question
        self.label = qlabel
        # la réponse associée
        self.answer = qanswer
        # le thème de la question
        self.theme = qtheme
        # le type de question (QCM, V/F, ouverte)
        self.type = qtype
        # le niveau de difficulté
        self.level = qlevel
    
    # Permer en utilisant print d'avoir un affichage console du thème et de l'énoncé de la question
    def __str__(self):
        return f"{self.theme}: {self.label} ?"

    # Fonctionnalité pour comparer une string avec la réponse associée à la question
    def compare_answer(self, answer):
        if str(answer.lower()) == self.answer:
            return True