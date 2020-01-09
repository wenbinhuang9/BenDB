from core import FieldKey, FieldType, TYPE_MAP
from core import SerializedInterface

# used to define the field and store the field data
# using List to store the data.
## four basic interfaces, get, update, delete, add
class Field(SerializedInterface):

    def __init__(self, type, key = FieldKey.NULL, default = None):
        self.__type = type
        self.__key = key
        self.__default = default
        self.values = []


    def check_index(self, index):
        if index < 0 or index >= len(self.values):
            ## todo log
            return  False
        return  True

    def check_constraints(self):
        return True
    def check_type(self, val):
        return True

    def get(self, index = None):
        if index == None:
            return self.values
        if not self.check_index(index):
            ## todo log
            return None
        return self.values[index]

    def update(self, index, val):
        if not self.check_index(index):
            ## todo log
            return False

        self.values[index] = val
        return True

    ## it takes linear time here
    def delete(self, index):
        if not self.check_index(index):
            ## todo log
            return False

        self.values.pop(index)
        return True


    def add(self, val):
        self.values.append(val)
        return True

