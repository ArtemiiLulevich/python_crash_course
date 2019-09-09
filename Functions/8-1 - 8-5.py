
def display_message():
    """8-1"""
    print('I am a function !')


def favourite_book(title):
    """8-2"""
    print("One of my favourite books is {}".format(title.title()))


def make_shirt(shirt_size='L', shirt_text='I love Python', shirt_color='Green'):
    """8-3 - 8-4"""
    print("A {} shirt, size - {}, with text - {}".format(shirt_size, shirt_text, shirt_color))


# display_message()
# favourite_book('Neiromancer')

make_shirt('L', 'Hornet')
make_shirt(shirt_text='Fort', shirt_size='XL')
make_shirt()
