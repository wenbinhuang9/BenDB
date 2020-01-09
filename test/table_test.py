import unittest

from core.field import Field
from core.table import Table


class MyTestCase(unittest.TestCase):
    def test_create_table(self):
        age = Field("age")
        name = Field("name")
        field_name_map = {"age": age,
                          "name": name
                          }
        table = Table(field_name_map)

        table.insert({"name": "wenbinhuang", "age":26})

        fileds = ["age", "name"]
        return_row  = table.search(fileds)
        print(return_row)
        cur_row = [[26, "wenbinhuang"]]

        self.assertEqual(all(return_row[i][j] == cur_row[i][j] for i in range(len(cur_row)) for j in range(len(cur_row[0]))), True)

        table.insert({"name" : "yyyy", "age": 123})
        cur_row = [[26, "wenbinhuang"], [123, "yyyy"]]
        return_row = table.search(fileds)
        print(return_row)
        self.assertEqual(all(return_row[i][j] == cur_row[i][j] for i in range(len(cur_row)) for j in range(len(cur_row[0]))), True)


if __name__ == '__main__':
    unittest.main()
