##person = {
##    'first_name' : 'Artemii',
##    'last_name' : 'Lulevich',
##    'age' : '24',
##    'city' :'Donetsk'
##    }
##
##print("First name is: {}".format(person.items()))
##
##for key, value in person.items():
##    print('{} -> {}'.format(key, value))
##
##favorite_languages = {
##    'jen': ['python', 'ruby'],
##    'sarah': ['c'],
##    'edward': ['ruby', 'go'],
##    'phil': ['python', 'haskell'],
##    }
##
##for name, languages in favorite_languages.items():
##    if len(languages) <= 1:
##        print("\n {}’s favorite language is:".format(name.title()))
##    else:
##        print("\n" + name.title() + "'s favorite languages are:")
##    for language in languages:
##        print("\t" + language.title())

Bonka = {'family' : 'cat',
         'owner' : 'Artemii'
         }

Mashka = {'family' : 'cat',
         'owner' : 'Larisa'
         }

Maska = {'family' : 'cat',
         'owner' : 'Mary'
         }

Bobik = {'family' : 'dog',
         'owner' : 'none'
         }

pets = [Bonka, Mashka, Maska, Bobik]
##print(pets)
for pet in pets:
    print("\nName is ")
    for info_1, info_2 in pet.items():
        print('{} : {}'.format(info_1.title(), info_2.title()))
