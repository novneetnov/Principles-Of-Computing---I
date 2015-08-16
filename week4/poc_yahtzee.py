"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)
import random


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    max_score = 0
    for _dice in hand:
        dice_score = _dice * hand.count(_dice)
        if dice_score > max_score:
            max_score = dice_score

    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = range(1, num_die_sides + 1)
    all_free_dice_seq = gen_all_sequences(outcomes, num_free_dice)
    all_seq = combine_tuple(all_free_dice_seq, held_dice)
    score_lst = []
    for seq in all_seq:
        score_lst.append(score(tuple(sorted(seq))))
    exp_value = 0
    for score_var in score_lst:
        exp_value += float(score_var) / len(score_lst)

    return exp_value


def combine_tuple(set_of_tuples, _tuple):
    ans = set([])
    for _ in set_of_tuples:
        ans.add(_ + _tuple)
    return ans


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_hold_set = set([])
    for hold_num in range(len(hand) + 1):
        hold_num_set = gen_all_combinations(hand, hold_num)
        all_hold_set = all_hold_set.union(hold_num_set)

    return all_hold_set


def gen_all_combinations(given_tuples, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in given_tuples:
                new_sequence = list(partial_sequence)
                if new_sequence.count(item) < given_tuples.count(item):
                    new_sequence.append(item)
                    new_sequence_sorted = sorted(new_sequence)
                    temp_set.add(tuple(new_sequence_sorted))
        answer_set = temp_set
    return answer_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_possible_holds = gen_all_holds(hand)
    max_exp_value = 0
    req_tuple_lst = []
    for _hold in all_possible_holds:
        num_free_dice = len(hand) - len(_hold)
        sorted_hold = tuple(sorted(_hold))
        exp_value = expected_value(sorted_hold, num_die_sides, num_free_dice)
        print "hold : ", sorted_hold, " : expected value : ", exp_value
        if exp_value > max_exp_value:
            req_tuple_lst = [(exp_value, sorted_hold)]
            max_exp_value = exp_value
        elif exp_value == max_exp_value:
            req_tuple_lst.append((exp_value, sorted_hold))
    print req_tuple_lst
    return random.choice(req_tuple_lst)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 1, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


run_example()


import poc_holds_testsuite
#poc_holds_testsuite.run_score(score)
#poc_holds_testsuite.run_expected_value(expected_value)
#poc_holds_testsuite.run_gen_all_holds(gen_all_holds)
                                       
    
    
    



