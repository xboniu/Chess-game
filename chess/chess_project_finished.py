# makes the piece the colour you want it to be
def c(piece, colour):
    if colour == 'white':
        return piece.upper()
    else:
        return piece.lower()

def create_piece(piece, position):
    x, y = converter(position)
    if piece == ' ':
        game[x][y] = ' '
        board[x][y] = ' '
    else:
        colour = which_colour(piece)
        board[x][y] = piece
        piece = piece.lower()
        if piece == 'p':
            game[x][y] = Pawn((x, y), colour)
        elif piece == 'k' and colour == 'white':
            game[x][y] = King((x, y), colour, can_white_castle_k, can_white_castle_q)
        elif piece == 'k' and colour == 'black':
            game[x][y] = King((x, y), colour, can_black_castle_k, can_black_castle_q)
        elif piece == 'q':
            game[x][y] = Queen((x, y), colour)
        elif piece == 'r':
            game[x][y] = Rook((x, y), colour)
        elif piece == 'n':
            game[x][y] = Knight((x, y), colour)
        elif piece == 'b':
            game[x][y] = Bishop((x, y), colour)
        else:
            print('There\'s no such piece')


# makes a duplicat of a list in a different place
def copy_list(array):
    final = []
    for line in array:
        t = []
        for element in line:
            t.append(element)
        final.append(t)
    return final

def which_colour(piece):
    if piece == ' ':
        return None
    if piece.isupper():
        return 'white'
    return 'black'
# returns the opposite colour
def o_c(colour):
    if colour == 'white':
        return 'black'
    return 'white'

# converts chess notation to the one used by the board. Return a tupple where the first variable is the row number [0-7] and the second for the column [0-7]
def converter(position):
    x = '87654321'
    y = 'abcdefgh'
    
    a = position[1]
    b = position[0]
    
    return x.find(a), y.find(b)

def is_blank(square):
    if square == ' ':
        return True
    return False

def visual(board):
    print('  +---+---+---+---+---+---+---+---+')
    for i in range(8):
        x = str(8-i)
        print(f'{x} |', end='')
        for element in board[i]:
            print(f' {element} |', end='')
        print('\n  +---+---+---+---+---+---+---+---+')
    print('    a   b   c   d   e   f   g   h  ')

