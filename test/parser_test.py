import unittest

from parser.parser import Parser
class MyTestCase(unittest.TestCase):
    def test_parse_select(self):
        select = "select * from me where a=1 and b=2"
        p = Parser()
        res = p.parse(select)
        print(res)
        self.assertEqual(res["type"] == "search", True)
        self.assertEqual(res["fields"] == "*", True)
        self.assertEqual(res["table"] == "me", True)

        select = "select a, b, c from me where a=1 and b=2"
        res = p.parse(select)
        print(res)
        field = ["a", 'b', 'c']
        return_filed = res["fields"]
        self.assertEqual(all( field[i] == return_filed[i] for i in range(len(return_filed))), True)

    def test_parse_update(self):
        update = "update me  set a = 2, b = 3"
        p = Parser()
        res = p.parse(update)
        print(res)

        self.assertEqual(res["type"] == "update", True)

        update_val = {"a":"2", "b":"3"}
        return_update_val = res["fields"]
        self.assertEqual(all(update_val[key] == return_update_val[key] for key in update_val.keys()), True)
        self.assertEqual(res["table"] == "me", True)

    def test_parse_insert(self):
        insert = "insert into me (a,b) values (2,3)"

        p = Parser()
        res = p.parse(insert)
        print(res)

        insert_val = {"a":"2", "b":"3"}
        return_insert_val = res["fields"]
        self.assertEqual(all(insert_val[key] == return_insert_val[key] for key in insert_val.keys()), True)

        self.assertEqual(res["type"] == "insert", True)
        self.assertEqual(res["table"] == "me", True)

if __name__ == '__main__':
    unittest.main()
