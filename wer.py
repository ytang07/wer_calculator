import jiwer
import pprint

transformation = jiwer.Compose([
    jiwer.ToLowerCase(),
    jiwer.SentencesToListOfWords(word_delimiter=" "),
    jiwer.RemovePunctuation(),
    jiwer.RemoveEmptyStrings(),
])

results = {}
songs = ['adorn', 'american_idiot', 'born_to_be_wild', 'dont_stop_believing',
    'good_4_u', 'hotline_bling', 'i_love_rock_and_roll', 'kiss_me_more',
    'levitating', 'one_two_step', 'rap_god', 'thriller', 'umbrella', 
    'watermelon_sugar', 'wildest_dreams', 'you_shook_me_all_night_long']
def add_song(song_name, _dict):
    _dict[song_name] = {}
    transcribed = song_name + '.txt'
    official = song_name + '_official.txt'

    with open(transcribed, 'r') as _file:
        t_text = _file.read()

    with open(official, 'r') as _file:
        o_text = _file.read()

    o_text = o_text.replace('\n', '')


    errors = jiwer.compute_measures(truth=o_text, hypothesis=t_text, truth_transform=transformation, hypothesis_transform=transformation)
    _dict[song_name]['mer'] = errors['mer']
    _dict[song_name]['wer'] = errors['wer']
    _dict[song_name]['wil'] = errors['wil']
    _dict[song_name]['wip'] = errors['wip']

def main():
    for song in songs:
        add_song(song, results)
    # pprint.pprint(results)

    for entry in results:
        print(entry)
        for er in results[entry]:
            print(f"\t{er} {results[entry][er]}")

if __name__ == '__main__':
    main()

# print(transformation(o_text))
# print(transformation(t_text))