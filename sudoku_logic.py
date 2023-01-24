Color=["Red","Blue"]

class Piece:
    def __init__(self, value):
        self.value = value
        self.color = None 
        self.row = -1
        self.col = -1
    def set_position(self, row, col):
        self.row = row
        self.col = col
    def distribute(self,color):
        self.color = color

    def __repr__(self):
        return "value: %d, color: %s, position: (%d, %d)" % (self.value, self.color, self.row, self.col)

class Chess:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = 0
        self.candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.color = None 
        self.accept_for_piece= True  
    def check(self, piece):
        if piece.value in self.candidates:
            self.accept_for_piece=True 
            return True
        else:
            self.accept_for_piece=False
            return False
    def put(self, piece):
        if self.check(piece):
            self.value = piece.value
            self.color = piece.color
            piece.set_position(self.row, self.col)
            self.candidates = {}
    def remove(self, piece):
        if piece.value in self.candidates:
            self.candidates.remove(piece.value)

class Line:
    def __init__(self, ID, chesses):
        self.ID = ID
        self.chesses = []
        for chess in chesses:
            self.chesses.append(chess)
    def update(self, piece):
        for chess in self.chesses:
            chess.remove(piece)

class Block:
    Color=["Red","Blue"]
    def __init__(self, row,col,chesses):
        self.row = row
        self.col = col
        self.chesses = []
        for chess in chesses:
            self.chesses.append(chess)
        self.count = {Color[0]:0,Color[1]:0}
    def update(self, piece):
        for chess in self.chesses:
            chess.remove(piece)
        # set Block color 
        # if color1 piece > color2 piece, set color1
        # if color1 piece < color2 piece, set color2
        # if color1 piece == color2 piece, set None
        self.count[piece.color] += 1
        if self.count[Color[0]] > self.count[Color[1]]:
            self.color = Color[0]
        elif self.count[Color[0]] < self.count[Color[1]]:
            self.color = Color[1]
        else:
            self.color = None

class Board:
    def __init__(self):
        self.chesses = [Chess(i//9,i%9) for i in range(81)]
        self.rows = [Line(row, self.chesses[row*9:row*9+9]) for row in range(9)]
        self.cols = [Line(col, self.chesses[col:col+81:9]) for col in range(9)]
        self.block = [[Block(i,j,[self.chesses[i*27+j*3+k*9+l] for k in range(3) for l in range(3)]) for j in range(3)] for i in range(3)]
    def put(self, piece, row, col):
        for chess in self.chesses:
            if chess.row == row and chess.col == col:
                chess.put(piece)    
        self.chesses[row*9+col].put(piece)
        self.rows[row].update(piece)
        self.cols[col].update(piece)
        self.block[row//3][col//3].update(piece)
    def hover(self, piece):
        for chess in self.chesses:
            chess.accept_for_piece(piece)