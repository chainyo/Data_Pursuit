class Questions():

    def __init__(self, qid, qlabel, qtheme, qlevel):
        # l'id de la question dans la bdd
        self.id = qid
        # l'énoncé de la question
        self.label = qlabel
        # le thème de la question
        self.theme = qtheme
        # le niveau de difficulté
        self.level = qlevel
    
    # Permer en utilisant print d'avoir un affichage console du thème et de l'énoncé de la question
    def __str__(self):
        return f"{self.theme}: {self.label} ?"

    # Fonctionnalité pour comparer une string avec la réponse associée à la question
    #def compare_answer(self, answer):
    #    if str(answer.lower()) == self.answer:
    #        return True

class Answer():

    def __init__(self, ansid, qid, anslabel, ansval):
        self.id = ansid
        self.qid = qid
        self.label = anslabel
        self.value = ansval

    def __str__(self):
        return f"{self.label}"

class Theme():

    def __init__(self, tid, tlabel):
        self.id = tid
        self.label = tlabel
    
    def __str__(self):
        return f"{self.label}"