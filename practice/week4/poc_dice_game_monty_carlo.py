
import random

NUM_TRIALS = 1000000
NUM_DICE = 3
DICE_FACES = 6


def generate_rolls():
    roll_values = []
    for _ in range(NUM_DICE):
        roll = random.choice(range(1, DICE_FACES + 1))
        roll_values.append(roll)
    return roll_values


def any_num_same(combination_rolls, number):
    if len(set(combination_rolls)) + number - 1 == len(combination_rolls):
        return True
    return False


def play_game():
    money_won = 0
    money_paid = 0
    for _ in range(NUM_TRIALS):
        money_paid += 10
        combination_rolls = generate_rolls()
        if any_num_same(combination_rolls, 3):
            money_won += 200
        elif any_num_same(combination_rolls, 2):
            money_won += 10

    print "Money paid : ", money_paid
    print "Money won : ", money_won
    print "Money won per trial : ", float(money_won) / NUM_TRIALS

play_game()