from Board import *

def PawnMove():
    if SelectedPiece == " P " and Player == 1:
        if Location_y == 2:
            if Target_y == 3 or Target_y == 4:
                UpdateBoard(Board, Target_y, Target_x, " P ")
                UpdateBoard(Board, Location_y, Location_x, " . ")
                GetPrintBoard()
                return True
            else:
                print("Invalid Target")

        elif Target_y == Location_y + 1:
            if Target_x == Location_x:
                UpdateBoard(Board, Target_y, Target_x, " P ")
                UpdateBoard(Board, Location_y, Location_x, " . ")
                GetPrintBoard()

            elif Board[Target_y][Target_x] == " p ":
                if Target_x == Location_x + 1 or Target_x == Location_x - 1:
                    UpdateBoard(Board, Target_y, Target_x, " P ")
                    UpdateBoard(Board, Location_y, Location_x, " . ")
                    GetPrintBoard()
                else:
                    print("Invalid Target")
            else:
                print("Invalid Target")

    elif SelectedPiece == " p " and Player == 2:
        if Location_y == 7:
            if Target_y == 6 or Target_y == 5:
                UpdateBoard(Board, Target_y, Target_x, " p ")
                UpdateBoard(Board, Location_y, Location_x, " . ")
                GetPrintBoard()
                return True
            else:
                print("Invalid Target")

        elif Target_y == Location_y - 1:
            if Target_x == Location_x:
                UpdateBoard(Board, Target_y, Target_x, " p ")
                UpdateBoard(Board, Location_y, Location_x, " . ")
                GetPrintBoard()

            elif Board[Target_y][Target_x] == " P ":
                if Target_x == Location_x - 1 or Target_x == Location_x + 1:
                    UpdateBoard(Board, Target_y, Target_x, " p ")
                    UpdateBoard(Board, Location_y, Location_x, " . ")
                    GetPrintBoard()
                else:
                    print("Invalid Target")
            else:
                print("Invalid Target")

    else:
        print("Invalid Piece")
                   
def BishopMove():
    if SelectedPiece == " B " and Player == 1:
        Change_y = Location_y - Target_y
        Change_x = Location_x - Target_x
        if Change_y == Change_x or 0 - Change_y == Change_x or Change_y == 0 - Change_x or 0 - Change_y == 0 - Change_x:
            UpdateBoard(Board, Target_y, Target_x, " B ")
            UpdateBoard(Board, Location_y, Location_x, " . ")
            GetPrintBoard()
        else:
            print("Invalid Target")

    elif SelectedPiece == " b " and Player == 2:
        Change_y = Location_y - Target_y
        Change_x = Location_x - Target_x
        if Change_y == Change_x or 0 - Change_y == Change_x or Change_y == 0 - Change_x or 0 - Change_y == 0 - Change_x:
            UpdateBoard(Board, Target_y, Target_x, " b ")
            UpdateBoard(Board, Location_y, Location_x, " . ")
            GetPrintBoard()
        else:
            print("Invalid Target")
    else:
        print("Invalid Piece")
        
def KnightMove():
    pass
def RookMove():
    pass
def QueenMove():
    pass
def KingMove():
    pass


global Player
Player = 0

while True:
    if Player == 1:
        Player = 2
        print("Player 2")
    else:
        Player = 1
        print("Player 1")

    
        
    Location = input()
    Target = input()

    if len(Location) != 2:
        print("Invalid Piece")


    for i in range(len(Letters)):
        if Location[0] == Letters[i]:
            Location_y = i

    Location_x = int(Location[1])

    if len(Target) != 2:
        print("Invalid Piece")


    for i in range(len(Letters)):
        if Target[0] == Letters[i]:
            Target_y = i

    Target_x = int(Target[1])
        
    SelectedPiece = Board[Location_y][Location_x]
    if SelectedPiece in Pawn:
        PawnMove()
    elif SelectedPiece in Bishop:
        BishopMove()
    elif SelectedPiece in Knight:
        KnightMove()
    elif SelectedPiece in Rook:
        RookMove()
    elif SelectedPiece in Queen:
        QueenMove()
    elif SelectedPiece in King:
        KingMove()
    else:
        print("Invalid Piece")

