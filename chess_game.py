class Board:
    def __init__(self):
        self.columns = "abcdefgh"
        self.squares = {}
        self.taken_pieces = []
        self.en_passant_target = None
        for letter in 'abcdefgh':
            for number in range(1, 9):
                self.squares[letter + str(number)] = None

class Piece:
    def __init__(self, color, position, board):
        self.color = color
        self.position = position
        self.board = board
        self.has_moved = False
        if color == 'white':
            self.direction = 1
        else:
            self.direction = -1

    def Move(self, new_position):
        piece = self.board.squares[new_position]
        if piece is None:
            self.board.squares[self.position] = None
            self.board.squares[new_position] = self
            self.position = new_position
            self.has_moved = True
            return True
        elif piece.color != self.color:
            piece.captured = True
            self.board.squares[self.position] = None
            self.board.squares[new_position] = self
            self.board.taken_pieces.append(piece)
            self.position = new_position
            self.has_moved = True
            return True
        elif piece.color == self.color:
            print("Invalid move: cannot capture your own piece.")
            return False
        else:
            pass



class King(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position, board)
    def __str__(self):
        return "♚" if self.color == "white" else "♔"
    def can_castle(self):
        return not self.has_moved
    def possible_moves(self):
        moves = []
        column = self.position[0]
        row = int(self.position[1])
        column_index = self.board.columns.index(column)

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]

        for column_change, row_change in directions:
            new_column_index = column_index + column_change
            new_row = row + row_change

            if 0 <= new_column_index < 8 and 1 <= new_row <= 8:
                new_position = self.board.columns[new_column_index] + str(new_row)

                piece = self.board.squares[new_position]

                if piece is None or piece.color != self.color:
                    moves.append(new_position)
        if self.can_castle():
            if self.color == 'white':
                if self.board.squares['h1'] is not None and isinstance(self.board.squares['h1'], Rook) and self.board.squares['h1'].can_castle():
                    if self.board.squares['f1'] is None and self.board.squares['g1'] is None:
                        moves.append('g1')
                if self.board.squares['a1'] is not None and isinstance(self.board.squares['a1'], Rook) and self.board.squares['a1'].can_castle():
                    if self.board.squares['b1'] is None and self.board.squares['c1'] is None and self.board.squares['d1'] is None:
                        moves.append('c1')
            else:
                if self.board.squares['h8'] is not None and isinstance(self.board.squares['h8'], Rook) and self.board.squares['h8'].can_castle():
                    if self.board.squares['f8'] is None and self.board.squares['g8'] is None:
                        moves.append('g8')
                if self.board.squares['a8'] is not None and isinstance(self.board.squares['a8'], Rook) and self.board.squares['a8'].can_castle():
                    if self.board.squares['b8'] is None and self.board.squares['c8'] is None and self.board.squares['d8'] is None:
                        moves.append('c8')
        return moves

class Bishop(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position, board)

    def __str__(self):
        return "♝" if self.color == "white" else "♗"
    def possible_moves(self):
        moves = []

        column = self.position[0]
        row = int(self.position[1])
        column_index = self.board.columns.index(column)

        directions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]
        for column_change, row_change in directions:
            new_column_index = column_index + column_change
            new_row = row + row_change

            while 0 <= new_column_index < 8 and 1 <= new_row <= 8:
                new_position = self.board.columns[new_column_index] + str(new_row)
                piece = self.board.squares[new_position]

                if piece is None:
                    moves.append(new_position)
                elif piece.color != self.color:
                    moves.append(new_position)
                    break
                else:
                    break
                new_column_index += column_change
                new_row += row_change
        return moves

class Rook(Piece): 
    def __init__(self, color, position, board):
        super().__init__(color, position, board)
    def can_castle(self):
        return not self.has_moved
    def __str__(self):
        return "♜" if self.color == "white" else "♖"

    def possible_moves(self):
        moves = []
        column = self.position[0]
        row = int(self.position[1])
        column_index = self.board.columns.index(column)

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        for column_change, row_change in directions:
            new_column_index = column_index + column_change
            new_row = row + row_change

            while 0 <= new_column_index < 8 and 1 <= new_row <= 8:
                new_position = self.board.columns[new_column_index] + str(new_row)
                piece = self.board.squares[new_position]

                if piece is None:
                    moves.append(new_position)
                elif piece.color != self.color:
                    moves.append(new_position)
                    break
                else:
                    break
                new_column_index += column_change
                new_row += row_change
        return moves

class Queen(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position, board)

    def __str__(self):
        return "♛" if self.color == "white" else "♕"
    def possible_moves(self):
        moves = []
        column = self.position[0]
        row = int(self.position[1])
        column_index = self.board.columns.index(column)

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1)
        ]

        for column_change, row_change in directions:
            new_column_index = column_index + column_change
            new_row = row + row_change

            while 0 <= new_column_index < 8 and 1 <= new_row <= 8:
                new_position = self.board.columns[new_column_index] + str(new_row)
                piece = self.board.squares[new_position]

                if piece is None:
                    moves.append(new_position)
                elif piece.color != self.color:
                    moves.append(new_position)
                    break
                else:
                    break
                new_column_index += column_change
                new_row += row_change
        return moves

