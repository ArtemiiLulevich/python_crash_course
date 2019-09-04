for x in range(1, 21):
    print(x)

mil_list = list(range(1,1000001))

print("Min in list: " + str(min(mil_list)))
print("Max in list: " + str(max(mil_list)))
print("Sum of list: " + str(sum(mil_list)))

print("odd numbers list: " + str(list(range(1, 21, 2))))

print("Multiples of 3: " + str(list(range(3, 31, 3))))

for x in range(1, 11):
    print("{} -> {}".format(x, x**3))

list_of_3 = [value**3 for value in range(1, 11)]

print("List by list comprehension: " + str(list_of_3))

