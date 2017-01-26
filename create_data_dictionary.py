import json
import urllib2

# Load file
emojis_f = urllib2.urlopen('https://raw.githubusercontent.com/Ranks/emojione/master/emoji.json')

# Load json
emojis_json = json.load(emojis_f)
emojis_f.close()

# Default meanings and current_meaning to keywords and first keyword 
for k in emojis_json.keys():
	if 'keywords' in emojis_json[k].keys() and len(emojis_json[k]['keywords']) > 0:
		# print emojis_json[k]['keywords'][0]
		emojis_json[k]['meanings'] = emojis_json[k]['keywords']
		emojis_json[k]['currentmeaning'] = emojis_json[k]['keywords'][0]
	else:
		emojis_json[k]['meanings'] = ['']
		emojis_json[k]['currentmeaning'] = ''

# Overwrite the data we need
def setMeaningsAndDefaultMeaning(id, meanings, default_meaning):
	emojis_json[id]['meanings'] = meanings
	emojis_json[id]['currentmeaning'] = default_meaning


setMeaningsAndDefaultMeaning('prince', ['the prince', 'the king', 'the knight', 'the boy'], 'the prince')
setMeaningsAndDefaultMeaning('princess', ['the princess', 'the girl'], 'the princess')
setMeaningsAndDefaultMeaning('dragon', ['the dragon', 'the monster', 'the enemy'], 'the dragon')
setMeaningsAndDefaultMeaning('heart', ['love', 'the heart', 'loves'], 'love')


# Write out
emojis_f = open('./emoji_meaning.json', 'w')
json.dump(emojis_json, emojis_f)
