'''
Board representation and move generation.
'''

from array import array
from piece import *
from square import *
from bitboard import *
from direction import *
from move import *
from castling import *
from fen import *

class Board:
    def __init__(self):
        self.color_bitboards = array('Q', (EMPTY_BITBOARD,) * 2)
        self.piece_type_bitboards = array('Q', (EMPTY_BITBOARD,) * 6)
        self.pinned_bitboards = array('Q', (EMPTY_BITBOARD,) * 5)
        self.side_to_move = Color.WHITE
        self.castling_rights = CastlingRight(0)
        self.halfmoves = self.fullmoves = 0
        self.en_passant_square = None
    
    def get_all_pieces_bitboard(self):
        return self.color_bitboards[Color.WHITE] | self.color_bitboards[Color.BLACK]

    def get_bitboard(self, color: Color | None = None, piece_type: PieceType | None = None):
        bitboard = self.get_all_pieces_bitboard()
        if color is not None:
            bitboard &= self.color_bitboards[color]
        if piece_type is not None:
            bitboard &= self.piece_type_bitboards[piece_type]
        return bitboard
    
    def get_pieces(self, color: Color | None, piece_type: PieceType | None):
        return set_positions(self.get_bitboard(color, piece_type))
    
    def get_color(self, square: Square):
        for color in iter(Color):
            if self.color_bitboards[color] >> square & 1:
                return color
        return None
    
    def get_piece_type(self, square: Square):
        for piece_type in iter(PieceType):
            if self.piece_type_bitboards[piece_type] >> square & 1:
                return piece_type
        return None
    
    def add_piece(self, square: Square, color: Color, piece_type: PieceType):
        self.color_bitboards[color] |= 1 << square
        self.piece_type_bitboards[piece_type] |= 1 << square
    
    def remove_piece(self, square: Square):
        color, piece_type = self.get_color(square), self.get_piece_type(square)
        if color is not None:
            self.color_bitboards[color] &= ~(1 << square)
        if piece_type is not None:
            self.piece_type_bitboards[piece_type] &= ~(1 << square)
    
    def set_piece(self, square: Square, color: Color, piece_type: PieceType):
        self.remove_piece(square)
        self.add_piece(square, color, piece_type)

    @classmethod
    def from_fen(cls, fen: str = STARTING_FEN):
        if not is_pseudovalid_fen(fen):
            raise Exception()
        pieces, side_to_move, castling_rights, en_passant_square, halfmoves, fullmoves = fen.split()
        board = Board()
        for rank, rank_pieces in enumerate(pieces.split('/')):
            rank = relative_rank(Rank(rank), Color.BLACK)
            file = File.A
            for character in rank_pieces:
                if character.isdigit():
                    file = file + int(character)
                    try:
                        file = File(file)
                    except ValueError:
                        break
                else:
                    color, piece_type = color_of(character), piece_type_of(character)
                    board.add_piece(from_file_rank(file, rank), color, piece_type)
                    file = file + 1
                    try:
                        file = File(file)
                    except ValueError:
                        break
        board.side_to_move = Color(side_to_move == 'b')
        for character in castling_rights:
            match character:
                case 'K':
                    board.castling_rights |= CastlingRight.WHITE_KINGSIDE
                case 'Q':
                    board.castling_rights |= CastlingRight.WHITE_QUEENSIDE
                case 'k':
                    board.castling_rights |= CastlingRight.BLACK_KINGSIDE
                case 'q':
                    board.castling_rights |= CastlingRight.BLACK_QUEENSIDE
        board.en_passant_square = square_from(en_passant_square)
        board.halfmoves = int(halfmoves)
        board.fullmoves = int(fullmoves)
        return board
        