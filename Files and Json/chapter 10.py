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

# 10-6

##while True:
##    print("Enter two numbers to see sum. Enter q to exit.")
##
##    a = input('Enter first number: ')
##    if a.lower() == 'q':
##        break
##    b = input('Enter second number: ')
##    if b.lower() == 'q':
##        break
##    
##    try:
##        son = int(a) + int(b)
##    except ValueError:
##        print('One of the numbers is a letter')
##    else:
##        print('Sum is {}'.format(son))

#10-8

##def animals(filename):
##    try:
##        with open(filename) as file_obj:
##            line = file_obj.readline()
##            while line:
##                print(line, end='')
##                line = file_obj.readline()
##            print('\n')
##    except FileNotFoundError:
##        pass
####        msg = 'File {} not found'.format(filename)
####        print(msg)
##
##files = ['cats.txt', 'dogs.txt']
##for file in files:
##    animals(file)

#10-10


def count_of_words(filename, word):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        msg = 'File {} not found'.format(filename)
        print(msg)
    else:
        # count_of_words = contents.lower().count(word.lower())
        list_of_words = contents.split()
        len_of_book = len(list_of_words)
        # print("Count of word '{}' in  file {}: {}".format(word, filename, count_of_words))
        print("{} - {}".format(filename, len_of_book))


files = ['Dracula.txt', 'Iliad.txt']
for file in files:
    count_of_words(file, '')

