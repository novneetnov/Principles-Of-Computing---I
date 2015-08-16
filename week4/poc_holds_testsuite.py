"""
Test suite for gen_all_holds in "Yahtzee"
"""

import CourseraPoC1.util.poc_simpletest as poc_simpletest


def run_gen_all_holds(gen_all_holds):
    """
    Some informal testing code for gen_all_holds
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test gen_all_holds on various inputs
    hand = tuple([])
    suite.run_test(gen_all_holds(hand), set([()]), "Test #1:")

    hand = tuple([2, 4])
    suite.run_test(gen_all_holds(hand), set([(), (2,), (4,), (2, 4)]), "Test #2:")
    
    hand = tuple((3, 3, 3))
    suite.run_test(gen_all_holds(hand), set([(), (3,), (3, 3), (3, 3, 3)]), "Test #3:")

    hand = tuple((1, 2, 2))
    suite.run_test(gen_all_holds(hand), set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #4:")

    hand = tuple([2, 3, 6])
    suite.run_test(gen_all_holds(hand), set([(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)]), "Test #5:")

    suite.report_results()


def run_score(score):
    """
    Some informal testing code for score
    """

   # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test score on various inputs
    hand = tuple([1, 2, 2, 4, 5])
    suite.run_test(score(hand), 5, "Test #1")

    hand = tuple([])
    suite.run_test(score(hand), 0, "Test #2")

    hand = tuple((2, 2, 2, 2, 2))
    suite.run_test(score(hand), 10, "Test #3")

    suite.report_results()


def run_expected_value(expected_value):
    """
    Some informal testing code for expected_value
    """

    #create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test score on various inputs
    hand = tuple([1, 2, 3, 4, 5])
    held_dice = tuple([hand[0], hand[1]])
    num_free_dice = len(hand) - len(held_dice)
    suite.run_test(expected_value(held_dice, 6, num_free_dice), 6.4722, "Test #1")

    hand = tuple([6, 6, 6, 6, 6])
    held_dice = tuple(hand)
    num_free_dice = len(hand) - len(held_dice)
    suite.run_test(expected_value(held_dice, 6, num_free_dice), 30.0, "Test #2")

    hand = tuple([6, 6, 6, 6, 6])
    held_dice = tuple(hand[0:4])
    num_free_dice = len(hand) - len(held_dice)
    suite.run_test(expected_value(held_dice, 6, num_free_dice), 25.0, "Test #3")

    hand = tuple([6, 6, 6, 6, 6])
    held_dice = tuple(hand[0:3])
    num_free_dice = len(hand) - len(held_dice)
    suite.run_test(expected_value(held_dice, 6, num_free_dice), 20.0, "Test #4")