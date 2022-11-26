import numpy as np
from typing import List

from data_types.data_types import Color, File, Rank
from pieces.piece import Bishop, King, Knight, Piece, Queen, Pawn, Position, Rook


class Universe:
    
    # for destroyed pieces
    __annihilated: List[Piece] = list()

    def __init__(self):
        self.__state = self.__initialize_state()

    def get_state(self) -> np.ndarray:
        return self.__state

    @staticmethod
    def __initialize_state() -> np.ndarray:
        # initialize board with all zeros
        state = np.zeros([8, 8], dtype="O")
        for i, file_c in enumerate([(Rank.ONE, Rank.TWO), (Rank.EIGHT, Rank.SEVEN)]):
            color: Color = Color.WHITE if i == 0 else Color.BLACK
            main_rank: Rank = file_c[0]
            pawn_rank = file_c[1]
            m_rank = [
                Rook(color, Position(File.A, main_rank)),
                Knight(color, Position(File.B, main_rank)),
                Bishop(color, Position(File.C, main_rank)),
                Queen(color, Position(File.D, main_rank)),
                King(color, Position(File.E, main_rank)),
                Bishop(color, Position(File.F, main_rank)),
                Knight(color, Position(File.G, main_rank)),
                Rook(color, Position(File.H, main_rank)),
            ]
            # add pawns
            p_rank = [Pawn(color, Position(file, pawn_rank)) for file in File]
            state[main_rank], state[pawn_rank] = m_rank, p_rank

        return state
    
    def __repr__(self) -> str:

        def get_checkerboard(i: int, j: int) -> str:
            # "__" will represent black squares
            return "__" if (i + j) % 2 == 0 else "  "

        state_str = "\n"
        for i, rank in list(enumerate(self.get_state()))[::-1]:  # TODO np.flip rotates, but something else?
            rank_str = "\t"
            for j, place in enumerate(rank):
                if place == 0:
                    rank_str += get_checkerboard(i, j)
                else:
                    rank_str += str(place) + " "
            state_str += rank_str + "\n"

        return state_str
