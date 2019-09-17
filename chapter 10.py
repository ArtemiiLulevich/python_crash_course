# 10 - 1

##file_name = 'learning_Python.txt'
##
##with open(file_name) as file_object:
##    contents = file_object.read()
##    print(contents.rstrip())
##
##print('*' * 79)
##
##with open(file_name) as file_object:
##    for line in file_object:
##        print(line)
##
##print('*' * 79)
##
##with open(file_name) as file_object:
##    lines = file_object.readlines()
##
##for line in lines:
##    print(line)

# 10 - 2

##file_name = 'learning_Python.txt'
##
##with open(file_name) as file_object:
##    lines = file_object.readlines()
##
##for line in lines:
##    print(line.replace('Python', 'C'))

# 10-3 - 10-4

file_name = 'guest_book.txt'

with open(file_name, 'a') as file_object:
    while True:
        guest_name = input('Enter your name: ')
        if guest_name.lower() == 'q':
            break
        print('Hello {}!'.format(guest_name))
        guest_name += '\n'
        file_object.write(guest_name)
