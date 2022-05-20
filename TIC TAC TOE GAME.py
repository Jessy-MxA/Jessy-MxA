'''
STEPS:
1: BOARD SET-UP
2. CREATE GAME PROMPTING - WITH CHECKING SPACE FILLING/EMPTY
3. AFTER 5 TURNS, CHECK FOR 8 POSSIBLE WIN CONDITIONS. IF WIN FOUND - END GAME.
4. IF WINS NOT FOUND, CONTINUE UNTIL WIN FOUND OR WHEN TIE: END GAME.

'''
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = [] #keeps a list of our board key numbers for resetting it later
for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'], '|', board['8'], '|', board['9'])
    print('-', '+', '-', '+', '-')
    print(board['4'], '|', board['5'], '|', board['6'])
    print('-', '+', '-', '+', '-')
    print(board['1'], '|', board['2'], '|', board['3'])

'''GAME'''
def game():
    turn = 'X' #For identifying whose turn it is
    count = 0 #For counting total number of boxes filled on the board

    for i in range(10): #0-8 - for each box from 1-9.
        '''Prompts user to go.'''
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")

        '''Checks if the move is valid. If not valid, prompts to place it somewhere else.
        User must input a block from '''
        move = input() #Should result in move equaling a number from 1-9; for which board box
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to which place?")

        '''After five moves, begin to check all 8 possible win conditions'''
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\n Game Over. \n")
            print("It's a Tie!")
            break

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    #After the game ends, ask the players if they'll like to play again:
    restart = input("Do you want to play again? (y/n) ")
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = ' '
        game()

    else:
        print('Thanks for playing!')


if __name__ == '__main__':
    game()


