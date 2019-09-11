# 8 - 12
def in_sandwich(*components):
    """Function with an arbitrary set of parameters"""
    print("\nSandwich contains: ")
    for component in components:
        print("\t- {};".format(component))


##in_sandwich('Tuna')
##in_sandwich('Tuna', 'Becon')
##in_sandwich('Tuna', 'Vaga', 'Spam', 'Eggs')

# 8 - 14
def car_info(creator, model, **other):
    car = {}
    car['Creator'] = creator
    car['Model'] = model
    for key, value in other.items():
        car[key] = value
    for key, value in car.items():
        print('{} -> {}'.format(key, value))
##    return car


car_info('Ferrari', 'Enzo')
car_info('Ferrari', 'Enzo', l = 4702, w = 2035, h = 1147)
