# 9-1

##class Restaurant():
##    """Simple restaurant model"""
##
##    def __init__(self, restaurant_name, cuisine_type):
##        self.name = restaurant_name
##        self.cuisine = cuisine_type
##
##
##    def describe_restaurant(self):
##        print("Restaurant name - {}, cuisine type - {}.".format(self.name, self.cuisine))
##
##
##    def open_restaurant(self):
##        print("Restaurnat {} is open.".format(self.name))
##
### 9-2
##restaurant_italian = Restaurant('Domino', 'Italian')
##restaurant_china = Restaurant('Kung-Fu', 'China')
##restaurant_russian = Restaurant('Balalaika', 'Russian')
####print(restaurant.name)
####print(restaurant.cuisine)
##restaurant_italian.describe_restaurant()
##restaurant_china.describe_restaurant()
##restaurant_russian.describe_restaurant()
####restaurant.open_restaurant()


# 9-3
class User():
    """Simple user model"""


    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("{} {}, age {}".format(self.last_name, self.first_name, self.age))


    def greet_user(self):
        print("Hello, {}!".format(self.first_name))


user = User('Artemii', 'Lulevich', 24)
user.describe_user()
user.greet_user()
    
