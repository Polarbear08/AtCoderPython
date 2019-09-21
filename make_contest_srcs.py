"""
Make source files for a contest
"""
import os

def make_srcs(contest_name: str, num_problem: int) -> int:
    """
    Create contest source files into the designated directory
    :param contest_name:
        target contest name
    :param num_problem:
        the number of the problems in the constest
    :return:
        exit status
        0: successfully finished
        1: some files were already existed
    """
    A_ORD = ord("A")
    Z_ORD = ord("Z")
    ALPHABETS = [chr(i) for i in range(A_ORD, Z_ORD + 1)]

    # create files
    # raise Exception if a folder or file already exist

    # TODO: add try-except
    base_filepath = "./contests/"
    for problem in range(num_problem):
        filepath = build_filepath(base_filepath, contest_name, ALPHABETS[problem])
        os.makedirs(filepath)

    return 0


def build_filepath(base_filepath: str, contest_name: str, problem_char: str) -> str:
    """
    Build the path of a source file
    :param base_filepath:
    :param contest_name:
    :param problem_char:
    :return:
        source file path
    """
    return base_filepath + contest_name + "/" + problem_char + "01.py"
