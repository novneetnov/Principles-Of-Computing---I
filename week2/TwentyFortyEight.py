"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    return_line = [0]
    merge_flag = False

    for elem in line:
        if elem != 0:
            if return_line[-1] == elem and merge_flag is False:
                return_line[-1] = 2 * elem
                merge_flag = True
                continue
            else:
                return_line.append(elem)
            merge_flag = False

    return_line.pop(0)
    zeros_lst = [0] * (len(line) - len(return_line))
    return_line.extend(zeros_lst)

    return return_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._init_lst_dict = {UP: [(0, col) for col in range(self._grid_width)],
                          DOWN: [(self._grid_height - 1, col) for col in range(self._grid_width)],
                          LEFT: [(row, 0) for row in range(self._grid_height)],
                          RIGHT: [(row, self._grid_width - 1) for row in range(self._grid_height)]}
        self._cells = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        readable_board = "\n"
        for row in self._cells:
            readable_board += str(row) + "\n"
        return readable_board

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        init_lst = self._init_lst_dict.get(direction)
        len_pre_merge = (self._grid_height * self._grid_width)/len(init_lst)
        legal_move = False
        for head_elem_idx in init_lst:
            pre_merge = []
            lst_head_elem = list(head_elem_idx)
            lst_elem_idx = []

            for dummy_tile_num in range(len_pre_merge):
                pre_merge.append(self._cells[lst_head_elem[0]][lst_head_elem[1]])
                lst_elem_idx.append([lst_head_elem[0], lst_head_elem[1]])
                lst_head_elem[0] += OFFSETS.get(direction)[0]
                lst_head_elem[1] += OFFSETS.get(direction)[1]

            merged = merge(pre_merge)

            for elem_idx in lst_elem_idx:
                self._cells[elem_idx[0]][elem_idx[1]] = merged[lst_elem_idx.index(elem_idx)]

            if not merged.__eq__(pre_merge):
                legal_move = True

        if legal_move:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_squares = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._cells[row][col] == 0:
                    empty_squares.append((row, col))

        rand_square = random.choice(empty_squares)

        rand_int = random.randrange(0, 10)
        if rand_int == 9:
            self._cells[rand_square[0]][rand_square[1]] = 4
        else:
            self._cells[rand_square[0]][rand_square[1]] = 2
        return

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
