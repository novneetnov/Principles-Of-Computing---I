
NUM_DICE = 3
DICE_FACES = 6

REWARD_DOUBLE = 10
REWARD_TRIPLE = 200


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


def any_num_same(combination_rolls, number):
    if len(set(combination_rolls)) + number - 1 == len(combination_rolls):
        return True
    return False


def compute_probability(all_outcomes, num_same):
    num_num_same = 0
    for outcome in all_outcomes:
        if any_num_same(list(outcome), num_same):
            num_num_same += 1
    return float(num_num_same) / len(all_outcomes)


def get_exp_value():
    all_outcomes = gen_all_sequences((1, 2, 3, 4, 5, 6), 3)
    print all_outcomes
    prob_double = compute_probability(all_outcomes, 2)
    prob_triple = compute_probability(all_outcomes, 3)
    exp_value = prob_double * REWARD_DOUBLE + prob_triple * REWARD_TRIPLE
    print "Expected Return : ", exp_value


get_exp_value()