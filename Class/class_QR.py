class Questions():

    def __init__(self, qlabel, qanswer, qtheme, qtype, qlevel):
        self.label = qlabel
        self.answer = qanswer
        self.theme = qtheme
        self.type = qtype
        self.level = qlevel
    
    def __str__(self):
        return f"{self.theme}: {self.label} ?"

    def compare_answer(self, answer):
        if answer.lower() == self.answer:
            return True