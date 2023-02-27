

def sumOfMultiples(n: int, m: int, k: int) -> int:
    sum = 0
    if k <= min(n, m):
        return 0
    for num in range(min(n, m), k):
        if num % n == 0 or num % m == 0:
            sum += num
    return sum


n1 = 3
m1 = 5
k1 = 10
print(sumOfMultiples(n1, m1, k1))
# Answer: 23

n1 = 3
m1 = 5
k1 = 20
print(sumOfMultiples(n1, m1, k1))
# Answer: 88
