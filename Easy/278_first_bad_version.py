"""
Leetcode #278 Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad. You are given an API bool isBadVersion(version) which returns whether
version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""


def isBadVersion(n: int, bad: int) -> bool:
    if n == bad:
        return True
    return False


def first_bad_version(n: int, bad: int) -> int:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    fi = 0
    li = n
    while fi + 1 < li:
        median = (fi + li) // 2
        if isBadVersion(median, bad):
            li = median
        else:
            fi = median
    return fi + 1


# ----------------- TESTS -----------------

n_1 = 5
bad_1 = 4
print(first_bad_version(n_1, bad_1))
# Expected Output: 4

n_2 = 1
bad_2 = 1
print(first_bad_version(n_2, bad_2))
# Expected Output: 1
