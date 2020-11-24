import mysql.connector

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