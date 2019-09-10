# 8-6

##def city_country(city='Donetsk', country='Ukraine'):
##    return "{}, {}".format(city.title(), country.title())
##
##
##print(city_country())
##print(city_country('London', 'UK'))
##print(city_country('Rio', 'Brazile'))


# 8-7

##def make_album(artist_name, album_name, tracks = ''):
##    album = {'artist' : artist_name, 'name' : album_name}
##    if tracks:
##        album['tracks'] = tracks
##    return album
##
##
##print(make_album('AC/DC', 'Back in black'))
##print(make_album('AC/DC', 'Back in black', 10))

# 8-8

##while True:
##    artist = input('Enter an artist name: ')
##    if artist.lower() == 'q':
##        break
##
##    album = input('Enter an album name: ')
##    if album.lower() == 'q':
##        break
##
##    print(make_album('AC/DC', 'Back in black'))


# 8-9
def show_magicians(mag_list):
    for mag in mag_list:
        print(mag.title())


def make_great(mag_list):
    great_mags_list = []
    for mag in mag_list:
        great_mags_list.append('Great ' + mag)
    return great_mags_list
    
        

mags = ['Philip', 'Alex', 'Leo']
##make_great()
show_magicians(make_great(mags))

