'''
Constants and helper function for directions.
'''

from piece import *

NORTH, EAST, SOUTH, WEST = 8, 1, -8, -1
NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST = NORTH + EAST, SOUTH + EAST, SOUTH + WEST, NORTH + WEST

MOVE_DIRECTIONS = ((NORTH, NORTH + NORTH), (NORTH + NORTHEAST, EAST + NORTHEAST, EAST + SOUTHEAST, SOUTH + SOUTHEAST, SOUTH + SOUTHWEST, WEST + SOUTHWEST, WEST + NORTHWEST, NORTH + NORTHWEST), (NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST), (NORTH, EAST, SOUTH, WEST), (NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST), (NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST))
ATTACK_DIRECTIONS = ((NORTHEAST, NORTHWEST), (NORTH + NORTHEAST, EAST + NORTHEAST, EAST + SOUTHEAST, SOUTH + SOUTHEAST, SOUTH + SOUTHWEST, WEST + SOUTHWEST, WEST + NORTHWEST, NORTH + NORTHWEST), (NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST), (NORTH, EAST, SOUTH, WEST), (NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST), (NORTH, NORTHEAST, EAST, SOUTHEAST, SOUTH, SOUTHWEST, WEST, NORTHWEST))

def relative_direction(direction: int, color: Color):
    return -direction if color else direction