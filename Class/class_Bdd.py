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
        
        cls.cursor.execute(query)
        fetch = cls.cursor.fetchall()
        for row in fetch:
            question = Questions(str(row[0]), str(row[1]), str(row[2]), int(row[3]))
            liste_question.append(question)
        return liste_question