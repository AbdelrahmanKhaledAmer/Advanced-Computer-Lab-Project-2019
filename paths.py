from pathlib import Path

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


def _get_task(milestone, folder, filename, root=ROOT_PATH):
    return root.joinpath('milestone{}'.format(milestone), folder, filename)


def get_test_src(milestone, subtest=None):
    filename = "milestone_{}.py".format(milestone)

    return _get_task(
        milestone=milestone, folder=SRC_PATH, filename=filename)


def get_test_inp(milestone, test, subtest=None):
    filename = "Testcase_{:02d}.txt".format(test)
    if subtest:
        filename = "Testcase_{:02d}_{:02d}.txt".format(test, subtest)

    return _get_task(
        milestone=milestone, folder=INP_PATH, filename=filename)


def get_test_res(milestone, test, subtest=None):
    pass


def get_test_exp(milestone, test, subtest=None):
    filename = "Testcase_{:02d}_result.txt".format(test)
    if subtest:
        filename = "Testcase_{:02d}_{:02d}_result.txt".format(test, subtest)

    return _get_task(
        milestone=milestone, folder=INP_PATH, filename=filename)


def get_test_cmp(milestone, test, subtest=None):
    filename = "Testcase_{:02d}_result.diff".format(test)
    if subtest:
        filename = "Testcase_{:02d}_{:02d}_result.diff".format(test, subtest)

    return _get_task(
        milestone=milestone, folder=INP_PATH, filename=filename)
