#!/usr/bin/python

import json

filename = "users_settings.txt"
# Create file for write
myfile = open(filename, "w")

# Player 1 info
player1 = {
	'PlayerName' : "Gevorg",
	'Score' : 345,
	'avards' : ["OR", "NV", "NY"]
}

# Player 2 info
player2 = {
	'PlayerName' : "Tigran",
	'Score' : 346,
	'avards' : ["WI", "TX", "MI"]
}

# Create list
myplayers = []
# Add in list both players info
myplayers.append(player1)
myplayers.append(player2)

# Add list data in json file
json.dump(myplayers, myfile)
myfile.close()

# Open file for read
myfile = open(filename, 'r')
# Load json file data in variables
json_data = json.load(myfile)

# Show players information
for user in json_data:
	print("Player name is: " + str(user['PlayerName']))
	print("Player score is: " + str(user['Score']))
	print("Player avards N1: " + str(user['avards'][0]))
	print("Player avards N2: " + str(user['avards'][1]))
	print("Player avards N3: " + str(user['avards'][2]))
	print("--------------------------------------\n\n")