def is_in_check(board, colour):
    x = 10
    y = 10
    o = o_c(colour)
    # x, y as coordinates of the king
    for i in range(8):
        for j in range(8):
            if board[i][j] == c('k', colour):
                x = i
                y = j
    if x==10:
        return False
    # check if a knight is checking the king
    lista = [(x+1, y+2), (x-1, y-2), (x+1, y-2), (x-1, y+2), (x+2, y+1), (x-2, y-2), (x+2, y-1), (x-2, y+1)]
    for pole in lista:
        if pole[0]>=0 and pole[0]<=7 and pole[1]>=0 and pole[1]<=7:
            if board[pole[0]][pole[1]] == c('n', o):
                return True
    
    # check is a rook/queen is checking horizontally/vertically:

    b = y+1
    while b<=7 and (board[x][b]==' ' or board[x][b]==c('r', o) or board[x][b] == c('q', o)):
        if board[x][b] != ' ':
            return True
        b+=1
    
    b = y-1
    while b>=0 and (board[x][b]==' ' or board[x][b]==c('r', o) or board[x][b] == c('q', o)):
        if board[x][b] != ' ':
            return True
        b-=1
    
    b = x+1
    while b<=7 and (board[b][y]==' ' or board[b][y]==c('r', o) or board[b][y] == c('q', o)):
        if board[b][y] != ' ':
            return True
        b+=1
    
    b = x-1
    while b>=0 and (board[b][y]==' ' or board[b][y]==c('r', o) or board[b][y] == c('q', o)):
        if board[b][y] != ' ':
            return True
        b-=1
    
    # check if a pawn isnt checking 
    if colour == 'white' and ((x>0 and y<7 and board[x-1][y+1]=='p') or (x>0 and y>0 and board[x-1][y-1]=='p')):
        return True
    if colour == 'black' and ((x<7 and y<7 and board[x+1][y+1]=='P') or (x<7 and y>0 and board[x+1][y-1]=='P')):
        return True
    
    # check if a bishop or a queen is checking diagonally
    a = x-1
    b = y-1
    while a>=0 and b>=0 and (board[a][b]==' ' or board[a][b]==c('b', o) or board[a][b] == c('q', o)):
        if board[a][b] != ' ':
            return True
        a-=1
        b-=1
    a = x+1
    b = y+1
    while a<=7 and b<=7 and (board[a][b]==' ' or board[a][b]==c('b', o) or board[a][b] == c('q', o)):
        if board[a][b] != ' ':
            return True
        a+=1
        b+=1

    a = x+1
    b = y-1

    while a<=7 and b>=0 and (board[a][b]==' ' or board[a][b]==c('b', o) or board[a][b] == c('q', o)):
        if board[a][b] != ' ':
            return True
        a+=1
        b-=1
    
    a = x-1
    b = y+1
    while a>=0 and b<=7 and (board[a][b]==' ' or board[a][b]==c('b', o) or board[a][b] == c('q', o)):
        if board[a][b] != ' ':
            return True
        a-=1
        b+=1
    # Checks if a king is next to another king
    enemy_k = c('k', o)
    if x>0:
        if y>0 and board[x-1][y-1] == enemy_k:
            return True
        elif y<7 and board[x-1][y+1] == enemy_k:
            return True
        elif board[x-1][y] == enemy_k:
            return True
    if x<7:
        if y>0 and board[x+1][y-1] == enemy_k:
            return True
        elif y<7 and board[x+1][y+1] == enemy_k:
            return True
        elif board[x+1][y] == enemy_k:
            return True
    elif y>0 and board[x][y-1]== enemy_k:
        return True
    elif y<7 and board[x][y+1] == enemy_k:
        return True
    return False



