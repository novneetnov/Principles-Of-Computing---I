
from CourseraPoC1.util import poc_simpletest
import TwentyFortyEight

suite = poc_simpletest.TestSuite()


def run_reset(call_obj):

    call_obj.new_tile()
    call_obj.new_tile()
    call_obj.new_tile()
    call_obj.move("UP")
    print call_obj
    call_obj.reset()

    suite.run_test(call_obj, [8, 8, 0, 0], "Test 1:")
    suite.report_results()

# run_reset(TwentyFortyEight.TwentyFortyEight(4, 4))


def run_str(call_obj):

    suite.run_test(call_obj.__str__(), [], "Test 1:")
    call_obj.new_tile()
    suite.run_test(call_obj.__str__(), [], "Test 2:")
    call_obj.new_tile()
    suite.run_test(call_obj.__str__(), [], "Test 3:")
    call_obj.move("UP")
    suite.run_test(call_obj.__str__(), [], "Test 4:")
    call_obj.set_tile(3, 3, 4)
    suite.run_test(call_obj.__str__(), [], "Test 5:")
    call_obj.reset()
    suite.run_test(call_obj.__str__(), [], "Test 6:")
    suite.report_results()

# run_str(TwentyFortyEight.TwentyFortyEight(4, 4))


def run_new_tile(call_obj):

    call_obj.new_tile()
    suite.run_test(call_obj, [8, 8, 0, 0], "Test 1:")
    call_obj.new_tile()
    suite.run_test(call_obj, [8, 8, 0, 0], "Test 2:")
    call_obj.new_tile()
    suite.run_test(call_obj, [8, 8, 0, 0], "Test 3:")
    call_obj.new_tile()
    suite.run_test(call_obj, [8, 8, 0, 0], "Test 4:")
    suite.report_results()

# run_new_tile(TwentyFortyEight.TwentyFortyEight(4, 4))

def run_move(call_obj):

    call_obj.set_tile(0, 0, 2)
    call_obj.set_tile(0, 1, 2)
    print call_obj
    call_obj.move(TwentyFortyEight.LEFT)
    suite.run_test(call_obj, "", "Test 1:")

    call_obj.set_tile(0, 0, 2)
    call_obj.set_tile(1, 0, 2)
    print call_obj
    call_obj.move(TwentyFortyEight.UP)
    suite.run_test(call_obj, "", "Test 1:")

run_move(TwentyFortyEight.TwentyFortyEight(4, 4))