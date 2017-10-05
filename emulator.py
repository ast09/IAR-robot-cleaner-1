from random import randrange
from cell import Cell


class Emulator:
    def __init__(self):
        self.map = [[Cell(0, 0) for j in range(3)] for i in range(3)]  # The map matrices containing the cells
        self.algorithm = 0  # 0 for dynamic programming, 1 for MonteCarlo, 2 for Time Differentials
        # rewards and transition model under the idea of ((action reward + time reward), probability of success)
        self.empty_battery = {"go_forward_vacuuming": ((-100 + -1), 0.0),
                              "go_forward_no_vacuuming": ((-100 + -1), 0.0),
                              "rotate_left": ((-100 + -1), 0.0),
                              "rotate_right": ((-100 + -1), 0.0),
                              "vacuum": ((-100 + -1), 0.0)}
        self.critical_battery = {"go_forward_vacuuming": ((-3 + -1), 1.0),
                                 "go_forward_no_vacuuming": ((0 + -1), 1.0),
                                 "rotate_left": ((0 + -1), 1.0),
                                 "rotate_right": ((0 + -1), 1.0),
                                 "vacuum": ((-5 + -1), 1.0)}
        self.sufficient_battery = {"go_forward_vacuuming": ((0 + -1), 1.0),
                                   "go_forward_no_vacuuming": ((0 + -1), 1.0),
                                   "rotate_left": ((0 + -1), 1.0),
                                   "rotate_right": ((0 + -1), 1.0),
                                   "vacuum": ((0 + -1), 1.0)}
        self.front_wall = {"go_forward_vacuuming": (-10, 0.0),
                           "go_forward_no_vacuuming": (-10, 0.0),
                           "rotate_left": (10, 1.0),
                           "rotate_right": (10, 1.0),
                           "vacuum": (0, 1.0)}
        self.right_wall = {"go_forward_vacuuming": (0, 1.0),
                           "go_forward_no_vacuuming": (0, 1.0),
                           "rotate_left": (0, 1.0),
                           "rotate_right": (-10, 1.0),
                           "vacuum": (0, 1.0)}
        self.left_wall = {"go_forward_vacuuming": (0, 1.0),
                          "go_forward_no_vacuuming": (0, 1.0),
                          "rotate_left": (-10, 1.0),
                          "rotate_right": (0, 1.0),
                          "vacuum": (0, 1.0)}
        self.dirty_cell = {"go_forward_vacuuming": (40, 0.9),
                           "go_forward_no_vacuuming": (-40, 0.8),
                           "rotate_left": (0, 1.0),
                           "rotate_right": (0, 1.0),
                           "vacuum": (40, 1.0)}
        self.clean_cell = {"go_forward_vacuuming": (-10, 0.9),
                           "go_forward_no_vacuuming": (5, 0.9),
                           "rotate_left": (0, 1.0),
                           "rotate_right": (0, 1.0),
                           "vacuum": (-10, 1.0)}

    """
    Creates a 3x3 map with random dirtiness state
    """

    def createmap(self):
        nb = 0
        for i in range(3):
            for j in range(3):
                if nb == 0:
                    self.map[i][j] = Cell(i, j, randrange(2), 1)
                else:
                    self.map[i][j] = Cell(i, j, randrange(2))
                nb += 1
        self.printmap()

    """
    Prints the map in the terminal (h = homebase, x = dirty, o = clean)
    """

    def printmap(self):
        for i in range(3):
            line = ""
            for j in range(3):
                if self.map[i][j].home == 1:
                    line += "h"
                elif self.map[i][j].dirty == 1:
                    line += "x"
                elif self.map[i][j].dirty == 0:
                    line += "o"
            print(line)

    """
    Simulate the model according to the algorithm we're using
    """

    def simulate(self):
        return
