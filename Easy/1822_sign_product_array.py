"""
Leetcode #1822 - Easy

There is a function signFunc(x) that returns:
    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.

You are given an integer array. Let product be the product of all values in the array nums. Return signFunc(product).


"""


def sign_product_array(arr: list) -> int:
    """
    This function takes a list of integers as input and returns 1 if the product of all the numbers in the
    list is positive, -1 if the product is negative, and 0 if the product is 0.

    :param arr:
    :return:

    Example:
        (1) arr = [1, 2, 3]
            sign_product_array(arr) => 1
        (1) arr = [-1, 2, 3]
            sign_product_array(arr) => -1

    Spacetime Complexity:     O(1)/O(n), where n is the size of the array
    """
    product = 1
    for num in arr:
        product *= num
    if product > 0:
        return 1
    elif product < 0:
        return -1
    else:
        return 0


# ----------------- TESTS -----------------

arr = [-1, -2, -3, -4, 3, 2, 1]
print(sign_product_array(arr))
# Expected Output: 1

arr = [1, 5, 0, 2, -3]
print(sign_product_array(arr))
# Expected Output: 0

arr = [-1, 1, -1, 1, -1]
print(sign_product_array(arr))
# Expected Output: -1
