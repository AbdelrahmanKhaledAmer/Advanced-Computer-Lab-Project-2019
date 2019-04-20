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
    return [(x, None) for x in range(from_, to_+1)]
    # arr.extend(extra)


if __name__ == "__main__":
    tests = list()

    # # official tests
    # tests += [(1, x) for x in range(1, 7)]
    # tests += [(x, None) for x in range(1, 12)]

    # # var, let, const expr test 
    # var_tests = add_tests(from_=1001, to_=1025, arr=tests)
    # tests += var_tests

    # # if test
    # if_tests = add_tests(from_=2101, to_=2113, arr=tests)
    # tests += if_tests

    # # when test
    # when_tests = add_tests(from_=2201, to_=2201, arr=tests)
    # tests += when_tests

    # # while test
    # while_tests = add_tests(from_=2301, to_=2307, arr=tests)
    # tests += while_tests

    # case test
    case_tests = add_tests(from_=2401, to_=2405, arr=tests)
    tests += case_tests

    # # assert test 
    # assert_tests = add_tests(from_=2501, to_=2501, arr=tests)
    # tests += assert_tests

    # # block test 
    # block_tests = add_tests(from_=2601, to_=2603, arr=tests)
    # tests += block_tests

    # # break test 
    # break_tests = add_tests(from_=2701, to_=2704, arr=tests)
    # tests += break_tests

    # # import test 
    # import_tests = add_tests(from_=3001, to_=3005, arr=tests)
    # tests += import_tests

    # # macro test
    # macro_tests = add_tests(from_=4101, to_=4101, arr=tests)
    # tests += macro_tests

    # # template test
    # template_tests = add_tests(from_=4201, to_=4201, arr=tests)
    # tests += template_tests

    # # type test 
    # type_tests = add_tests(from_=4301, to_=4303, arr=tests)
    # tests += type_tests

    # # proc test
    # proc_tests = add_tests(from_=4401, to_=4412, arr=tests)
    # tests += proc_tests

    # # for loop test 
    # for_tests = add_tests(from_=5001, to_=5016, arr=tests)
    # tests += for_tests

    Milestone2().test(tests=tests)
