import psycopg2
from pprint import pprint

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='..' user='..' host='localhost' password='' port='' ")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to database")

if __name__ == '__main__':
    database_connection = DatabaseConnection()