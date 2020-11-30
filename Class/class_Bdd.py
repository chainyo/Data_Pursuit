import mysql.connector
from Class.class_QR import Questions, Answer, Theme


class Bdd:

    @classmethod
    def connect(cls):
        cls.bdd = mysql.connector.connect(user='root', password='root', host='localhost', port='3306',
                                          database='data_pursuit', raise_on_warnings=True)
        cls.cursor = cls.bdd.cursor()

    @classmethod
    def close(cls):
        cls.bdd.close()
        cls.cursor.close()

    @classmethod
    def commit(cls):
        cls.bdd.commit()

    @classmethod
    def get_question_1(cls):
        cls.connect()
        liste_question = []
        query = "select id_question, libelle_question, nom_theme, difficulte_question from questions \
                join theme on theme.id_theme = questions.id_theme \
                where difficulte_question = '1'"

        cls.cursor.execute(query)
        fetch = cls.cursor.fetchall()
        for row in fetch:
            question = Questions(str(row[0]), str(row[1]), str(row[2]), int(row[3]))
            liste_question.append(question)
        cls.close()
        return liste_question

    @classmethod
    def get_question_2(cls):
        cls.connect()
        liste_question = []
        query = "select id_question, libelle_question, nom_theme, difficulte_question from questions \
                join theme on theme.id_theme = questions.id_theme\
                where difficulte_question = '2'"

        cls.cursor.execute(query)
        fetch = cls.cursor.fetchall()
        for row in fetch:
            question = Questions(str(row[0]), str(row[1]), str(row[2]), int(row[3]))
            liste_question.append(question)
        cls.close()
        return liste_question

    @classmethod
    def get_question_3(cls):
        cls.connect()
        liste_question = []
        query = "select id_question, libelle_question, nom_theme, difficulte_question from questions \
                join theme on theme.id_theme = questions.id_theme\
                where difficulte_question = '3'"

        cls.cursor.execute(query)
        fetch = cls.cursor.fetchall()
        for row in fetch:
            question = Questions(str(row[0]), str(row[1]), str(row[2]), int(row[3]))
            liste_question.append(question)
        cls.close()
        return liste_question

    @classmethod
    def get_answer(cls, get_qid):
        cls.connect()
        id_question = get_qid
        query = f"select id_reponse, id_question, libelle_reponse, valeur_reponse from reponses where id_question = '{id_question}' order by valeur_reponse desc"

        cls.cursor.execute(query)
        liste_reponse = []
        fetch = cls.cursor.fetchall()
        for row in fetch:
            reponse = Answer(str(row[0]), str(row[1]), str(row[2]), str(row[3]))
            liste_reponse.append(reponse)
        cls.close()
        return liste_reponse

    @classmethod
    def get_theme(cls):
        cls.connect()
        liste_theme = []
        query = "select * from theme"

        cls.cursor.execute(query)
        fetch = cls.cursor.fetchall()
        for row in fetch:
            theme = Theme(str(row[0]), str(row[1]))
            liste_theme.append(theme)
        cls.close()
        return liste_theme
