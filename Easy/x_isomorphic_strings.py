"""
Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in
s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving
the order of characters. No two characters may map to the same character, but a character may map to itself.
"""


def isomorphic_strings(s: str, t: str) -> bool:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    if len(s) != len(t):
        return False
    set_all = set([s[i] + t[i] for i in range(len(s))])
    st = set(s)
    tt = set(t)
    if 2 * len(set_all) == len(st) + len(tt):
        return True
    return False


# ----------------- TESTS -----------------

s_1 = 'egg'
t_1 = 'add'
print(isomorphic_strings(s_1, t_1))
# Expected Output: True

s_2 = 'foo'
t_2 = 'bar'
print(isomorphic_strings(s_2, t_2))
# Expected Output: False

s_3 = 'paper'
t_3 = 'title'
print(isomorphic_strings(s_3, t_3))
# Expected Output: True
