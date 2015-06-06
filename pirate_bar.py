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

questions = {
	"strong": "Do ye like yer drinks strong?",
	"salty": "Do ye like it with a salty tang?",
	"bitter": "Are ye a lubber who likes it bitter?",
	"sweet": "Would ye like a bit of sweetness with yer poison?",
	"fruity": "Are ye one for a fruity finish?"
}

ingredients = {
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	"sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def drinks():
	count = 0			# add to count for each question asked
	drink_desc = []		# append to store desc name for each y ans
	drink_ingr = []		# append to store random ingr for each y ans
	
	while count <= 5:
		print questions["strong"],
		print ("Y or N?")
		strong_ans = raw_input()
		if strong_ans == "Y" or strong_ans == "y":
			print "Aye!"
		elif strong_ans == "N" or strong_ans == "n":
			print "Arrgh!"
		else:
			print "Ye son of a biscuit eater! Be ye tryin' to scuttle me rum makin'?"
		
	



if __name__ == '__main__':
	drinks()
print ""
print ""



