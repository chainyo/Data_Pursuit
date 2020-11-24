import mysql.connector
from class_QR import Questions


class Bdd():

    @classmethod
    def connect(cls) :
        cls.bdd = mysql.connector.connect(user='', password='', host='', port= '', database='', raise_on_warnings=True)
        cls.cursor = cls.bdd.cursor()

    @classmethod
    def close(cls):
        cls.bdd.close()
        cls.cursor.close()

    @classmethod
    def commit(cls):
        cls.bdd.commit()

    @classmethod
    def get_question(cls):
        liste_question = []
        query = "select id_question, libelle_question, nom_theme, difficulte_question from questions \
                join theme on theme.id_theme = questions.id_theme"
        
        cursor.execute(query)
        fetch = cursor.fetchall()
        for row in fetch:
            qid = str(row[0])
            qlabel = str(row[1])
            qtheme = str(row[2])
            qlevel = int(row[3])
        
            question = Questions(qid, qlabel, qtheme, qlevel)
            liste_question.append(question)
        return liste_question