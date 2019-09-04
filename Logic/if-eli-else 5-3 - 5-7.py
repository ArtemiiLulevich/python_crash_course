"""Ex. 5-8 - 5-11"""
names_list = ['admin', 'artem', 'kolya', 'vasia', 'igor']

# 5-8
# if names_list:
#     for name in names_list:
#         if name.lower() == 'admin':
#             print('Hello admin, would you like to see a status report?')
#         else:
#             print("Hello {}, thank you for logging in again".format(name))
# else:
#     print("We need to find some users!")

new_users = ['Kolya', 'VASIA', 'Erik', "Bonka"]
# 5-10
# for user in new_users:
#     if user.lower() in names_list:
#         print("This user is present in system.")
#     else:
#         print("Hello new user!")

# 5-11
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print("{}th".format(number))
