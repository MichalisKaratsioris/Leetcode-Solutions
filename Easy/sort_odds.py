

def sortOdds(nums: list) -> list:
    odds = sorted([num for num in nums if num % 2 == 1])
    return [num if num % 2 == 0 else odds.pop(0) for num in nums]


arr = [7, 1]
print(sortOdds(arr))
# Answer: [1, 7]

arr = [5, 8, 6, 3, 4]
print(sortOdds(arr))
# Answer: [3, 8, 6, 5, 4]

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sortOdds(arr))
# Answer: [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
