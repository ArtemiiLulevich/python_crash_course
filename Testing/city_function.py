def city_country(city, country, population=''):
    """Function returns formatted city name."""
    if population:
        formatted_city = '{}, {} - population {}.'.format(city, country, population)
    else:
        formatted_city = '{}, {}'.format(city, country)
    return formatted_city.title()
