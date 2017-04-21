# File: proj2.py
# Author: Tyler Little
# Date: 12/6/15
# Section: 29
# E-mail: tyler10@umbc.edu
# Description: This program simulates the auto-fill function used in
#              image programs like MS Paint to enclose a white space
#              from a text file given.

# Input: text file
# Output: board1 as a 2D list
def printBoard(file1):
    
    board1 = []

    for eachLine in file1:
        board1.append(eachLine.strip())

    for column in board1:
        print(column)

    return board1

# Input: row, column, symbol of fill, whether to display recursion or not, and the board as a 2D list
# Output: board with filled area
def autoFill(row, column, symbol, recursion, board):
    
    if board[row][column] == ' ':
        board[row] = list(board[row])
        board[row][column] = symbol
        board[row] = ''.join(board[row])

        if recursion == 'yes':
            printBoard(board)

        
        if board[row - 1][column] == ' ':
            autoFill(row - 1, column, symbol, recursion, board)

        if board[row][column + 1] == ' ':
            autoFill(row, column + 1, symbol, recursion, board)

        if board[row + 1][column] == ' ':
            autoFill(row + 1, column, symbol, recursion, board)

        if board[row][column - 1] == ' ':
            autoFill(row, column - 1, symbol, recursion, board)

    return board


def main():

    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0

    # Input validation for file
    while counter1 == 0:

        filename = input("Please enter a file for input: ")
        if filename[-4:] == '.txt' or filename[-4:] == '.dat':
            counter1 = 1

        else:
            print("\tThat is not a valid filename -- please enter a filename \n\tthat ends in \".dat\" or \".txt\"")
    
    file1 = open(filename, 'r')
    board = printBoard(file1)
    fill = ' '

    while fill != 'Q':

        # Input validation for coordinates
        while counter2 == 0:

            fill = input("Please enter the coordinates you would like to start filling at in the form \"row,col\", or Q to quit: ")
            if fill != 'Q':
                fill = fill.split(',')

                if int(fill[0]) < 0 or int(fill[0]) > len(board):
                    print("\t", str(fill[0]), "is not a valid row value; please enter a number\n\t between 0 and", len(board) - 1, "inclusive.")
                
                elif int(fill[1]) < 0 or int(fill[1]) > len(board[0]):
                    print("\t", str(fill[0]), "is not a valid column value; please enter a number\n\t between 0 and", len(board[0]) - 1, "inclusive.")

                else:
                    counter2 = 1

                    row = int(fill[0])
                    column = int(fill[1])

                    # Input validation for symbol
                    while counter3 == 0:
        
                        symbol = input("Please enter a symbol to fill with: ")
                        if len(symbol) < 1 or len(symbol) > 1:
                            print("\tThe symbol","\'", symbol, "\'", "is not a single character.")
        
                        else:
                            counter3 = 1
    
                            # Input validation for recursion
                            while counter4 == 0:

                                recursion = input("Would you like to show each step of the recursion?\nEnter \"yes\" or \"no\" : ")
                                if recursion != 'yes' and recursion != 'no':
                                    print("The choice","\'", recursion, "\'", "is not valid.")

                                else:
                                    counter4 = 1
                    
                    fill1 = autoFill(row, column, symbol, recursion, board)            
                    print("\n====================================================\n")
                    printBoard(fill1)

                    # resets every while loop so user is reprompted
                    counter2 = 0
                    counter3 = 0
                    counter4 = 0

            # quits function after entering Q
            else:
                counter2 = 1

    print("Thank you for using the auto-fill program! :3")

main()
