# url : http://www.codeskulptor.org/#user39_ixRwYqRAjy_16.py

"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.board = [0]
        
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.board = list(configuration)
       
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        str_board = self.board
        str_board.reverse()
        return str(str_board)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.board[house_num]
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num >= 1:
            if self.board[house_num] == house_num:
                return True
        return False
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self.board[house_num] = 0
            house_num -= 1
            while house_num >= 0:
                self.board[house_num] += 1
                house_num -= 1
            return
    
    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        iter = 1
        len_board = len(self.board)
        while iter < len_board:
            if iter == self.board[iter]:
                return iter
            iter += 1
        return 0
    
    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        play_board = self.board[1:]
        for house_num in play_board:
            if house_num != 0:
                return False
        return True
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        moves_list = []
        while self.choose_move() != 0:
            house_num = self.choose_move()
            self.apply_move(house_num)
            moves_list.append(house_num)
        return moves_list
        
def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 1, 2, 3, 4, 5, 6]    
    my_game.set_board(config1)
    config1.append(89)
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([6, 5, 4, 3, 2, 1, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    # add more tests here
    config2 = [0, 1]
    my_game.set_board(config2)
    
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(0), "Expected: False"
    print "Testing is_legal_move - Computed:", my_game.is_legal_move(1), "Expected: True"
    my_game.apply_move(1)
    print "Testing apply_move - Computed:", str(my_game), "Expected: [0, 1]"
    
    config3 = [5, 0, 0, 0, 0]
    my_game.set_board(config3)
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected: 0"
   
    
test_mancala()


# Import GUI code once you feel your code is correct
from CourseraPoC1.practice.week1 import poc_mancala_gui

poc_mancala_gui.run_gui(SolitaireMancala())
        