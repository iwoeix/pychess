'''
Class for moves.
'''

from piece import *
from square import *

class Move:
    def __init__(self, starting_square: Square = Square.A1, destination_square: Square = Square.A1, promotion: PieceType | None = None):
        self.starting_square, self.destination_square, self.promotion = starting_square, destination_square, promotion