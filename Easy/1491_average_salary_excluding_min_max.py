"""
Leetcode #1491 - Easy

You are given an array of unique integers salary where salary[i] is the salary of the ith employee. Return the average
salary of employees excluding the minimum and maximum salary. Answers within 10**(-5) of the actual answer will be
accepted.

Constraints:
    3 <= salary.length <= 100
    1000 <= salary[i] <= 106
    All the integers of salary are unique.
"""


def average_salary_excluding_min_max(arr: list) -> float:
    """
    This function calculates the sum of all the salaries except for the minimum and maximum salary using a slice of
    the list. Finally, it returns the average salary by dividing the total by the number of salaries.

    :param arr:
    :return:

    Example:
        (1) arr [50000, 45000, 40000, 35000]
            average_salary_excluding_min_max(arr, 5) => 42500.00000

    # Spacetime Complexity:     O(1)/O(n), where n is the size of the array.
    Spacetime Complexity:     O(1)
    """
    # First solution with O(n) time complexity
    # total = 0
    # for number in arr:
    #     if number != max(arr) and number != min(arr):
    #         total = total + number
    # # return total/(len(arr) - 2)
    # return "{0:.5f}".format(total/(len(arr) - 2))
    min_salary = min(arr)
    max_salary = max(arr)
    total_salary = sum(arr)
    return (total_salary - min_salary - max_salary) / (len(arr) - 2)


# ----------------- TESTS -----------------

arr = [4000, 3000, 1000, 2000]
print(average_salary_excluding_min_max(arr))
# Expected Output: 2500.00000

arr = [1000, 2000, 3000]
print(average_salary_excluding_min_max(arr))
# Expected Output: 2000.00000
