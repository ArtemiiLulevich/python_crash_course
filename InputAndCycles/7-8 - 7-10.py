# 7-8
##sandwich_orders = ['Tuna', 'Bacon', 'Fruit', 'Vegan']
##
##finished_sandwiches = []
##
##while sandwich_orders:
##    current_sandwich = sandwich_orders.pop()
##    print('I made your {} sandwich'.format(current_sandwich))
##    finished_sandwiches.append(current_sandwich)
##print('Created sandwiches: ', end=' ')
##for sandwich in finished_sandwiches:
##    print(sandwich, end=' ')


# 7-9
##sandwich_orders = ['pastrami', 'Bacon','pastrami', 'Fruit', 'Vegan', 'pastrami']
##
##x = 'pastrami'
##
##finished_sandwiches = []
##print('Pastrami is out of stock')
##
##while x in sandwich_orders:
##    sandwich_orders.remove(x)
##
##while sandwich_orders:
##    current_sandwich = sandwich_orders.pop()
##    print('I made your {} sandwich'.format(current_sandwich))
##    finished_sandwiches.append(current_sandwich)
##print('Created sandwiches: ', end=' ')
##for sandwich in finished_sandwiches:
##    print(sandwich, end=' ')

#7-10

num_of_persons = input('Enter number of persons: ')
data = {}
for person in range(int(num_of_persons)):
    name = input('Enter your name: ')
    city = input('Enter your favorit city: ')
    data[name] = city

print(data)
