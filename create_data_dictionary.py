import json
import urllib2

# Set up emoji whitelist
whitelist = ['grinning','grin','joy','rofl','smiley','sweat_smile','laughing','wink','blush','yum','sunglasses','heart_eyes','kissing_heart','kissing','kissing_smiling_eyes','kissing_closed_eyes','relaxed','slight_smile','hugging','thinking','neutral_face','no_mouth','rolling_eyes','disappointed_relieved','open_mouth','zipper_mouth','sleeping','nerd','stuck_out_tongue_winking_eye','frowning2','astonished','disappointed','worried','triumph','cry','sob','scream','dizzy_face','rage','innocent','cowboy','clown','lying_face','mask','thermometer_face','head_bandage','nauseated_face','sneezing_face','smiling_imp','skull','ghost','alien','robot','poop','smiley_cat','boy','girl','man','woman','older_man','older_woman','angel','cop','spy','guardsman','construction_worker','man_with_turban','santa','princess','prince','bride_with_veil','man_in_tuxedo','pregnant_woman','no_good','ok_woman','information_desk_person','bow','face_palm','shrug','walking','runner','muscle','point_left','point_right','point_up','v','vulcan','metal','call_me','ok_hand','thumbsup','thumbsdown','punch','wave','clap','raised_hands','pray','nail_care','kiss','zzz','eyeglasses','dark_sunglasses','necktie','shirt','jeans','dress','kimono','womans_clothes','handbag','school_satchel','athletic_shoe','high_heel','boot','crown','tophat','lipstick','ring','closed_umbrella','briefcase',
'see_no_evil','hear_no_evil','speak_no_evil','sweat_drops','dash','dog','poodle','wolf','fox','cat','lion_face','tiger','horse','unicorn','cow','pig','boar','ram','sheep','dromedary_camel','camel','elephant','rhino','mouse','hamster','rabbit','bat','bear','koala','panda_face','chicken','hatching_chick','bird','dove','eagle','owl','crocodile','turtle','snake','dragon','whale','dolphin','tropical_fish','shark','octopus','crab','butterfly','snail','bee','beetle','spider_web','scorpion','rose','bouquet','sunflower','tulip','evergreen_tree','palm_tree','cactus','herb','shamrock','maple_leaf','mushroom','earth_africa','new_moon_with_face','first_quarter_moon_with_face','sunny','full_moon_with_face','star','cloud','partly_sunny','thunder_cloud_rain','white_sun_rain_cloud','cloud_rain','cloud_snow','cloud_lightning','cloud_tornado','umbrella','zap','snowflake','fire','ocean','christmas_tree','snowman']

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
	whitelist.append(id)
	emojis_json[id]['meanings'] = meanings
	emojis_json[id]['currentmeaning'] = default_meaning

setMeaningsAndDefaultMeaning('prince', ['the prince', 'the king', 'the knight', 'the boy', 'the hero'], 'the prince')
setMeaningsAndDefaultMeaning('princess', ['the princess', 'the girl', 'the hero'], 'the princess')
setMeaningsAndDefaultMeaning('dragon', ['the dragon', 'the monster', 'the enemy'], 'the dragon')
setMeaningsAndDefaultMeaning('heart', ['love', 'the heart'], 'love')
setMeaningsAndDefaultMeaning('thunder_cloud_rain', ['the storm', 'the rain', 'sad', 'scared', 'scary'], 'the storm')
setMeaningsAndDefaultMeaning('dog', ['the dog', 'the pug', 'the friend'], 'the dog')
setMeaningsAndDefaultMeaning('hugging', ['the hug', 'safe', 'secure'], 'the hug')
setMeaningsAndDefaultMeaning('arrow_right', ['right', 'leave'], 'right')
setMeaningsAndDefaultMeaning('house_with_garden', ['the house', 'home'], 'the house')
setMeaningsAndDefaultMeaning('walking', ['walking', 'hiking', 'the pedestrian'], 'walking')
setMeaningsAndDefaultMeaning('oncoming_bus', ['the bus', 'public transport'], 'the bus')
setMeaningsAndDefaultMeaning('cityscape', ['the city', 'the town', 'the building'], 'the city')
setMeaningsAndDefaultMeaning('clapper', ['the cinema', 'the movie', 'hollywood'], 'the cinema')
setMeaningsAndDefaultMeaning('projector', ['the projector', 'the movie'], 'the projector')
setMeaningsAndDefaultMeaning('new_moon_with_face', ['the moon', 'dark'], 'the moon')
setMeaningsAndDefaultMeaning('loudspeaker', ['loud', 'the loudspeaker'], 'loud')
setMeaningsAndDefaultMeaning('heart_eyes', ['love', 'enjoy'], 'love')
setMeaningsAndDefaultMeaning('frowning2', ['sad', 'frowning'], 'sad')
setMeaningsAndDefaultMeaning('rofl', ['lol', 'rofl'], 'lol')
setMeaningsAndDefaultMeaning('cowboy', ['the cowboy'], 'cowboy')
setMeaningsAndDefaultMeaning('lying_face', ['lie', 'Pinocchio'], 'lie')
setMeaningsAndDefaultMeaning('nauseated_face', ['sick', 'unwell'], 'sick')
setMeaningsAndDefaultMeaning('sneezing_face', ['sick', 'sneeze', 'cold'], 'sick')
setMeaningsAndDefaultMeaning('man_in_tuxedo', ['the suit', 'well-dressed'], 'groom')
setMeaningsAndDefaultMeaning('pregnant_woman', ['pregnant', 'pregnant woman'], 'pregnant')
setMeaningsAndDefaultMeaning('face_palm', ['embarrassed', 'exasperated', 'the facepalm'], 'embarassed')
setMeaningsAndDefaultMeaning('shrug', ['don\'t care', 'the shrug', 'don\'t know'], 'don\'t care')
setMeaningsAndDefaultMeaning('call_me', ['call me'], 'call me')
setMeaningsAndDefaultMeaning('fox', ['the fox'], 'the fox')
setMeaningsAndDefaultMeaning('rhino', ['the rhino'], 'the rhino')
setMeaningsAndDefaultMeaning('bat', ['the bat'], 'the bat')
setMeaningsAndDefaultMeaning('eagle', ['the eagle'], 'the eagle')
setMeaningsAndDefaultMeaning('owl', ['the owl'], 'the owl')
setMeaningsAndDefaultMeaning('shark', ['the shark'], 'the shark')
setMeaningsAndDefaultMeaning('butterfly', ['the butterfly'], 'the butterfly')
setMeaningsAndDefaultMeaning('clown', ['the clown'], 'the clown')

output = []

for k in whitelist:
	if (emojis_json[k]['currentmeaning'] == ''):
		print k
	if ('-' not in emojis_json[k]['unicode']):
		output.append(emojis_json[k])


# Write out
emojis_f = open('./emoji_meaning.json', 'w')
json.dump(output, emojis_f)
