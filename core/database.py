
## object of database

## create database
## manage table
from core import SerializedInterface
from core.table import Table


class Database(SerializedInterface):

    def __init__(self, name):
        self.__name = name
        self.__table_list = []
        self._table_obj_map = {}


    ## field_map : fieldname, fieldobj
    def create_table(self, table, field_map):
        if table in self.__table_list:
            ## todo log
            return self._table_obj_map[table]

        self.__table_list.append(table)
        table_obj = Table(field_map)
        self._table_obj_map[table] = table_obj

        return table_obj


    def drop_table(self):
        return True

