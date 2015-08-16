
import random

TRIALS = 10000


class MontyHall:

    def __init__(self):
        self.doors = [0, 1, 2]
        self.wins = 0
        self.loses = 0

    def add_door(self):
        self.doors.append(len(self.doors))

    def remove_door(self):
        self.doors.pop(-1)

    def convergence_probability(self):
        probability = 0.0
        wins = 0
        for _ in range(TRIALS):
            door_lst = list(self.doors)
            car_door = random.choice(door_lst)
            player_door_choice = random.choice(door_lst)
            if car_door != player_door_choice:
                wins += 1
        probability = float(wins) / TRIALS
        return probability

