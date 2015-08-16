"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.


def mc_trial(board, player):
    """ plays a game by choosing random squares and return when the game is over
    :param board: The current board.
    :param player: The player to move.
    :return: None, Changes the configuration of the board.
    """
    while board.check_win() is None:
        empty = board.get_empty_squares()
        (row, col) = random.choice(empty)
        board.move(row, col, player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """ Updates the scores of this board to the previous board,
    :param scores:The score of before this trial,
    :param board:The current board whose score is to be updated.
    :param player:The player to move.
    :return:None
    """
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            winner = board.check_win()
            if winner == player:
                if board.square(row, col) == winner:
                    scores[row][col] += SCORE_CURRENT
                elif board.square(row, col) is provided.EMPTY:
                    scores[row][col] += 0.0
                else:
                    scores[row][col] -= SCORE_OTHER
            elif winner == provided.switch_player(player):
                if board.square(row, col) == winner:
                    scores[row][col] += SCORE_OTHER
                elif board.square(row, col) is provided.EMPTY:
                    scores[row][col] += 0.0
                else:
                    scores[row][col] -= SCORE_CURRENT


def get_best_move(board, scores):
    """ Returns the move with the highest score,
    :param board: The current board.
    :param scores: The scores after the MC simulations.
    :return:The tuple (row, col) which is the best predicted move,
    """
    max_score_squares = []
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) == provided.EMPTY:
                if max_score_squares == []:
                    max_score = scores[row][col]
                if scores[row][col] > max_score:
                    max_score = scores[row][col]
                    max_score_squares = [(row, col)]
                elif scores[row][col] == max_score:
                    max_score_squares.append((row, col))
    if not max_score_squares == []:
        best_move = random.choice(max_score_squares)
    else:
        return 0, 0
    return best_move


def mc_move(board, player, trials):
    """ Runs the trials and predicts the best possible move.
    :param board: The current board.
    :param player: The player to move.
    :param trials: Number of trials for which the simulation is run,
    :return: Returns the best predicted move,
    """
    scores = [[0 for dummy_col in range(board.get_dim())]
              for dummy_row in range(board.get_dim())]
    best_move = (0, 0)
    for _ in range(trials):
        duplicate_board = board.clone()
        mc_trial(duplicate_board, player)
        if duplicate_board.check_win() != provided.DRAW:
            mc_update_scores(scores, duplicate_board, player)

    best_move = get_best_move(board, scores)
    return best_move


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
