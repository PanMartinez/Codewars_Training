from collections import Counter

def duplicate_count(text):
    dubles = 0
    for key,value in Counter(list(text.upper())).items():
        if value > 1:
           dubles += 1
    return dubles



print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdea"), 1)
print(duplicate_count("indivisibility"), 1)
