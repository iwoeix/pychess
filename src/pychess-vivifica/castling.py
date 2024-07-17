'''
Class for castling rights.
'''

from enum import IntFlag

class CastlingRight(IntFlag):
    WHITE_KINGSIDE, WHITE_QUEENSIDE, BLACK_KINGSIDE, BLACK_QUEENSIDE = (1 << shift for shift in range(4))