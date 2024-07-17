'''
Classes and helper functions for squares.
'''

from enum import IntEnum
from direction import *
from piece import *

class Square(IntEnum):
    A1, B1, C1, D1, E1, F1, G1, H1, A2, B2, C2, D2, E2, F2, G2, H2, A3, B3, C3, D3, E3, F3, G3, H3, A4, B4, C4, D4, E4, F4, G4, H4, A5, B5, C5, D5, E5, F5, G5, H5, A6, B6, C6, D6, E6, F6, G6, H6, A7, B7, C7, D7, E7, F7, G7, H7, A8, B8, C8, D8, E8, F8, G8, H8 = range(64)

class File(IntEnum):
    A, B, C, D, E, F, G, H = range(8)

class Rank(IntEnum):
    ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT = range(8)

def get_file(square: Square):
    return File(square & 7)

def get_rank(square: Square):
    return Rank(square >> 3)

def get_file_rank(square: Square):
    return get_file(square), get_rank(square)

def from_file_rank(file: File, rank: Rank):
    return Square(rank << 3 | file)

def shift(square: Square, direction: int):
    return Square(square + direction)

def relative_rank(rank: Rank, color: Color):
    return Rank(rank ^ 7 if color else rank)

def relative_square(square: Square, color: Color):
    return Square(square ^ 56 if color else square)

def file_from(character: str):
    if len(character) == 1 and character in 'abcdefgh':
        return File(ord(character) - 97)

def rank_from(character: str):
    if len(character) == 1 and character in '12345678':
        return Rank(int(character))

def square_from(string: str):
    if len(string) == 2:
        return from_file_rank(file_from(string[0]), rank_from(string[1]))