class King:
    def __init__(self, position, colour, can_castle_king, can_castle_queen):
        self.x = position[0]
        self.y = position[1]
        self.position = position
        self.colour = colour
        self.castle_k = can_castle_king
        self.castle_q = can_castle_queen
        self.piece = board[self.x][self.y]

    def can_move(self, x, y):
        if x not in range(8) or y not in range(8):
            return False
        if self.x==x and self.y==y:
            return False
        if which_colour(board[x][y]) == self.colour:
            return False
        new = copy_list(board)
        new[x][y] = c('k', self.colour)
        new[self.x][self.y] = ' '
        if is_in_check(new, self.colour):
            return False
        # if move 2 or more squares vertically return False
        if abs(self.x-x)>1 or abs(self.y-y)>2:
            return False
        # if the move is a castle
        if self.x-x == 0 and abs(self.y-y)==2:
            if self.colour == 'white' and self.x == 7:
                if y-self.y == 2 and self.castle_k:
                    check = copy_list(board)
                    check[7][5] = 'K'
                    if is_blank(board[7][5]) and is_blank(board[7][6]) and not(is_in_check(check, 'white')):
                        return True
                elif y-self.y == -2 and self.castle_q:
                    check = copy_list(board)
                    check[7][3] = 'K'
                    if is_blank(board[7][3]) and is_blank(board[7][2])and is_blank(board[7][1]) and not(is_in_check(check, 'white')):
                        return True
            elif self.colour == 'black' and self.x == 0:
                if y-self.y == 2 and self.castle_k:
                    check = copy_list(board)
                    check[0][5] = 'k'
                    if is_blank(board[0][5]) and is_blank(board[0][6]) and not(is_in_check(check, 'black')):
                        return True
                elif y-self.y == -2 and self.castle_q:
                    check = copy_list(board)
                    check[0][3] = 'k'
                    if is_blank(board[0][3]) and is_blank(board[0][2])and is_blank(board[0][1]) and not(is_in_check(check, 'black')):
                        return True
        
        # normal move
        if abs(self.x-x)<=1 and abs(self.y-y)<=1:
            return True
        return False
    def possible_move(self):
        possible_moves = []
        squares = [
            (self.x+1, self.y+1),
            (self.x, self.y+1),
            (self.x+1, self.y),
            (self.x+1, self.y-1),
            (self.x-1, self.y+1),
            (self.x-1, self.y-1),
            (self.x, self.y-1),
            (self.x-1, self.y),
        ]
        for square in squares:
            x, y = square
            if x in range(8) and y in range(8) and self.can_move(x, y):
                possible_moves.append(square)
        return possible_moves 
    
    def move(self, x, y):
        if self.can_move(x, y):
            board[self.x][self.y] = ' '
            board[x][y] = self.piece
            if self.colour == 'white':
                can_white_castle_k = False
                can_white_castle_q = False
                game[x][y] = King((x, y), self.colour, can_white_castle_k, can_white_castle_q)
            else:
                can_black_castle_k = False
                can_black_castle_q = False
                game[x][y] = King((x, y), self.colour, can_black_castle_k, can_black_castle_q)
            game[self.x][self.y] = ' '
            if abs(self.y-y) == 2:
                if x==7 and y==6:
                    board[7][7] = ' '
                    board[7][5] = c('r', self.colour)
                    game[7][7] = ' '
                    game[7][5] = Rook((7, 5), self.colour)
                elif y==7 and y==2:
                    board[7][0] = ' '
                    board[7][3] = c('r', self.colour)
                    game[7][0] =' '
                    game[7][3] = Rook((7, 3), self.colour)
                elif x==0 and y==6:
                    board[0][7] = ' '
                    board[0][5] = c('r', self.colour)
                    game[0][7] = ' '
                    game[0][5] = Rook((0, 5), self.colour)
                elif y==7 and y==2:
                    board[0][0] = ' '
                    board[0][3] = c('r', self.colour)
                    game[0][0] =' '
                    game[0][3] = Rook((0, 3), self.colour)
            prev = [(self.x, self.y), (x, y)]
            return True
        return False
        
        
    
# work on it

class Rook:
    def __init__(self, position, colour):
        self.x = position[0]
        self.y = position[1]
        self.colour = colour
        self.piece = board[self.x][self.y]

    def possible_move_r(self):
        possible_moves = []
        # Get all the moves when rook moves right
        if self.y<7:
            b = self.y+1
            while b <= 7:
                if self.can_move_r(self.x, b):
                    possible_moves.append((self.x, b))
                    b+=1
                else:
                    break
        if self.y>0:
            b = self.y-1
            while b >=0:
                if self.can_move_r(self.x, b):
                    possible_moves.append((self.x, b))
                    b-=1
                else:
                    break
        if self.x<7:
            a = self.x+1
            while a <= 7:
                if self.can_move_r(a, self.y):
                    possible_moves.append((a, self.y))
                    a+=1
                else:
                    break
        if self.x>0:
            a = self.x-1
            while a >=0:
                if self.can_move_r(a, self.y):
                    possible_moves.append((a, self.y))
                    a-=1
                else:
                    break
        return possible_moves

    def possible_move(self):
        return self.possible_move_r()  

    
    def can_move_r(self, x, y):
        if self.x==x and self.y==y:
            return False
        if which_colour(board[x][y]) == self.colour:
            return False
        new = copy_list(board)
        new[x][y] = c('r', self.colour)
        new[self.x][self.y] = ' '
        if is_in_check(new, self.colour):
            return False
        if self.x-x != 0 and self.y-y != 0:
            return False
        elif self.x - x != 0:
            if self.x>x:
                for i in range(x+1, self.x):
                    if board[i][self.y] != ' ':
                        return False
            else:
                for i in range(self.x+1, x):
                    if board[i][self.y] != ' ':
                        return False
        else:
            if self.y>y:
                for i in range(y+1, self.y):
                    if board[self.x][i] != ' ':
                        return False
            else:
                for i in range(self.y+1, y):
                    if board[self.x][i] != ' ':
                        return False
        return True
    
    def move(self, x, y):
        if self.can_move_r(x, y):
            board[self.x][self.y] = ' '
            board[x][y] = self.piece
            game[self.x][self.y] = ' '
            game[x][y] = Rook((x, y), self.colour)
            if self.x == 0 and self.y == 0:
                can_black_castle_q = False
            elif self.x == 0 and self.y == 7:
                can_black_castle_k = False
            elif self.x == 7 and self.y == 7:
                can_white_castle_k = False
            elif self.x == 7 and self.y == 7:
                can_white_castle_k = False
            prev = [(self.x, self.y), (x, y)]
            return True
        return False

