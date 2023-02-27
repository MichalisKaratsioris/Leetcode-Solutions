"""
Leetcode #496 - Easy

The next greater element of some element x in an array is the first greater element that is to the right of x
in the same array. You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset
of nums2. For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next
greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""


def next_greater_element(arr1: list, arr2: list) -> list:
    """
    This function takes as an input
    and returns

    Example:
        (1)

    Spacetime Complexity:     O(1)/O(m), where m is the size of nums1
    """
    result = []
    for n in arr1:
        for m in arr2:
            if n == m:
                for k in arr2[arr2.index(m)+1:]:
                    if m < k:
                        result.append(k)

                    else:
                        result.append(-1)
                    break
    return result


# ----------------- TESTS -----------------

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_element(nums1, nums2))
# Expected Output: [-1, 3, -1]

nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(next_greater_element(nums1, nums2))
# Expected Output: [3, -1]
