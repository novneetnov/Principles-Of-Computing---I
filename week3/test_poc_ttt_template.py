from CourseraPoC1.util import poc_simpletest
import poc_ttt_template
import poc_ttt_provided as provided

suite = poc_simpletest.TestSuite()

player = provided.PLAYERX
board = provided.TTTBoard(3)
scores = [[0 for dummy_row in range(board.get_dim())]
          for dummy_col in range(board.get_dim())]


def run_mc_trial(call_obj):

    suite.run_test("\n" + str(board), "", "Test 1:")
    suite.report_results()

# run_mc_trial(poc_ttt_template.mc_trial(board, player))


def run_mc_update_scores(call_obj):

    suite.run_test("\n" + str(board) + "\n" + str(scores), "", "Test 1:")
    suite.report_results()

# poc_ttt_template.mc_trial(board, player)
# run_mc_update_scores(poc_ttt_template.mc_update_scores(scores, board, player))


def run_get_best_move(call_obj):

    suite.run_test(str(call_obj), "Test 1:")
    suite.report_results()

#poc_ttt_template.mc_trial(board, player)
#poc_ttt_template.mc_update_scores(scores, board, player)
run_get_best_move(poc_ttt_template.get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY],
                                            [provided.EMPTY, provided.EMPTY]]), [[0, 0], [3, 0]]))