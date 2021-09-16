from wer import add_song
import pprint

pop = ['good_4_u', 'levitating', 'watermelon_sugar', 'wildest_dreams', 'thriller']
rock = ['american_idiot', 'born_to_be_wild', 'dont_stop_believing', 'i_love_rock_and_roll', 'you_shook_me_all_night_long']
rnb = ['adorn', 'hotline_bling', 'kiss_me_more', 'one_two_step', 'umbrella']
special = ['rap_god']
all = pop + rock + rnb + special

pop_dict = {}
rock_dict = {}
rnb_dict = {}
eminem = {}

# calculate average values for each of the error rates for each
# find min and max
for song in pop:
    add_song(song, pop_dict)

for song in rock:
    add_song(song, rock_dict)

for song in rnb:
    add_song(song, rnb_dict)

for song in special:
    add_song(song, eminem)

def song_w_highest(err, _dict):
    higher = 0
    name = ""
    for song in _dict:
        if _dict[song][err] > higher:
            name = song
            higher = _dict[song][err] 
    return name, higher

def song_w_lowest(err, _dict):
    lowest = 1.0
    name = ""
    for song in _dict:
        if _dict[song][err] < lowest:
            name = song
            lowest = _dict[song][err] 
    return name, lowest

def _sort(_dict, kw):
    return sorted(_dict.items(), key = lambda x: x[1][kw])

def avg(_dict, kw):
    sum = 0
    for entry in _dict:
        sum += _dict[entry][kw]
    return sum/len(_dict)

print(song_w_highest('wer', eminem))
print(song_w_lowest('wer', eminem))
pprint.pprint(_sort(eminem, 'wer'))
print(avg(eminem, 'wer'))

print(song_w_highest('wer', pop_dict))
print(song_w_lowest('wer', pop_dict))
pprint.pprint(_sort(pop_dict, 'wer'))
print(avg(pop_dict, 'wer'))

print(song_w_highest('wer', rock_dict))
print(song_w_lowest('wer', rock_dict))
pprint.pprint(_sort(rock_dict, 'wer'))
print(avg(rock_dict, 'wer'))

print(song_w_highest('wer', rnb_dict))
print(song_w_lowest('wer', rnb_dict))
pprint.pprint(_sort(rnb_dict, 'wer'))
print(avg(rnb_dict, 'wer'))