class Knight:
    def __init__(self, position, colour):
        self.x = position[0]
        self.y = position[1]
        self.colour = colour
        self.piece = board[self.x][self.y]
        
    def can_move_n(self, x, y):
        if self.x==x and self.y==y:
            return False
        if which_colour(board[x][y]) == self.colour:
            return False
        new = copy_list(board)
        new[x][y] = c('n', self.colour)
        new[self.x][self.y] = ' '
        if is_in_check(new, self.colour):
            return False
        if (abs(self.x-x) == 2 and abs(self.y-y) == 1) or (abs(self.x-x) == 1 and abs(self.y-y) == 2):
            return True
        return False
    
    def possible_move(self):
        possible_moves = []
        squares = [
            (self.x+1, self.x+2),
            (self.x+1, self.x-2),
            (self.x-1, self.x+2),
            (self.x-1, self.x-2),
            (self.x+2, self.y+1),
            (self.x-2, self.y+1),
            (self.x+2, self.y-1),
            (self.x-2, self.y-1),
        ]
        for square in squares:
            if square[0] in range(8) and square[1] in range(8) and self.can_move_n(square[0], square[1]):
                possible_moves.append(square)
        return possible_moves
    
    def move(self, x, y):
        if self.can_move_n(x, y):
            board[self.x][self.y] = ' '
            board[x][y] = self.piece
            game[self.x][self.y] = ' '
            game[x][y] = Knight((x, y), self.colour)
            return True
        return False
            
            

class Bishop:
    def __init__(self, position, colour):
        self.x = position[0]
        self.y = position[1]
        self.colour = colour
        self.piece = board[self.x][self.y]
    
    def possible_move_b(self):
        possible_moves = []
        a = self.x
        b = self.y
        while a<7 and b<7:
            a+=1
            b+=1
            if self.can_move_b(a, b):
                possible_moves.append((a, b))
            else:
                break
        a = self.x
        b = self.y
        while a<7 and b>0:
            a+=1
            b-=1
            if self.can_move_b(a, b):
                possible_moves.append((a, b))
            else:
                break
        a = self.x
        b = self.y
        while a>0 and b<7:
            a-=1
            b+=1
            if self.can_move_b(a, b):
                possible_moves.append((a, b))
            else:
                break
        a = self.x
        b = self.y
        while a>0 and b>0:
            a-=1
            b-=1
            if self.can_move_b(a, b):
                possible_moves.append((a, b))
            else:
                break
        return possible_moves
    
    def possible_move(self):
        return self.possible_move_b()

    def can_move_b(self, x, y):
        if self.x==x and self.y==y:
            return False
        if which_colour(board[x][y]) == self.colour:
            return False
        new = copy_list(board)
        new[x][y] = c('b', self.colour)
        new[self.x][self.y] = ' '
        if is_in_check(new, self.colour):
            return False
        if abs(self.x-x) != abs(self.y-y):
            return False
        if x-self.x>0:
            first = 1
        else:
            first = -1
        if y-self.y>0:
            second = 1
        else:
            second = -1
        for i in range(1, abs(self.x-x)):
            if board[self.x+first*i][self.y+second*i] != ' ':
                return False
        return True
    
    def move(self, x, y):
        if self.can_move_b(x, y):
            board[self.x][self.y] = ' '
            board[x][y] = self.piece
            game[self.x][self.y] = ' '
            game[x][y] = Bishop((x, y), self.colour)
            return True
        return False
        
        
