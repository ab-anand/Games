"""
Clone of 2048 game.
"""
# __author__ = Abhinav Anand
# project url = http://www.codeskulptor.org/#user44_IZFKLJElC29dav7.py 

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
    counter = 0
    new_list = [0]*len(line)
    result_list = [0]*len(line)
    
    for num in line:
        if num != 0:
            new_list[counter] = num
            counter += 1
            
    for counter in range(len(line)-1):
        if new_list[counter] == new_list[counter+1]:
            new_list[counter] *= 2
            new_list[counter+1] = 0
            counter += 2
            
    counter = 0    
    for num in new_list:
        if num != 0:
            result_list[counter] = num
            counter += 1        
            
    return result_list



class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.set_initial_tiles()
        self.reset()
           
    def set_initial_tiles(self):
        """
        For each direction, pre-computes a list of the indices
        for the initial tiles in that direction
        """
        self._initial_tiles_dict = {}

        tiles = []

        # temp dictionary for fetching increment counters
        # for each direction

        temp_offset_dict = {

            UP      : (0, 1),
            DOWN    : (self.get_grid_height() - 1, 1),
            LEFT    : (1, 0),
            RIGHT   : (1, self.get_grid_width() - 1)
        }

        # sets up the initial_tiles_dict for each direction

        for direction in range(1,5):

            # fetches the increment counters from
            # temp_offset_dict dict
            row_increment = temp_offset_dict[direction][0]
            col_increment = temp_offset_dict[direction][1]

            # direction is either UP or DOWN
            if col_increment == 1:
                for col in range(self.get_grid_width()):
                    tiles.append((row_increment, col))


            # direction is either LEFT or RIGHT
            if row_increment == 1:
                for row in range(self.get_grid_height()):
                    tiles.append((row, col_increment))


            self._initial_tiles_dict[direction] = tiles

            tiles = []
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_row in range(self.get_grid_width())] for dummy_col in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        board = ""
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                board = board + str(self._grid[row][col]) + " "
            board = board + "\n"
        return board

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
        initial_tiles = self._initial_tiles_dict[direction]
        if direction == UP or direction == DOWN:
            steps = self.get_grid_height()
        else:
            steps = self.get_grid_width()
        
        changed = False
        
        for tile_index in range(len(initial_tiles)):
            x_incr = OFFSETS[direction][0]
            y_incr = OFFSETS[direction][1]
            
            temp_list = []
            
            for step in range(steps):
                row = initial_tiles[tile_index][0] + step*x_incr
                col = initial_tiles[tile_index][1] + step*y_incr

                temp_list.append(self.get_tile(row, col))
           
            merged_list = merge(temp_list)
            
            for step in range(steps):
                row = initial_tiles[tile_index][0] + step*x_incr
                col = initial_tiles[tile_index][1] + step*y_incr
                
                self.set_tile(row, col, merged_list[step])
                
            if merged_list != temp_list:
                changed = True
                
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        values = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        rand_row = random.randint(0, self.get_grid_height()-1)
        rand_col = random.randint(0, self.get_grid_width()-1)
        while self._grid[rand_row][rand_col] != 0:
            rand_row = random.randint(0, self.get_grid_height()-1)
            rand_col = random.randint(0, self.get_grid_width()-1)
            
        self._grid[rand_row][rand_col] = random.choice(values)
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

M_G9_ = TwentyFortyEight(2, 3)
poc_2048_gui.run_gui(M_G9_)
print str(M_G9_)
