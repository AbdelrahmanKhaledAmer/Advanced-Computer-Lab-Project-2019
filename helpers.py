import shutil
from subprocess import call

__all__ = [
    'execute_python', 'git_diff', 'printAlert', 'printSuccess', 'printInfo',
    'copy_file', 'delete_directory', 'clean_dir'
]


def execute_python(src_file, res_dir, args):
    command = "cd \"{}\" && python \"{}\" ".format(res_dir, src_file)
    for k, v in args.items():
        command += "--{} \"{}\" ".format(k, v)

    # print(command)
    call(command, shell=True)


def git_diff(file1, file2, result):
    command = "git diff --no-index \"{}\" \"{}\" > \"{}\"".format(
        file1, file2, result)
    call(command, shell=True)


def copy_file(file1, file2, dir):
    file1 = dir.joinpath(file1)
    file2 = dir.joinpath(file2)
    file1.rename(file2)


def delete_directory(dir):
    if dir.exists() and dir.is_dir():
        shutil.rmtree(str(dir))


COLOR_NONE = "\033[93m"
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"

TYPE_ALERT = "[ALERT]"
TYPE_INFO = "[INFO] "


def printInfo(*args):
    _print(*args, type=TYPE_INFO)


def printAlert(*args):
    _print(*args, type=TYPE_ALERT, color=COLOR_RED)


def printSuccess(*args):
    _print(*args, type=TYPE_INFO, color=COLOR_GREEN)


def _print(*args, color=COLOR_NONE, type=""):
    text = ' '.join(args)
    print("{color}{type} {text}\033[00m".format(
        type=type, color=color, text=text))

def clean_dir(path):
    if not path.is_dir():
        path = path.parent
    delete_directory(path)
    path.mkdir(exist_ok=True, parents=True)
    