class Queen(Rook, Bishop):
    def __init__(self, position, colour):
        self.x = position[0]
        self.y = position[1]
        self.colour = colour
        self.piece = board[self.x][self.y]

    def possible_move(self):
        possible_moves = self.possible_move_b()+self.possible_move_r()
        return possible_moves
    
    def can_move_q(self, x, y):
        if self.can_move_r(x, y) or self.can_move_b(x, y):
            return True
        return False
    
    def move(self, x, y):
        if self.can_move_q(x, y):
            board[self.x][self.y] = ' '
            board[x][y] = self.piece
            game[self.x][self.y] = ' '
            game[x][y] = Queen((x, y), self.colour)
            return True
        return False
   

# Finished (I think)
class Pawn:
    def __init__(self, position, colour):
        self.x = position[0]
        self.y = position[1]
        self.colour = colour
        self.piece = board[self.x][self.y]
    
    def possible_move(self):
        possible_moves = []
        if self.colour == 'white':
            k = -1
        else:
            k = 1
        if self.can_move_p(self.x+k*1, self.y):
            possible_moves.append((self.x+k*1, self.y))
        if self.can_move_p(self.x+k*2, self.y):
            possible_moves.append((self.x+k*2, self.y))
        if self.y>0 and self.can_move_p(self.x+k*1, self.y-1):
            possible_moves.append((self.x+k*1, self.y-1))
        if self.y<7 and self.can_move_p(self.x+k*1, self.y+1):
            possible_moves.append((self.x+k*1, self.y+1))
        return possible_moves
        
        


    def move_1_up(self):
        if self.colour == 'white' and board[self.x-1][self.y] == ' ':
            return True
        elif self.colour == 'black' and board[self.x+1][self.y] == ' ':
            return True
        return False
    
    def move_2_up(self):
        if all([self.colour == 'white', self.x == 6, board[5][self.y] == ' ', board[4][self.y]==' ']):
            return True
        elif self.colour == 'black' and self.x == 1 and board[self.x+1][self.y] == ' ' and board[self.x+2][self.y]==' ':
            return True
        return False
    # with en passant
    def take_left(self):
        if self.colour == 'white':
            if self.y>0 and board[self.x-1][self.y-1]!=' ' and board[self.x-1][self.y-1].islower():
                return True
            elif self.y>0 and board[self.x][self.y-1]=='p' and prev == [(self.x+2, self.y-1), (self.x, self.y-1)]:
                return True
        elif self.colour == 'black':
            if self.y>0 and board[self.x+1][self.y-1]!=' ' and board[self.x+1][self.y-1].isupper():
                return True
            elif self.y>0 and board[self.x][self.y-1]=='P' and prev == [(self.x-2, self.y-1), (self.x, self.y-1)]:
                return True
        return False
    # with en passant
    def take_right(self):
        if self.colour == 'white':
            if self.y<7 and board[self.x-1][self.y+1]!=' ' and board[self.x-1][self.y+1].islower():
                return True
            elif self.y>0 and board[self.x][self.y+1]=='p' and prev == [(self.x+2, self.y+1), (self.x, self.y+1)]:
                return True
        elif self.colour == 'black':
            if self.y<7 and board[self.x+1][self.y+1]!=' ' and board[self.x+1][self.y+1].isupper():
                return True
            elif self.y>0 and board[self.x][self.y+1]=='P' and prev == [(self.x-2, self.y+1), (self.x, self.y+1)]:
                return True
        return False
    # Main move function
    def can_move_p(self, x, y):
        if self.x==x and self.y==y:
            return False
        if which_colour(board[x][y]) == self.colour:
            return False
        new = copy_list(board)
        new[x][y] = c('p', self.colour)
        new[self.x][self.y] = ' '
        if is_in_check(new, self.colour):
            return False
        if self.colour == 'white':
            if x-self.x==-1:
                if y == self.y:
                    return self.move_1_up()
                elif y-self.y==-1:
                    return self.take_left()
                elif y-self.y==1:
                    return self.take_right()
            elif x-self.x==-2 and y==self.y:
                return self.move_2_up()
        elif self.colour == 'black':
            if x-self.x==1:
                if y == self.y:
                    return self.move_1_up()
                elif y-self.y==-1:
                    return self.take_left()
                elif y-self.y==1:
                    return self.take_right()
            elif x-self.x==2 and y==self.y:
                return self.move_2_up()
    
    def move(self, x, y):
        if self.can_move_p(x, y):
            board[self.x][self.y] = ' '
            game[self.x][self.y] = ' '
            if x==0 or x==7:
                p = input('What piece do tou want to promote to?\n')
                if p == c('q', self.colour):
                    game[x][y] = Queen((x, y), self.colour)
                elif p == c('r', self.colour):
                    game[x][y] = Rook((x, y), self.colour)
                elif p == c('n', self.colour):
                    game[x][y] = Knight((x, y), self.colour)
                elif p == c('b', self.colour):
                    game[x][y] = Bishop((x, y), self.colour)
                else:
                    print('Enter a possible piece')
                    self.move(x, y)
                board[x][y] = p
            else:
                board[x][y] = self.piece
                game[x][y] = Pawn((x, y), self.colour)
                
            return True
        return False

