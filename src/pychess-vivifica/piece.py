'''
Classes, constant and helper function for pieces.
'''

from enum import IntEnum

class Color(IntEnum):
    WHITE, BLACK = range(2)

def opposite_side(color: Color):
    return Color(not color)

class PieceType(IntEnum):
    PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = range(6)

PROMOTION_PIECE_TYPES = (PieceType.KNIGHT, PieceType.BISHOP, PieceType.ROOK, PieceType.QUEEN)

def color_of(character: str):
    return Color(character.islower())

def piece_type_of(character: str):
    match character.upper():
        case 'R':
            return PieceType.ROOK
        case 'N':
            return PieceType.KNIGHT
        case 'B':
            return PieceType.BISHOP
        case 'Q':
            return PieceType.QUEEN
        case 'K':
            return PieceType.KING
        case 'P':
            return PieceType.PAWN

def from_color_piece_type(color: Color | None, piece_type: PieceType | None):
    match piece_type:
        case PieceType.ROOK:
            character = 'R'
        case PieceType.KNIGHT:
            character = 'N'
        case PieceType.BISHOP:
            character = 'B'
        case PieceType.QUEEN:
            character = 'Q'
        case PieceType.KING:
            character = 'K'
        case PieceType.PAWN:
            character = 'P'
        case _:
            character = '.'
    return character.lower() if color else character