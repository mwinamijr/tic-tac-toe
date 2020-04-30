#define the tic tac toe board using python dictionary

theBoard = {'TL':' ', 'TM':' ', 'TR':' ',     #TL = TOP LEFT, TM = TOP MIDDLE , TR = TOP RIGHT
			'ML':' ', 'MM':' ', 'MR':' ',     #ML = MIDDLE LEFT, MM = MIDDLE MIDDLE , MR = MIDDLE RIGHT
			'LL':' ', 'LM':' ', 'LR':' '}     #LL = LOW LEFT, LM = LOW MIDDLE , LR = LOW RIGHT

#print an empty board

def printBoard(board):
	print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
	print('--+--+--')
	print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
	print('--+--+--')
	print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])