# initiating the game variables
whose_move = 'white'
occupied_by_white = []
occupied_by_black = []
can_white_castle_q = True
can_white_castle_k = True
can_black_castle_q = True
can_black_castle_k = True
prev = []
game = []
start = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
board = start
for i in range(8):
    t = []
    for j in range(8):
        square = board[i][j]
        if square == ' ':
            t.append(' ')
            continue
        if square.isupper():
            color = 'white'
            occupied_by_white.append((i, j))
        else:
            color = 'black'
            occupied_by_black.append((i, j))
        if square.lower() == 'k':
            t.append(King((i, j), color, True, True))
        elif square.lower() == 'q':
            t.append(Queen((i, j), color))
        elif square.lower() == 'r':
            t.append(Rook((i, j), color))
        elif square.lower() == 'b':
            t.append(Bishop((i, j), color))
        elif square.lower() == 'n':
            t.append(Knight((i, j), color))
        elif square.lower() == 'p':
            t.append(Pawn((i, j), color))
    game.append(t)


# check if in an opposite colour than the move is mated
def is_mate():
    if not(is_in_check(board, o_c(whose_move))):
        return False
    for i in range(8):
        for j in range(8):
            if board[i][j] == ' ':
                continue
            elif which_colour(board[i][j]) == o_c(whose_move):
                if game[i][j].possible_move():
                    print(i, j)
                    print(game[i][j].possible_move())
                    return False
    return True
# check if stalemate
def stalemate():
    if is_in_check(board, o_c(whose_move)):
        return False
    for i in range(8):
        for j in range(8):
            if board[i][j] == ' ':
                continue
            elif which_colour(board[i][j]) == o_c(whose_move):
                print(game[i][j])
                if game[i][j].possible_move():
                    return False
    return True

