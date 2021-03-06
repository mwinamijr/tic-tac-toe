#define the tic tac toe board using python dictionary

theBoard = {'TL':' ', 'TM':' ', 'TR':' ',     #TL = TOP LEFT, TM = TOP MIDDLE , TR = TOP RIGHT
			'ML':' ', 'MM':' ', 'MR':' ',     #ML = MIDDLE LEFT, MM = MIDDLE MIDDLE , MR = MIDDLE RIGHT
			'LL':' ', 'LM':' ', 'LR':' '}     #LL = LOW LEFT, LM = LOW MIDDLE , LR = LOW RIGHT

#print an empty board

def printBoard(board):
	print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
	print('-+-+-')
	print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
	print('-+-+-')
	print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])

#input player's letter
def playerLetter():
	letter = ''

	while letter != 'X' and letter != 'O':
		letter = input("Choose between 'X' and 'O': ").upper()
	if letter == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

#place letter on the board
def placeLetter(board, position, letter):
	board[position] = letter

#who choose first choose first
import random 
def chooseFirst():
	choice = random.randint(0, 1)
	if choice == 0:
		return 'Player 1'
	else:
		return 'Player 2'

#space check
def spaceCheck(board, position):
	return board[position] == ' '

