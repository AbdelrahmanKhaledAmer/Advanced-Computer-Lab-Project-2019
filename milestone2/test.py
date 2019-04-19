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


def add_tests(from_, to_, arr):
    extra = [(x, None) for x in range(from_, to_+1)]
    arr.extend(extra)


if __name__ == "__main__":
    tests = list()

    # official tests
    tests += [(1, x) for x in range(1, 7)]
    tests += [(x, None) for x in range(1, 12)]

    # var, let, const expr test
    add_tests(from_=1001, to_=1025, arr=tests)

    # if test
    add_tests(from_=2101, to_=2103, arr=tests)

    # when test
    add_tests(from_=2201, to_=2201, arr=tests)

    # while test
    add_tests(from_=2301, to_=2307, arr=tests)

    # case test
    add_tests(from_=2401, to_=2405, arr=tests)

    # assert test
    add_tests(from_=2501, to_=2501, arr=tests)

    # block test
    add_tests(from_=2601, to_=2603, arr=tests)

    # break test
    add_tests(from_=2701, to_=2704, arr=tests)

    # import test
    add_tests(from_=3001, to_=3005, arr=tests)

    # macro test
    add_tests(from_=4101, to_=4101, arr=tests)

    # template test
    add_tests(from_=4201, to_=4201, arr=tests)

    # type test
    add_tests(from_=4301, to_=4302, arr=tests)

    # proc test
    add_tests(from_=4401, to_=4412, arr=tests)

    # for loop test
    add_tests(from_=5001, to_=5016, arr=tests)

    Milestone2().test(tests=tests)
