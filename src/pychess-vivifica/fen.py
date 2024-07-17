'''
Function and constants for FEN processing.
'''

from re import fullmatch

FEN_REGULAR_EXPRESSION = r'([rnbqkpRNBQKP1-8]+\/){7}([rnbqkpRNBQKP1-8]+) [bw] (-|K|Q|k|q|(KQ)|(Kk)|(Kq)|(Qk)|(Qq)|(kq)|(KQk)|(KQq)|(Kkq)|(Qkq)|(KQkq)) (([a-h][36])|(-)) \d+ \d+'

STARTING_FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

def is_pseudovalid_fen(fen: str):
    return bool(fullmatch(FEN_REGULAR_EXPRESSION, fen))