class Knight(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position, board)

    def __str__(self):
        return "♞" if self.color == "white" else "♘"
    def possible_moves(self):
        moves = []
        column = self.position[0]
        row = int(self.position[1])
        column_index = self.board.columns.index(column)

        knight_moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1)
        ]
        for column_change, row_change in knight_moves:
            new_column_index = column_index + column_change
            new_row = row + row_change

            if 0 <= new_column_index < 8 and 1 <= new_row <= 8:
                new_position = self.board.columns[new_column_index] + str(new_row)
                piece = self.board.squares[new_position]

                if piece is None or piece.color != self.color:
                    moves.append(new_position)
        return moves

class Pawn(Piece):
    def __init__(self, color, position, board):
        super().__init__(color, position, board)
        self.first_move = True

    def __str__(self):
        return "♟" if self.color == "white" else "♙"
    def possible_moves(self):
        moves = []
        column = self.position[0]
        row = int(self.position[1])
        column_index = self.board.columns.index(column)
        self.first_move = True if (self.color == 'white' and row == 2) or (self.color == 'black' and row == 7) else False
        pawn_moves = [
            (0, self.direction)
        ]
        # two forward, only on first move AND if the square ahead is empty
        one_ahead = self.board.columns[column_index] + str(row + self.direction)
        if self.first_move and self.board.squares[one_ahead] is None:
            pawn_moves.append((0, 2 * self.direction))

        # diagonals (direction already handles color)
        pawn_moves.append((-1, self.direction))
        pawn_moves.append((1, self.direction))

        for column_change, row_change in pawn_moves:
            new_column_index = column_index + column_change
            new_row = row + row_change

            if 0 <= new_column_index < 8 and 1 <= new_row <= 8:
                new_position = self.board.columns[new_column_index] + str(new_row)
                piece = self.board.squares[new_position]

                if column_change == 0:          # forward move
                    if piece is None:
                        moves.append(new_position)
                else:                           # diagonal capture
                    if (piece is not None and piece.color != self.color) or (self.board.en_passant_target == new_position):
                        moves.append(new_position)
        return moves
    def promote(self, new_piece_type):
        if new_piece_type == 'queen':
            self.board.squares[self.position] = Queen(self.color, self.position, self.board)
        elif new_piece_type == 'rook':
            self.board.squares[self.position] = Rook(self.color, self.position, self.board)
        elif new_piece_type == 'bishop':
            self.board.squares[self.position] = Bishop(self.color, self.position, self.board)
        elif new_piece_type == 'knight':
            self.board.squares[self.position] = Knight(self.color, self.position, self.board)
        else:
            print("Invalid promotion piece type. Choose from 'queen', 'rook', 'bishop', or 'knight'.")
