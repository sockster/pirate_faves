"""
ask each question, user replies yes or no; store a random ingredient 
from each correlating category - random.choice(ingredients.strong) (?)
create new dictionary
save type of ingredient (key?) to new dictionary, and corresponding ingredient as well

dictionary questions; dictionary of ingredients lists
create a counter (count)
create empty dict for drink_descr; append w/ y descriptions  Optional?
create empty dict list for drink_ingr; append w/ y ingredients

while count <= 5
- ask each question
- append drink_ingr list
- count += 1
repeat up to count =ing 5 and then cease looping
"""




import random


ingredients = {
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	"sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


questions = {
	"strong": "Do ye like yer drinks strong?",
	"salty": "Do ye like it with a salty tang?",
   	"bitter": "Are ye a lubber who likes it bitter?",
   	"sweet": "Would ye like a bit of sweetness with yer poison?",
   	"fruity": "Are ye one for a fruity finish?"
}


"""    just testing ... all of these work
print questions["strong"]
print drink_desc
print drink_ingr
ingredients["tart"] = "add lime"		<--- adds "tart": ["add lime"] to ingredients dictionary

"""	



def drinks():
	print questions["strong"]
	print ("Y or N?")
	strong_ans = raw_input()
	if strong_ans == "Y" or "y":
		print "Aye!",
		drink_desc[(random.choice(ingredients["strong"]))] = "strong"
	elif strong_ans == "N" or "n":
		print "Arrgh!"
	else:
		print "Ye son of a biscuit eater! Be ye tryin' to scuttle me rum makin'?"

	print questions["salty"]
	print ("Y or N?")
	salty_ans = raw_input()
	if salty_ans == "Y" or "y":
		print "Aye!",
		drink_desc[(random.choice(ingredients["salty"]))] = "salty"
	elif salty_ans == "N" or "n":
		print "Arrgh!"
	else:
		print "Ye scurvy landlubber! Be ye tryin' to scuttle me rum makin'?"
	
	print questions["bitter"]
	print ("Y or N?")
	bitter_ans = raw_input()
	if bitter_ans == "Y" or "y":
		print "Aye!",
		drink_desc[(random.choice(ingredients["bitter"]))] = "bitter"
	elif bitter_ans == "N" or bitter_ans == "n":
		print "Arrgh!"
	else:
		print "Ye scabby weasel! Be ye tryin' to scuttle me rum makin'?"
		
	print questions["sweet"]
	print ("Y or N?")
	sweet_ans = raw_input()
	if sweet_ans == "Y" or "y":
		print "Aye!",
		drink_desc[(random.choice(ingredients["sweet"]))] = "sweet"
	elif sweet_ans == "N" or "n":
		print "Arrgh!"
	else:
		print "Ye gin-soaked sot! Be ye tryin' to scuttle me rum makin'?"

	print questions["fruity"]
	print ("Y or N?")
	fruity_ans = raw_input()
	if fruity_ans == "Y" or "y":
		print "Aye!",
		drink_desc[(random.choice(ingredients["fruity"]))] = "fruity"
	elif fruity_ans == "N" or "n":
		print "Arrgh!"
	else:
		print "Ye grog-faced swabby! Be ye tryin' to scuttle me rum makin'?"

	
	
	





seconds = ""

if __name__ == '__main__':
	drink_desc = {}
	drinks()
	print "Aye, yer one hard drinker matey! So, I'll mix ye up a ",
	print str(drink_desc.values()) + " ",
	print "fancy drink fer ye."
	print ""
	
	print "I be puttin' in some ",
	print drink_desc.keys()
	print ""
	print ""
	
"""
	while seconds == "Y" or "y":
		print "Fancy ye another?"
		seconds = raw_input()	
		if seconds == "Y" or "y":
			drinks()
		else:
			print "Then g'night to ye!"

"""



