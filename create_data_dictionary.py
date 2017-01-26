import json
import urllib2

# Load file
emojis_f = urllib2.urlopen('https://raw.githubusercontent.com/Ranks/emojione/master/emoji.json')

# Load json
emojis_json = json.load(emojis_f)
emojis_f.close()

# Default meanings and current_meaning to keywords and first keyword 
for k in emojis_json.keys():
	emojis_json[k]['id'] = k
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

setMeaningsAndDefaultMeaning('prince', ['the prince', 'the king', 'the knight', 'the boy', 'the hero'], 'the prince')
setMeaningsAndDefaultMeaning('princess', ['the princess', 'the girl', 'the hero'], 'the princess')
setMeaningsAndDefaultMeaning('dragon', ['the dragon', 'the monster', 'the enemy'], 'the dragon')
setMeaningsAndDefaultMeaning('heart', ['love', 'the heart'], 'love')
setMeaningsAndDefaultMeaning('thunder_cloud_rain', ['the storm', 'the rain', 'sad', 'scared', 'scary'], 'the storm')
setMeaningsAndDefaultMeaning('dog', ['the dog', 'the pug', 'the friend'], 'the dog')
setMeaningsAndDefaultMeaning('hugging', ['the hug', 'safe', 'secure'], 'the hug')

output = []

for k in emojis_json.keys():
	output.append(emojis_json[k])


# Write out
emojis_f = open('./emoji_meaning.json', 'w')
json.dump(output, emojis_f)
