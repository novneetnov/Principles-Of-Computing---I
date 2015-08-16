
from CourseraPoC1.util import poc_simpletest


def run_suite(merge):

    suite = poc_simpletest.TestSuite()

    suite.run_test(merge([4, 0, 4, 8]), [8, 8, 0, 0], "Test 1:")
    suite.run_test(merge([0, 0, 2, 2]), [4, 0, 0, 0], "Test 2:")
    suite.run_test(merge([2, 2, 0, 0]), [4, 0, 0, 0], "Test 3:")
    suite.run_test(merge([2, 2, 2, 2]), [4, 4, 0, 0], "Test 4:")
    suite.run_test(merge([2, 4, 4, 2]), [2, 8, 2, 0], "Test 5:")
    suite.run_test(merge([4, 4, 8, 8]), [8, 16, 0, 0], "Test 6:")
    suite.run_test(merge([2, 0, 0, 4, 4]), [2, 8, 0, 0, 0], "Test 7:")
    suite.run_test(merge([4]), [4], "Test 8:")
    suite.run_test(merge([8, 16, 16, 8]), [8, 32, 8, 0], "Test 9:")
    suite.run_test(merge([8, 4, 2, 4]), [8, 4, 2, 4], "Test 10:")
    suite.run_test(merge([]), [], "Test 11:")
    suite.run_test(merge([4, 0, 0, 0]), [4, 0, 0, 0], "Test 12:")
    suite.run_test(merge([4, 4, 0, 8, 4, 8]), [8, 8, 4, 8, 0, 0], "Test 13:")
    suite.run_test(merge([0, 0, 0, 8, 4, 8]), [8, 4, 8, 0, 0, 0], "Test 14:")
    suite.report_results()
