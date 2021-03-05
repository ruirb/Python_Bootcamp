#TIC TAC TOE

#Divided tasks
#   1. We need to print a board.
#   2. Take in player input.
#   3. Place their input on the board.
#   4. Check if the game is won,tied, lost, or ongoing.
#   5. Repeat c and d until the game has been won or tied.
#   6. Ask if players want to play again.

def print_board(user_input):
	print(" "+user_input[1]+" | "+user_input[2]+" | "+user_input[3]+" ")
	print("___|___|___")
	print(" "+user_input[4]+" | "+user_input[5]+" | "+user_input[6]+" ")
	print("___|___|___")
	print(" "+user_input[7]+" | "+user_input[8]+" | "+user_input[9]+" ")
	print("   |   |   ")

#user_input = [" " for i in range(10)]
#print_board(user_input)

def define_player():
	#Variable for the while loop
	good = 0
	choice = ["X","O"]
	print(" ")
	print("Let's begin by choosing players")
	print(" ")

	#Keep asking what character player 1 wants
	while not good:
		p1 = input("Player 1, do you want to be X or O? ")
		if p1 not in choice:
			print("I could not understand you")
		else:
			print("Let's start!")
			good = 1
	choice.remove(p1)
	p2 = choice[0]

	return p1, p2

def conclusion(cur_game, p1, p2):
	#Is the game finished?
	finished = False
	winner = "Tie"

	#Check if P1 won
	if cur_game[1] == p1 and cur_game[2] == p1 and cur_game[2] == p1:
		finished = True
		winner = "Player 1"
	elif cur_game[4] == p1 and cur_game[5] == p1 and cur_game[6] == p1:
		finished = True
		winner = "Player 1"
	elif cur_game[7] == p1 and cur_game[8] == p1 and cur_game[9] == p1:
		finished = True
		winner = "Player 1"
	elif cur_game[1] == p1 and cur_game[4] == p1 and cur_game[7] == p1:
		finished = True
		winner = "Player 1"
	elif cur_game[2] == p1 and cur_game[5] == p1 and cur_game[8] == p1:
		finished = True
		winner = "Player 1"
	elif cur_game[3] == p1 and cur_game[6] == p1 and cur_game[9] == p1:
		finished = True
		winner = "Player 1"
	elif cur_game[1] == p1 and cur_game[5] == p1 and cur_game[9] == p1:
		finished = True
		winner = "Player 1"
	elif cur_game[3] == p1 and cur_game[5] == p1 and cur_game[7] == p1:
		finished = True
		winner = "Player 1"
	#Check if P2 won
	elif cur_game[1] == p2 and cur_game[2] == p2 and cur_game[2] == p2:
		finished = True
		winner = "Player 2"
	elif cur_game[4] == p2 and cur_game[5] == p2 and cur_game[6] == p2:
		finished = True
		winner = "Player 2"
	elif cur_game[7] == p2 and cur_game[8] == p2 and cur_game[9] == p2:
		finished = True
		winner = "Player 2"
	elif cur_game[1] == p2 and cur_game[4] == p2 and cur_game[7] == p2:
		finished = True
		winner = "Player 2"
	elif cur_game[2] == p2 and cur_game[5] == p2 and cur_game[8] == p2:
		finished = True
		winner = "Player 2"
	elif cur_game[3] == p2 and cur_game[6] == p2 and cur_game[9] == p2:
		finished = True
		winner = "Player 2"
	elif cur_game[1] == p2 and cur_game[5] == p2 and cur_game[9] == p2:
		finished = True
		winner = "Player 2"
	elif cur_game[3] == p2 and cur_game[5] == p2 and cur_game[7] == p2:
		finished = True
		winner = "Player 2"

	return finished, winner

def start_game(p1,p2):
	finished = False
	game_board = ["D"," "," "," "," "," "," "," "," "," "]
	p1_turn = True
	while not finished:
		#Who's next
		if p1_turn:
		#Player 1 play
			p1_input = input("Player 1, choose a position: ")
			print(" ")
			if p1_input.isdigit():
				p1_input = int(p1_input)
				if p1_input in range(1,10):
					if game_board[p1_input] != " ":
						print("That's not a valid position")
						print(" ")
					else:
						game_board[p1_input] = p1
						p1_turn = False
						print_board(game_board)
				else:
					print("Not a position number")
					continue
			else:
				print("Not a position number")
				continue
		#Player 2 play
		else:
			p2_input = input("Player 2, choose a position: ")
			print(" ")
			if p2_input.isdigit():
				p2_input = int(p2_input)
				if p2_input in range(1,10):
					if game_board[p2_input] != " ":
						print("That's not a valid position")
						print(" ")
					else:
						game_board[p2_input] = p2
						p1_turn = True
						print_board(game_board)
				else:
					print("Not a position number")
					continue
			else:
				print("Not a position number")
				continue
		#Check if finished
		finished, winner = conclusion(game_board, p1, p2)

		#Check if Tie
		if " " not in game_board and winner == "Tie":
			break

	return winner

#Main code
#Print welcome and rules
print(" ")
print("Welcome players to TIC TAC TOE")
print(" ")
print("Rules are simple:")
print("\t"+"Choose a number in the board as displayed below to position your X or O")
print(" ")
ex_board = ["D","1","2","3","4","5","6","7","8","9"]

print_board(ex_board)

#Define players
p1, p2 = define_player()

again = True

while again:
	#Start Game
	winner = start_game(p1,p2)

	#Display Results
	if winner == "Tie":
		print(" ")
		print("There was a tie!")
		print(" ")
	else:
		print(" ")
		print("The winner is {}".format(winner))
		print(" ")

	#Ask if they want to play again
	control = True
	while control:	
		yn = input("Do you want to play again? (Y/N): ")
		if yn not in ["Y","N"]:
			print(" ")
			print("I could not understand you")
			print(" ")
		elif yn == "Y":
			control = False
			print("Here is the board")
			print(" ")
			print_board(ex_board)
		else:
			control = False
			again = False

print(" ")
print("Thanks for playing")
print(" ")










