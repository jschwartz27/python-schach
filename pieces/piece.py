from abc import ABC

from data_types.data_types import Color, PieceType, Rank, File


class Position:

    def __init__(self, file: File, rank: Rank):
        self.update(file, rank)

    def update(self, file: str, rank: int):
        self.file: File = file
        self.rank: Rank = rank

    def __str__(self):
        return f"{self.file}{self.rank}"


class Piece(ABC):

    def __init__(self, color: Color, position: Position, piece_type: PieceType):
        self._has_moved = False
        self._color: Color = color
        self._position: Position = position
        self._piece_type: PieceType = piece_type

    def __str__(self):
        # return f"{self._piece_type}-{self._position}"
        letter = str(self._piece_type)[0]
        if self._color == Color.BLACK:
            letter = letter.lower()
        return f"{letter}"


class King(Piece):

    def __init__(self, color: Color, position: Position):
        super().__init__(color, position, PieceType.KING)


class Queen(Piece):

    def __init__(self, color: Color, position: Position):
        super().__init__(color, position, PieceType.QUEEN)


class Rook(Piece):

    def __init__(self, color: Color, position: Position):
        super().__init__(color, position, PieceType.ROOK)


class Knight(Piece):

    def __init__(self, color: Color, position: Position):
        super().__init__(color, position, PieceType.KNIGHT)


class Bishop(Piece):

    def __init__(self, color: Color, position: Position):
        super().__init__(color, position, PieceType.BISHOP)


class Pawn(Piece):

    def __init__(self, color: Color, position: Position):
        super().__init__(color, position, PieceType.PAWN)