# check if insufficient material
def draw():
    pieces_white = []
    pieces_black = []
    w_b = 0
    w_n = 0
    b_b = 0
    b_n = 0
    occupied_by_black = []
    occupied_by_white = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == ' ':
                continue
            elif which_colour(board[i][j]) == 'white':
                occupied_by_white.append((i, j))
            else:
                occupied_by_black.append((i, j))
    for square in occupied_by_black:
        x = square[0]
        y = square[1]
        if board[x][y] == 'b':
            b_b+=1
        elif board[x][y] == 'n':
            b_n +=1
        pieces_black.append(board[x][y])
    for square in occupied_by_white:
        x = square[0]
        y = square[1]
        if board[x][y] == 'B':
            w_b+=1
        elif board[x][y] == 'N':
            w_n+=1
        pieces_white.append(board[x][y])
    if 'p' in pieces_black or 'P' in pieces_white:
        return False
    elif 'q' in pieces_black or 'Q' in pieces_white:
        return False
    elif 'r' in pieces_black or 'R' in pieces_white:
        return False
    elif ('b' in pieces_black and 'n' in pieces_black) or ('B' in pieces_white and 'N' in pieces_white):
        return False
    elif (w_b>0 and w_n>0) or (b_b>0 and b_n>0):
        return False
    elif w_b>1 or b_b>1:
        return False
    elif w_b+w_n<2 and w_b+w_n<2:
        return True
    return True
    # later solve the issue with just 2 knights left
    

# main
# whose_move is the colour of the player whose move it is. At the beginning it's white
# game = the interactive board with pieces
# board = the board that is printed
end = False
while end != True:
    print('------------------------')
    visual(board)
    print(f'Player {whose_move} to move\n')
    action = (input('From which square do you want to move?\n'), input('To which square do you want to move\n'))
    try:
        prev = [converter(action[0]), converter(action[1])]
    except:
        print('Enter existing squares.')
        continue
    where_from = prev[0]
    where_to = prev[1]
    piece = board[where_from[0]][where_from[1]]
    if piece == ' ':
        print('There\'s no piece on the square you entered.')
        continue
    if whose_move !=which_colour(piece):
        print('The piece you\'re trying to move isn\'t yours')
        continue
    if where_from == where_to:
        print('You can\'t not move')
        continue
    if which_colour(board[where_from[0]][where_from[1]]) == which_colour(board[where_to[0]][where_to[1]]):
        print('You can\'t move a piece to a square occupied by your other piece')
        continue

    # Now doing the move after which the board and the game get updated
    action = game[where_from[0]][where_from[1]].move(where_to[0], where_to[1])
    if action:
        if whose_move == 'white':
            occupied_by_white.remove((where_from[0], where_from[1]))
            occupied_by_white.append((where_to[0], where_to[1]))
            if (where_to[0], where_to[1]) in occupied_by_black:
                occupied_by_black.remove((where_to[0], where_to[1]))
        else:
            occupied_by_black.remove((where_from[0], where_from[1]))
            occupied_by_black.append((where_to[0], where_to[1]))
            if (where_to[0], where_to[1]) in occupied_by_white:
                occupied_by_white.remove((where_to[0], where_to[1]))
    if action == False:
        print('Please enter a legal move')
        continue
    if draw():
        visual(board)
        print('------------------------')
        print('The game ended in a draw')
        print('------------------------')
        end = True
    if stalemate():
        visual(board)
        print('-----------------------------')
        print('The game ended in a stalemate')
        print('-----------------------------')
        end = True
    if is_mate():
        winner = whose_move
        visual(board)
        print('------------------- -')
        print(f'The winner is {winner}!!!')
        print('------------------- -')
        end = True
    whose_move = o_c(whose_move)
'''

# checking smth

board = []
for i in range(8):
    t = []
    for j in range(8):
        t.append(' ')
    board.append(t)
game = copy_list(board)
can_black_castle_k = False
can_black_castle_q = False
can_white_castle_k = False
can_white_castle_q = False
create_piece('K', 'c3')
#create_piece('R', 'b2')
create_piece('k', 'a1')
create_piece('B', 'd8')
#create_piece('R', 'a2')
print(draw())
'''
# smth wrong with the possible_move function for the king

# rewrite possible_move for the Rook and the Bishop

# smth wrong with is_mate(), maybe because of the above