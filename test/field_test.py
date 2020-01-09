import unittest

from core import FieldType
from core.field import Field


class MyTestCase(unittest.TestCase):
    def test_field_add(self):
        field = Field(FieldType.int)

        self.assertEqual(field.add(1), True)
        print(field.values)
        print(field.get(0))
        self.assertEqual(field.get(0) == 1, True)

        field.add(2)

        l = [1, 2]
        return_l = field.get()
        self.assertEqual(all(l[i] == return_l[i] for i in range(len(l))), True)
        

if __name__ == '__main__':
    unittest.main()
