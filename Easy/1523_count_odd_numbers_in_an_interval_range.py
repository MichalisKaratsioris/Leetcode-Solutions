"""
Leetcode #1523 - Easy

Given two non-negative integers "low" and "high", return the count of odd
numbers between low and high (inclusive).

Constraints:
    0 <= low <= high <= 10^9
"""


def count_odds_in_interval(low: int, high: int) -> int:
    """
    This function takes two non-negative integers "low" and "high" as input and returns the count of odd
    numbers between "low" and "high" (inclusive).

    :param arr:
    :return:

    Example:
        (1)

    Spacetime Complexity:     O(1)
    """
    # if low % 2 == 0 and high % 2 == 0:
    #     return (high - low) // 2
    # else:
    #     return 1 + (high - low) // 2
    return (high - low + 1) // 2 + (low % 2)


# ----------------- TESTS -----------------

l = 3
h = 7
print(count_odds_in_interval(l, h))
# Expected Output: 3

l = 8
h = 10
print(count_odds_in_interval(l, h))
# Expected Output: 1

l = 800445804
h = 979430543
print(count_odds_in_interval(l, h))
# Expected Output: 89492370
