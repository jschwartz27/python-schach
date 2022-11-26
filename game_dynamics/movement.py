from abc import ABC

from pieces.piece import Position


class KnightMovement(ABC):

    def get_legal_moves(self, state, position: Position):
        pass


class Diagonals(ABC):
    
    def get_legal_diagonals(self, state, position: Position):
        pass


class Rows(ABC):
    
    def get_legal_rows(self, state, position: Position):
        pass


class PawnMovement(ABC):

    def get_legal_moves(self, state, position: Position):
        pass


class KingMovement(ABC):

    def get_legal_moves(self, state, position: Position):
        pass
