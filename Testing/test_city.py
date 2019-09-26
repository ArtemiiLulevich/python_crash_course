import unittest
from city_function import city_country


class CityCountryTests(unittest.TestCase):

    def test_city_country(self):
        city_and_country = city_country('Kiev', 'ukraine')
        self.assertEqual(city_and_country, 'Kiev, Ukraine')

    def test_city_country_population(self):
        city_and_country = city_country('Kiev', 'ukraine', '50000')
        self.assertEqual(city_and_country, 'Kiev, Ukraine - Population 50000.')


if __name__ == '__main__':
    unittest.main()
