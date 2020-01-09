import unittest

from core.field import Field
from engine.engine import Engine


class MyTestCase(unittest.TestCase):
    def test_engine(self):
        engine = Engine()
        db = engine.create_database("db")

        age = Field("age")
        name = Field("name")
        field_name_map = {"age": age,
                          "name": name}
        table = db.create_table("customer", field_name_map)

        self.assertEqual(table != None, True)

        table.insert({"age": 12, "name":"wenbinhuang"})

        data = engine.execute("select * from customer")
        right_data = [[12]]

        self.assertEqual( all(data[i][j] == right_data[i][j] for i in range(len(right_data)) for j in range(len(right_data[0]))),True)


if __name__ == '__main__':
    unittest.main()
