"""
Leetcode #1281 - Easy

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Constraints:
    1 <= n <= 10^5
"""


def subtract_product_sum_digits_integer(n: int) -> int:
    """
    This function takes an integer as input and returns the difference between the product of its digits and
    the sum of its digits. For example, if the input is 12345, the function will first compute the sum of its
    digits, which is 1 + 2 + 3 + 4 + 5 = 15, and then compute the product of its digits, which is
    1 * 2 * 3 * 4 * 5 = 120. Finally, the function will return the difference between the product and the sum,
    which is 120 - 15 = 105.

    :param arr:
    :return:

    Spacetime Complexity:     O(n), where n is the number of digits in the input integer.
    """

    n_str = str(n)
    s = 0
    p = 1
    for digit in n_str:
        s = s + int(digit)
        p = p * int(digit)
    return p - s


# ----------------- TESTS -----------------

n = 234
print(subtract_product_sum_digits_integer(n))
# Expected Output: 15

n = 4421
print(subtract_product_sum_digits_integer(n))
# Expected Output: 21

n = 123
print(subtract_product_sum_digits_integer(n))
# Expected Output: 0
