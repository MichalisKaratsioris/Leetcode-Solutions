

def vowelCount(s: str) -> int:
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in s:
        if c in vowels:
            count += 1
    return count


s1 = "michalis"
print(vowelCount(s1))
# Answer: 3
