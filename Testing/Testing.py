import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('artemii', 'lulevich')
        self.assertEqual(formatted_name, 'Artemii Lulevich')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('artemii', 'lulevich', 'andreevich')
        self.assertEqual(formatted_name, 'Artemii Andreevich Lulevich')


if __name__ == '__main__':
    unittest.main()

