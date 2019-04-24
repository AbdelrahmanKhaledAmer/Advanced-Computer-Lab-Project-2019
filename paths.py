from pathlib import Path

import numpy as np

POSSIBLE_ROOTS = [
    'Advanced-Computer-Lab-Project-2019',
    'Project'
]


def _find_ROOT(abs_path):
    while abs_path.name not in POSSIBLE_ROOTS:
        abs_path = abs_path.parent
    return abs_path


ROOT_PATH = _find_ROOT(Path(__file__).absolute())
RES_PATH = 'results'
EXP_PATH = 'expected'
INP_PATH = 'input'
CMP_PATH = 'compare'
SRC_PATH = 'src'


def is_empty(res):
    return res.stat().st_size == 0


def similar_files(path, as_int=False, basename_only=False):
    pattern = '*' + str(path.suffix)
    filenames = list(path.parent.glob(pattern))

    filenames = np.array(filenames)
    filenames = np.sort(filenames)

    if len(filenames) > 0:
        if basename_only:
            path_to_name = np.vectorize(lambda x: x.name)
            filenames = path_to_name(filenames)
        elif as_int:
            path_to_name = np.vectorize(lambda x: x.stem)
            filenames = path_to_name(filenames).astype(int)

    return list(filenames)


def _get_task(milestone, folder, filename, root=ROOT_PATH):
    return root.joinpath('milestone{}'.format(milestone), folder, filename)


def get_test_src(milestone):
    filename = "milestone_{}.py".format(milestone)

    return _get_task(
        milestone=milestone, folder=SRC_PATH, filename=filename)


def get_test_inp(milestone, test, subtest=None):
    filename = "Testcase_{:02d}.txt".format(test)
    if subtest:
        filename = "Testcase_{:02d}_{:02d}.txt".format(test, subtest)

    return _get_task(
        milestone=milestone, folder=INP_PATH, filename=filename)


def get_test_res(milestone, test=None, subtest=None, filename=None):
    if not filename:
        filename = "milestone_{}_result.txt".format(milestone)
        if test:
            filename = "Testcase_{:02d}_result.txt".format(test)
        if subtest:
            filename = "Testcase_{:02d}_{:02d}_result.txt".format(
                test, subtest)

    return _get_task(
        milestone=milestone, folder=RES_PATH, filename=filename)


def get_test_exp(milestone, test, subtest=None):
    filename = "Testcase_{:02d}_result.txt".format(test)
    if subtest:
        filename = "Testcase_{:02d}_{:02d}_result.txt".format(test, subtest)

    return _get_task(
        milestone=milestone, folder=EXP_PATH, filename=filename)


def get_test_cmp(milestone, test=None, subtest=None, filename=None):
    if not filename:
        filename = "Testcase_{:02d}_result.diff".format(test)
        if subtest:
            filename = "Testcase_{:02d}_{:02d}_result.diff".format(
                test, subtest)

    return _get_task(
        milestone=milestone, folder=CMP_PATH, filename=filename)
