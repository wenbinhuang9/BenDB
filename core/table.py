
### manage field
### manage data, insert, query, update data.
from core import SerializedInterface


class Table(SerializedInterface):

    ## what is the options?
    def __init__(self, field_map):
        self.__field_name = []
        self.__filed_name_obj_map = {}

        for k, v in field_map.items():
            self.add_field(k, v)

    ##todo  when adding new field how to adding the old data
    def add_field(self, fieldname, filedobj):
        self.__field_name.append(fieldname)
        self.__filed_name_obj_map[fieldname] = filedobj

    ## todo implementation
    def delete_field(self, fieldname):
        return None

    ## todo support
    def update_field(self, fieldname):
        return None

    ## condition (func, field, val)
    ## there should be index for optimization
    ## todo using condition
    ## todo support sort
    def search(self, fields, sort=None, format_type=None, condition=None):
        if fields == "*":
            fields = self.__field_name

        field_data = []
        for field in fields:
            field_data.append(self.__filed_name_obj_map[field].get())

        if len(field_data) == 0:
            return []
        print(field_data)
        return [[f[i] for f in field_data] for i in range(len(field_data[0]))]



    ## data: map, (fieldname, val)
    ## todo no concurrency control
    def insert(self, data):
        for field_name, value in data.items():
            res = self.__filed_name_obj_map[field_name].add(value)
            if res == False:
                ## todo log
                return False
        return  True

    def delete(self):
        return True

    def update(self):
        return True