class Game:
    def __init__(self):
        self.board = Board()
        self.turn = 'white'
        self.taken_pieces = []
        self.setup_pieces()

    def play(self):
        while True:
            self.take_turn()

    def is_attacked(self, square, color):
        for position, piece in self.board.squares.items():
            if piece is None:
                continue
            if piece.color != color:
                continue
            if isinstance(piece, Pawn):
                # a pawn attacks only its two diagonals, regardless of what's there
                column_index = self.board.columns.index(position[0])
                row = int(position[1])
                for column_change in (-1, 1):
                    new_column_index = column_index + column_change
                    new_row = row + piece.direction
                    if 0 <= new_column_index < 8 and 1 <= new_row <= 8:
                        attacked = self.board.columns[new_column_index] + str(new_row)
                        if attacked == square:
                            return True
            else:
                if square in piece.possible_moves():
                    return True
        return False

    def is_in_check(self, color):
        for position, piece in self.board.squares.items():
            if isinstance(piece, King) and piece.color == color:
                king_square = position
                break

        enemy_color = 'black' if color == 'white' else 'white'
        return self.is_attacked(king_square, enemy_color)

    def legal_moves(self, piece):
        legal = []

        for destination in piece.possible_moves():
            if self.move_is_safe(piece, destination):
                legal.append(destination)

        return legal


    def move_is_safe(self, piece, destination):

        start = piece.position
        piece_on_destination = self.board.squares[destination]

        self.board.squares[start] = None
        self.board.squares[destination] = piece
        piece.position = destination

        king_safe = not self.is_in_check(piece.color)

        self.board.squares[start] = piece
        self.board.squares[destination] = piece_on_destination
        piece.position = start

        return king_safe

    def display_board(self, turn):
        if turn == 'white':
            rows = range(8, 0, -1)
            cols = self.board.columns
        else:
            rows = range(1, 9)
            cols = self.board.columns[::-1]
        for row in rows:
            line = str(row) + " "
            for col in cols:
                piece = self.board.squares[col + str(row)]
                line = line + (str(piece) if piece else ".") + " "
            print(line)
        print("  " + " ".join(cols))



    def setup_pieces(self):
        self.board.squares["a1"] = Rook("white", "a1", board=self.board)
        self.board.squares["b1"] = Knight("white", "b1", board=self.board)
        self.board.squares["c1"] = Bishop("white", "c1", board=self.board)
        self.board.squares["d1"] = Queen("white", "d1", board=self.board)
        self.board.squares["e1"] = King("white", "e1", board=self.board)
        self.board.squares["f1"] = Bishop("white", "f1", board=self.board)
        self.board.squares["g1"] = Knight("white", "g1", board=self.board)
        self.board.squares["h1"] = Rook("white", "h1", board=self.board)

        for column in self.board.columns:
            position = column + "2"
            self.board.squares[position] = Pawn("white", position, board=self.board)

        self.board.squares["a8"] = Rook("black", "a8", board=self.board)
        self.board.squares["b8"] = Knight("black", "b8", board=self.board)
        self.board.squares["c8"] = Bishop("black", "c8", board=self.board)
        self.board.squares["d8"] = Queen("black", "d8", board=self.board)
        self.board.squares["e8"] = King("black", "e8", board=self.board)
        self.board.squares["f8"] = Bishop("black", "f8", board=self.board)
        self.board.squares["g8"] = Knight("black", "g8", board=self.board)
        self.board.squares["h8"] = Rook("black", "h8", board=self.board)

        for column in self.board.columns:
            position = column + "7"
            self.board.squares[position] = Pawn("black", position, board=self.board)
    def change_turn(self):
        if self.turn == 'white':
            self.turn = 'black'
        else:
            self.turn = 'white'    
    def take_turn(self):
        self.display_board(self.turn)

        result = self.check_game_over(self.turn)
        if result == 'checkmate':
            winner = 'black' if self.turn == 'white' else 'white'
            print(f"Checkmate! {winner} wins.")
            return 'over'
        if result == 'stalemate':
            print("Stalemate! It's a draw.")
            return 'over'

        if self.is_in_check(self.turn):
            print(f"{self.turn} is in check!")
        print(f"{self.turn}'s turn")

        while True:
            old_position = input("Enter the position of the piece you want to move (e.g., 'e2'): ")
            if old_position not in self.board.squares:
                print("Invalid position.")
                continue
            piece = self.board.squares[old_position]
            if piece is None:
                print("No piece at that position.")
                continue
            if piece.color != self.turn:
                print("You can only move your own pieces.")
                continue
            if len(self.legal_moves(piece)) == 0:
                print("This piece has no legal moves.")
                continue
            break

        print(f"Legal moves for {old_position}: {self.legal_moves(piece)}")

        while True:
            new_position = input("Enter the new position for the piece (e.g., 'e4'): ")
            if new_position not in self.legal_moves(piece):
                print("Invalid move.")
                continue
            if piece.Move(new_position):
                if isinstance(piece, Pawn) and (new_position[1] == '1' or new_position[1] == '8'):
                    while True:
                        new_piece_type = input("Promote pawn to (queen, rook, bishop, knight): ")
                        if new_piece_type in ['queen', 'rook', 'bishop', 'knight']:
                            piece.promote(new_piece_type)
                            break
                        else:
                            print("Invalid promotion piece type.")
                if isinstance(piece, Pawn) and self.board.en_passant_target == new_position:
                    captured_pawn_position = new_position[0] + str(int(new_position[1]) - piece.direction)
                    captured_pawn = self.board.squares[captured_pawn_position]
                    if isinstance(captured_pawn, Pawn) and captured_pawn.color != piece.color:
                        self.board.squares[captured_pawn_position] = None
                        self.board.taken_pieces.append(captured_pawn)
                if isinstance(piece, King) and abs(ord(new_position[0]) - ord(old_position[0])) == 2:
                    if new_position[0] == 'g':
                        rook = self.board.squares['h' + old_position[1]]
                        rook.Move('f' + old_position[1])
                    elif new_position[0] == 'c':
                        rook = self.board.squares['a' + old_position[1]]
                        rook.Move('d' + old_position[1])
                if isinstance(piece, Pawn) and abs(int(new_position[1]) - int(old_position[1])) == 2:
                    self.board.en_passant_target = new_position[0] + str(int(new_position[1]) - piece.direction)
                else:
                    self.board.en_passant_target = None
                self.change_turn()
                break
    def has_any_legal_move(self, color):
        for position, piece in self.board.squares.items():
            if piece is None:
                continue
            if piece.color != color:
                continue
            if self.legal_moves(piece):      
                return True
        return False

    def check_game_over(self, color):
        if self.has_any_legal_move(color):
            return None                      # game continues
        if self.is_in_check(color):
            return 'checkmate'
        return 'stalemate'
    def play(self):
        while True:
            if self.take_turn() == 'over':
                break

game = Game()
game.play()
        



