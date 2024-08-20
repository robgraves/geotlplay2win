#!/usr/bin/env python3

#######################################################
#
# Matthew Page
# 08/19/2024
#
# pay2win.py	- An attempt at simplifying Ken's life
#				for GEOTL Pay to Win results, in both
#				a random and fair way distributed by
# 				way of Ken's criteria for games are
# 				awarded.
#
#######################################################



##########################
#
# Importing yo
#
##########################

import random

#DO I NEED TO SAVE TO A FILE? MAYBE



##########################
#
# Function definitions
#
##########################

def gamemenu():
	#gamemenu function.

	#the game menu is just for entering
	#and editing pay to win game names.
	pass

def playermenu():
	#playermenu function.

	#the player menu is just for entering
	#and editing pay to win player names.
	pass

def gamelist():
	#gamelist function.

	#the game list merely shows the current
	#list of just game names.
	pass

def playerlist():
	#playerlist function.

	#the player list merely shows the current
	#list of just player names.
	pass

def playerassign():
	#playerassign function.

	#the player assign function is for
	#assigning player names in player list
	#to the games that they played.
	pass

def completelist():
	#completelist function.

	#the complete list should show each individual
	#pay to win game and every player who played
	#each of these games.
	pass

def gamewincalc():
	#gamewincalc function.

	#this is the whole point of the program which
	#now will be able to take all of the accumulated
	#pay to win game and player data all entered and
	#assigned correctly to each game and now choose
	#winners of each game randomly by way of weighting
	#players based off of how many games they are in
	#the running for as Ken's priority is ideally for
	#everyone to win one game.

	#My game plan for this process is to find all
	#players that have the least instances of their
	#name occurring on the play to win should be weighted
	#in their favor for the game(s) their names occur on.
	#Also once a player has won a game, they are done,
	#their name is now removed from the player database 
	#completely and from any other instances of their name
	#occuring on any other game, leaving only non-winners
	#available to win those games.

	#Hypothetical smaller scale scenario:
	# Catan: 	 Carcassonne: Ticket to Ride:
	# Nate (1)	 Ken    (6)   Matt   (6)
	# Matt (6)	 Matt   (6)	  Ken    (6)
	# Ken  (6)	 Mark   (6)   Andrew (5)
	# Mark (6)	 Andrew	(5)   Mark   (6)
	#
	# Dominion:  Twilight Imperium: Azul:
	# Matt   (6) Matt   (6)         Jen         (1)  
	# Ken    (6) Ken    (6)			Abi 	    (1)
	# Mark   (6) Andrew (5)			Don Hauri   (1)
	# Andrew (5) Mark   (6)			Cindy Hauri (1)
	#
	# King of Tokyo:
	# Matt   (6)
	# Ken	 (6)
	# Andrew (5)
	# Mark   (6)
	#
	#In the above scenario, Nate only exists once on the 
	#entire list for playing the Catan game(the parentheses
	#number signifies how many instances of a players name 
	#exist across the complete list.)  So according to Ken,
	#in the case of Catan, Nate should win it as otherwise
	#Nate wouldn't win anything and the other players in Catan
	#exist in so many other games and have so many other 
	#opportunities to win games.  In the case of Azul, all of
	#the players only played Azul.  In this part of the scenario
	#someone has to win Azul, each player only played this, this
	#is just a case of random pick between these 4 players.  Had 
	#one of them played more, you would strip the person who had
	#played more from the running for that game, say Jen has played
	#2 games, then the running for it would be between Abi, Don, and 
	#Cindy.  But then after the Azul game was awarded and closed,
	#remaining members of a closed game would have their instance
	#count dropped by one (decremented) for Example now if Jen was at 2,
	#now she would become a 1 and would be in the weighted pick for 
	#whatever game she remained in. In the cases of the 5 games that
	#the 4 multi-game players played, choose randomly for each and 
	#once each has won one and their name stripped from the remaining
	#game, that last game would be leftover and either become a demo 
	#game for the store or be carried over to next year's play to win
	#
	#Another consideration is that carryover game if its a highly
	#desired game then that could be problematic.
	#A possible option could be weighting the games by number of players
	#per game.  So assigning a faux "desirability" rating for a game
	#based upon its quantity of players total.  This would dictate
	#the order of the games awarded within this program.  The most 
	#"desirable" games would be selected first.  Also allowing for 
	#a staff discretion for swapping in the event of my less desirable
	#game being awarded before a carryover more desirable game would
	#allow the human element to fix the bias of a "desirability" rating.
	#
  

	pass


##########################
#
# MAIN MENU
#
##########################

main_choice = "0"
while main_choice != "Q" or main_choice != "q":
	print("**********************************       ")
	print("*****Great Escape On The Lake*****       ")
	print("***********Play to Win************       ")
	print("*********Help Ken Program*********       ")
	print("**********************************       ")
	print("                                         ")
	print("    1 - Enter/Edit game data             ")
	print("    2 - Enter/Edit a player name         ")
	print("    3 - Show game list   		        ") 
	print("    4 - Show player list			        ")
	print("    5 - Assign players to games			")
	print("    6 - Show games with assigned players ")
	print("    7 - Run game winners output          ")
	print("    Q - Quit                             ")
	print("                                         ")
	print("Please choose one of the above and       ")
	print("press ENTER.						        ")
	print("                                         ")
	 
	main_choice = input()
	print("You chose ", main_choice)

	if main_choice == "1":
		#game entry/edit menu
		print("Game Entry/Edit Menu                     ")
		gamemenu()
		input()
	elif main_choice == "2":
		#player enter/edit menu
		print("Player Entry/Edit Menu                   ")
		playermenu()
		input()
	elif main_choice == "3":
		#show game list
		print("Show game list                           ")
		gamelist()
		input()
	elif main_choice == "4":
		#show player list
		print("Show player list                         ") 
		playerlist()
		input()
	elif main_choice == "5":
		#add players to games
		print("Add players to games                     ") 
		playerassign()
		input()
	elif main_choice == "6":
		#show complete list with assigned players
		print("Show complete list with assigned players ") 
		completelist()
		input()
	elif main_choice == "7":
		#run actual game winners output
		print("Running Game Winners Calculation         ")
		print("    4 - Show player list			        ")
		gamewincalc()
		input()
	elif main_choice == "Q" or main_choice == "q":
		break



