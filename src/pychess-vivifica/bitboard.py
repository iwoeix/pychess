'''
Helper function and constants for bitboards.
'''

from array import array

EMPTY_BITBOARD, FULL_BITBOARD = 0, (1 << 64) - 1
RANK_BITBOARDS = array('Q', (0xff << shift for shift in range(0, 64, 8)))
FILE_BITBOARDS = array('Q', (0x0101010101010101 << shift for shift in range(8)))
SQUARE_BITBOARDS = array('Q', (1 << shift for shift in range(64)))

def set_positions(bitboard: int):
    while bitboard:
        yield (bitboard & -bitboard).bit_length() - 1
        bitboard &= bitboard - 1