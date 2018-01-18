import os

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
Letters = "_ABCDEFGH"
Board_Height = 9
Board_Length = 9

## Item 0 is identifier
Pawn = ["Pawn", " P ", " p "]
Bishop = ["Bishop", " B ", " b "]
Knight = ["Knight", " N ", " n "]
Rook = ["Rook", " R ", " r "]
Queen = ["Queen", " Q ", " q "]
King = ["King", " K ", " k "]
Pieces = [Pawn, Bishop, Knight, Rook, Queen, King]

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
                Board[y].append(" " + Letters[y] + " ")
            else:
                Board[y].append(" . ")
    y = 1
    Side = 0
    while True:
        Side += 1

        if Side == 3:
            break

        for x in range(Board_Length):
            if x == 1:
                UpdateBoard(Board, y, x, Pieces[3][Side])
            if x == 2:
                UpdateBoard(Board, y, x, Pieces[2][Side])
            if x == 3:
                UpdateBoard(Board, y, x, Pieces[1][Side])
            if x == 4:
                UpdateBoard(Board, y, x, Pieces[4][Side])
            if x == 5:
                UpdateBoard(Board, y, x, Pieces[5][Side])
            if x == 6:
                UpdateBoard(Board, y, x, Pieces[1][Side])
            if x == 7:
                UpdateBoard(Board, y, x, Pieces[2][Side])
            if x == 8:
                UpdateBoard(Board, y, x, Pieces[3][Side])

        if y == 1:
            y += 1
        else:
            y -= 1

        for x in range(Board_Length - 1):
            UpdateBoard(Board, y, x + 1, Pieces[0][Side])

        y = 8


def UpdateBoard(Board, Update_y, Update_x, Update):
    Board[Update_y][Update_x] = Update

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
