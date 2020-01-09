## manage the database
## query, update , insert, add data to the database.
## the entry to create database, table, and do data management manipilation.
from core.database import Database
from parser.parser import Parser

##1. todo , adding create table parser
## todo 2. adding pretty to show the data to the terminal
## todo 3. adding data constrainst to each field.
class Engine:
    def __init__(self, db_name=None, path='db.data'):
        self.__database_objs = {}
        self.__database_names = []
        self.__current_db = None
        self.path = path

        self.__action_map = {
            "search": self.__search
        }


    def create_database(self, name):
        if name in self.__database_names:
            ## todo log
            return None

        self.__database_names.append(name)
        db = Database(name)
        self.__database_objs[name] = db
        ##todo just for test here
        self.__current_db = db
        return db

    def __get_table(self, table_name):
        table =  self.__current_db._table_obj_map[table_name]

        return table
    def __search(self, query):
        table = self.__get_table(query["table"])
        fields = query["fields"]

        return table.search(fields, None, None, None)

    def execute(self, statement):

        action = Parser().parse(statement)

        ret = None

        if action['type'] in self.__action_map:

            ret = self.__action_map.get(action['type'])(action)

        return ret

