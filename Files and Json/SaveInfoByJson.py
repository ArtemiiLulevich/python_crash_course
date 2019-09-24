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

favour_number = input('Enter your favourite number: ')

filename = 'favourite_number.json'
with open(filename, 'w') as f_obj:
    json.dump(favour_number, f_obj)

with open(filename) as f_obj:
    number = json.load(f_obj)

print("I know you favourite number! It's {}".format(number))
