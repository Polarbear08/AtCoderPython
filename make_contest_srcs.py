"""
Make source files for a contest
"""


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
    try:
        for ord_file in range(num_problem):
            pass


    except:
        pass


    return 0