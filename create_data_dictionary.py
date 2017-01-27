import json
import urllib2

# Set up emoji whitelist
dict_f = open('./whitelist_dict.csv', 'r')
output = []
quick_access = ['arrow_right', 'house_with_garden', 'oncoming_bus', 'man', 'woman', 'boy', 'girl', 'cityscape', 'clapper', 'projector', 'tropical_fish', 'heart_eyes', 'loudspeaker', 'new_moon_with_face']

# Load file
emojis_f = urllib2.urlopen('https://raw.githubusercontent.com/Ranks/emojione/master/emoji.json')

# Load json
emojis_json = json.load(emojis_f)
emojis_f.close()

def applyGrammar(meaning):
	try:
		return {'grammartype': meaning.split(':')[0], 'text': meaning.split(':')[1].replace('\r\n', '')}
	except: 
		print meaning
		return {'grammartype': 'error', 'text': meaning}

# Default meanings and current_meaning to keywords and first keyword 
for line in dict_f:
	id = line.split(',')[0]
	meanings = filter(lambda x: ((x != '') and (x != '\r\n')), line.split(',')[1:])
	meanings = map(applyGrammar, meanings)
	try:
		emoji = emojis_json[id]
		emoji['id'] = id
		emoji['meanings'] = meanings
		emoji['currentmeaning'] = meanings[0]
		# Get rid of multi-emojis
		if ('-' in emoji['unicode']):
			emoji['unicode'] = emoji['unicode'].split('-')[0]
		# Set the visibility filter
		emoji['quickaccess'] = True if (id in quick_access) else False
		output.append(emoji)
	except:
		print "Can't find emoji with this id: " + str(id)

dict_f.close()

# Write out
emojis_f = open('./emoji_meaning_v2.json', 'w')
json.dump(output, emojis_f)
