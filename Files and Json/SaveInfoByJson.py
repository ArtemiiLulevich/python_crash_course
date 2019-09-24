import json

# filename = 'numbers.json'
#
# numbers = list(range(10))
#
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)
#
# # help(json.dump)
#
# with open(filename) as f_obj:
#     nums = json.load(f_obj)
#
# print(nums)

# 10-11

# favour_number = input('Enter your favourite number: ')
#
# filename = 'favourite_number.json'
# with open(filename, 'w') as f_obj:
#     json.dump(favour_number, f_obj)
#
# with open(filename) as f_obj:
#     number = json.load(f_obj)
#
# print("I know you favourite number! It's {}".format(number))

# 10-12

# filename = 'favourite_number.json'
# try:
#     with open(filename) as f_obj:
#         number = json.load(f_obj)
# except FileNotFoundError:
#     favour_number = input('Enter your favourite number: ')
#     with open(filename, 'w') as f_obj:
#         json.dump(favour_number, f_obj)
# else:
#     print("I know you favourite number! It's {}".format(number))

# 10-13


def get_stored_username():
    """Gets stored username if exists."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Gets new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")


def greet_user():
    """Greets user by name."""
    username = get_stored_username()
    if username:
        flag = input("Are you {}?Y/N: ".format(username))
        if flag.lower() == 'y':
            print("Welcome back, " + username + "!")
        else:
            get_new_username()
    else:
        get_new_username()


greet_user()
