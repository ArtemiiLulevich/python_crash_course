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

##class User():
##    """Simple user model"""
##
##
##    def __init__(self, first_name, last_name, age):
##        self.first_name = first_name
##        self.last_name = last_name
##        self.age = age
##
##    def describe_user(self):
##        print("{} {}, age {}".format(self.last_name, self.first_name, self.age))
##
##
##    def greet_user(self):
##        print("Hello, {}!".format(self.first_name))
##
##
##user = User('Artemii', 'Lulevich', 24)
##user.describe_user()
##user.greet_user()


# 9-4

##class Restaurant():
##    """Simple restaurant model"""
##
##    def __init__(self, restaurant_name, cuisine_type):
##        self.name = restaurant_name
##        self.cuisine = cuisine_type
##        self.number_served = 0
##
##
##    def describe_restaurant(self):
##        print("Restaurant name - {}, cuisine type - {}.".format(self.name, self.cuisine))
##
##
##    def open_restaurant(self):
##        print("Restaurnat {} is open.".format(self.name))
##
##
##    def set_number_served(self, served):
##        self.number_served = served
##
##
##    def increment_number_served(self, x):
##        self.number_served += x
##
##
##restaurant_italian = Restaurant('Domino', 'Italian')
##print("Served: {}".format(restaurant_italian.number_served))
##restaurant_italian.set_number_served(5)
##print("Served: {}".format(restaurant_italian.number_served))
##restaurant_italian.increment_number_served(19)
##print("Served: {}".format(restaurant_italian.number_served))

#9-5

##class User():
##    """Simple user model"""
##
##
##    def __init__(self, first_name, last_name, age):
##        self.first_name = first_name
##        self.last_name = last_name
##        self.age = age
##        self.login_attempts = 0
##
##    def describe_user(self):
##        print("{} {}, age {}".format(self.last_name, self.first_name, self.age))
##
##
##    def greet_user(self):
##        print("Hello, {}!".format(self.first_name))
##
##
##    def increment_login_attempts(self):
##        self.login_attempts += 1
##
##
##    def reset_login_attempts(self):
##        self.login_attempts = 0
##
##
##user = User('Artemii', 'Lulevich', 24)
##for x in range(4):
##    user.increment_login_attempts()
##print("Numbers of login: {}".format(user.login_attempts))
##user.reset_login_attempts()
##print("Numbers of login: {}".format(user.login_attempts))

#9-6

##class Restaurant():
##    """Simple restaurant model"""
##
##    def __init__(self, restaurant_name, cuisine_type):
##        self.name = restaurant_name
##        self.cuisine = cuisine_type
##        self.number_served = 0
##
##
##    def describe_restaurant(self):
##        print("Restaurant name - {}, cuisine type - {}.".format(self.name, self.cuisine))
##
##
##    def open_restaurant(self):
##        print("Restaurnat {} is open.".format(self.name))
##
##
##    def set_number_served(self, served):
##        self.number_served = served
##
##
##    def increment_number_served(self, x):
##        self.number_served += x
##
##
##class IceCreamStand(Restaurant):
##    """Simple Ice cream stand Class"""
##    def __init__(self, restaurant_name, cuisine_type):
##        super().__init__(restaurant_name, cuisine_type)
##        self.flavors = ['Lemon', 'Mango']
##
##
##    def iceCream_list(self):
##        print('We have:')
##        for iceCream in self.flavors:
##            print('\t- {}'.format(iceCream))
##
##                  
##iceCream_stand = IceCreamStand('Bom-Bom', 'Icecream')
##iceCream_stand.iceCream_list()

# 9-7 - 9-8
class User:
    """Simple user model"""

    def __init__(self, first_name, last_name, age = 18):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("{} {}, age {}".format(self.last_name, self.first_name, self.age))

    def greet_user(self):
        print("Hello, {}!".format(self.first_name))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """Simple admin Class"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    """Simple privileges class"""
    def __init__(self, delete=False, add=True, ban=False):
        self.privileges = {'delete_users' : delete, 'add_post' : add, 'ban_users' : ban}

    def show_privileges(self):
        print('Admin can: ')
        for key, value in self.privileges.items():
            print('\t - {} : {}'.format(key, value))


admin = Admin('Artemii', 'Lulevich')
admin.privileges.show_privileges()
print(admin.age)


