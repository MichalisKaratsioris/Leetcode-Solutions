"""
NOTE:
    16-bits ~ [-215, 215 – 1] = [-32,768, 32,767]
    32-bits ~ [-231, 231 – 1] = [-2,147,483,648, 2,147,483,647]
    64-bits ~ [-263, 263 – 1] = [-9,223,372,036,854,775,808, 9,223,372,036,854,775,807]

Leetcode #191 - Easy

Write a function that takes an unsigned integer and returns the number of '1' bits it has
(also known as the Hamming weight).

Constraints:
    The input must be a binary string of length 32.
"""


def number_one_bits(n: int) -> int:
    """
    This function works by using a bitwise AND operation to check if the rightmost bit of n is 1.
    If it is, it increments the count. It then right shifts n by 1 bit and repeats the process
    until n becomes 0. The time complexity of this function is O(n), where n is the number of bits
    in the integer.

    :param arr:
    :return:

    Example:
        (1)

    Spacetime Complexity:       O(n)
    # Spacetime Complexity:     O(1)/O(n)
    # Spacetime Complexity:     O(n)
    """
    # First solution with spacetime complexity O(n)
    b = f'{n:32b}'
    count = 0
    for digit in b:
        if digit == '1':
            count = count + 1
    return count

    # Second solution, using the >>= operator with spacetime complexity O(1)/O(n)
    # # Initialize the count to 0
    # count = 0
    # # Keep looping while n is greater than 0
    # while n > 0:
    #     # If the rightmost bit of n is 1, increment the count
    #     count += n & 1
    #     # Right shift n by 1 bit
    #     n >>= 1
    # # Return the count
    # return count

    # Third solution, using built-in functions, with spacetime complexity O(n).
    # return bin(n).count('1')

# ----------------- TESTS -----------------

s = 11
print(number_one_bits(s))
# Expected Output: 3

s = 128
print(number_one_bits(s))
# Expected Output: 1

s = 4294967293
print(number_one_bits(s))
# Expected Output: 31

s = 4294967295
print(number_one_bits(s))
# Expected Output: 32
