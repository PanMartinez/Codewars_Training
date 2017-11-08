def getCount(str):
    num_vowels = 0
    for w in str:
        if w in "aeiouAEIOU":
            num_vowels += 1

    return num_vowels

str = "andrzejeioustrzelbczynski"

print(getCount(str))

#     return sum(1 for let in inputStr if let in "aeiouAEIOU")