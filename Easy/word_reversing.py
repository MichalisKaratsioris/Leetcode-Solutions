

def wordReversing(s: str) -> str:
    if len(s) <= 4:
        return "boooo"
    words = s.split(" ")
    for word in words:
        if len(word) >= 5:
            # word_list = list(word)
            word_list = [ch for ch in word]
            word_list_rev = reversed(word_list)
            word_rev = "".join(word_list_rev)
            words[words.index(word)] = word_rev
    return " ".join(words)


print(wordReversing("Michalis Kara"))
