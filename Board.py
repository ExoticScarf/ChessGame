import os
import random

"""
   1 2 3 4 5 6 7 8
 A 
 B
 C
 D
 E
 F
 G
 H
"""
Letters = "ABCDEFGH"
Board_Height = 9
Board_Length = 9

def MakeBoard(): ## Do not use more than once
    
    global Board
    Board = []
    for y in range(Board_Height):
        Board.append([])
        for x in range(Board_Length):

            if y == 0 and x == 0:
                Board[y].append("   ")
            elif y == 0 and x != 0:
                Board[y].append(" " + str(x) + " ")
            elif x == 0 and y != 0:
                Board[y].append(" " + Letters[y - 1] + " ")
            else:
                Board[y].append(" . ")
            
            
        


def UpdateBoard(Board, Update_y, Update_x, Update): ## Updates board with new value
    pass                                            ## with Update_y and _x being the coords
    

##  Turns Board into a multiline string
def GetPrintBoard():

    global PrintBoard
    PrintBoard = ""

    for y in range(Board_Height):
        for x in range(Board_Length):
            PrintBoard += Board[y][x]

        if y < Board_Height - 1:
            PrintBoard += "\n"


    os.system("cls")
    print(PrintBoard)

MakeBoard() 
GetPrintBoard()
