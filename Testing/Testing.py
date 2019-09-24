import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('artemii', 'lulevich')
        self.assertEqual(formatted_name, 'Artemii Lulevich')


if __name__ == '__main__':
    unittest.main()
# import unittest
#
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # Проверим, что s.split не работает, если разделитель - не строка
#         with self.assertRaises(TypeError):
#             s.split(2)
#
#
# if __name__ == '__main__':
#     unittest.main()
