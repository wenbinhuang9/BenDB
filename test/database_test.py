import unittest

from core.database import Database
from core.field import Field


class MyTestCase(unittest.TestCase):
    def test_creating_table(self):
        db = Database("db")
        age = Field("age")
        name = Field("name")
        field_name_map = {"age": age,
                          "name": name
                          }

        table = db.create_table("customer", field_name_map)

        self.assertEqual(table != None, True)

        table.add_field("age", age)

        table.insert({"age": 12})
        data = table.search(["age"])
        right_data = [[12]]

        self.assertEqual(all(data[i][j] == right_data[i][j] for i in range(len(right_data)) for j in range(len(right_data[0]))), True)



if __name__ == '__main__':
    unittest.main()
