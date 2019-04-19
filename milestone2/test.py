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


def add_tests(arr, upper, base):
    arrB = [(base+x, None)for x in range(1, upper+1)]
    arr.extend(arrB)


OFFSET_VAR = 1000
OFFSET_FOR = 5000
OFFSET_IF = 2100
OFFSET_WHEN = 2200
OFFSET_WHILE = 2300
OFFSET_CASE = 2400
OFFSET_ASSERT = 2500
OFFSET_BLOCK = 2600
OFFSET_BREAK = 2700
OFFSET_MACRO = 4100
OFFSET_TEMPLATE = 4200
OFFSET_TYPE = 4300
OFFSET_PROC = 4400

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
    ]

    # var, let, const expr test
    add_tests(base=OFFSET_VAR, upper=25, arr=tests)

    # if test
    add_tests(base=OFFSET_IF, upper=13, arr=tests)

    # when test
    add_tests(base=OFFSET_WHEN, upper=1, arr=tests)

    # while test
    add_tests(base=OFFSET_WHILE, upper=7, arr=tests)

    # case test
    add_tests(base=OFFSET_CASE, upper=5, arr=tests)

    # assert test
    add_tests(base=OFFSET_ASSERT, upper=1, arr=tests)

    # block test
    add_tests(base=OFFSET_BLOCK, upper=3, arr=tests)

    # break test
    add_tests(base=OFFSET_BREAK, upper=4, arr=tests)

    # macro test
    add_tests(base=OFFSET_MACRO, upper=1, arr=tests)

    # template test
    add_tests(base=OFFSET_TEMPLATE, upper=1, arr=tests)

    # type test
    add_tests(base=OFFSET_TYPE, upper=2, arr=tests)

    # proc test
    add_tests(base=OFFSET_PROC, upper=12, arr=tests)

    # for loop test
    add_tests(base=OFFSET_FOR, upper=16, arr=tests)

    Milestone2().test(tests=tests)
