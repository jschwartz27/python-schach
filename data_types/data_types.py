from enum import Enum, IntEnum


class Rank(IntEnum):
    ONE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7

    def __str__(self) -> str:
        return str(self.value + 1)


class File(IntEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7

    def __str__(self) -> str:
        return self.name


class PieceType(Enum):
    KING = "king"
    QUEEN = "queen"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    PAWN = "pawn"

    def __str__(self):
        if self.value == "knight":
            return "N"
        return self.value.capitalize()


class Color(Enum):
    WHITE = "white"
    BLACK = "black"

    def __str__(self):
        return self.value.capitalize()
