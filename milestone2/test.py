from subprocess import call

import paths
from helpers import *
from models import Milestone


class Milestone2(Milestone):
    """
    Milestone 2
    """

    def __init__(self):
        super().__init__(milestone=2)


if __name__ == "__main__":
    tests = [
        # (1, 1),
        # (1, 2), 
        # (1, 3),
        # (1, 4),
        # (1, 5),
        # (1, 6),
        # (1, None),
        # (2, None),
        # (3, None),
        # (4, None),
        # (5, None),
        # (6, None),
        # (7, None),
        # (8, None),
        # (9, None),
        # (10, None),
        # (11, None),
        # (12, None),
        (13, None),
    ]

    Milestone2().test(tests=tests)
