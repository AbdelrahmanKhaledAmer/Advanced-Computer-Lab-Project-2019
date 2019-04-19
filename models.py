import numpy as np

import paths
from helpers import *


class Milestone:
    def __init__(self, milestone):
        self.milestone = milestone

    def test(self, tests):
        print()
        printInfo("Milestone{:02d}:".format(self.milestone))

        self.pre_testing()

        for test, subtest in tests:
            self.execute(test=test, subtest=subtest)
            self.compare(test=test, subtest=subtest)

    def pre_testing(self):
        res_dir = paths.get_test_res(milestone=self.milestone, test=1).parent
        clean_dir(res_dir)

        cmp_dir = paths.get_test_cmp(milestone=self.milestone, test=1).parent
        clean_dir(cmp_dir)

    def execute(self, test, subtest=None):
        # PART I: Exectute the Test
        # get source file
        src_file = paths.get_test_src(milestone=self.milestone)

        # get input file
        inp_file = paths.get_test_inp(
            milestone=self.milestone, test=test, subtest=subtest)

        # get actual result file
        res_file = paths.get_test_res(
            milestone=self.milestone, test=test, subtest=subtest)

        # execute files
        execute_python(
            src_file=src_file,
            res_dir=res_file.parent,
            args={"file": inp_file})

        # PART II: Change output filename
        # change output filename
        out_file = paths.get_test_res(milestone=self.milestone)
        copy_file(file1=out_file.name,
                  file2=res_file.name,
                  dir=res_file.parent)

    def compare(self, test, subtest=None):
        # get actual result file
        res_file = paths.get_test_res(
            milestone=self.milestone, test=test, subtest=subtest)

        # get expected result file
        exp_file = paths.get_test_exp(
            milestone=self.milestone, test=test, subtest=subtest)

        # get compare file path
        cmp_file = paths.get_test_cmp(
            milestone=self.milestone, test=test, subtest=subtest)

        # create .DIFF file
        git_diff(file1=exp_file, file2=res_file, result=cmp_file)

        # get input file
        inp_file = paths.get_test_inp(
            milestone=self.milestone, test=test, subtest=subtest)

        # Check .DIFF files is empty
        if not paths.is_empty(cmp_file):
            printAlert(cmp_file.name, "failed\t", str(inp_file))
        else:
            printSuccess(cmp_file.name, "success\t", str(inp_file))
