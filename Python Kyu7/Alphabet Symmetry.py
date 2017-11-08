def solve(arr):
    alphabet = "abcdefghijklmnoprstuwxyz"
    numbers = [0]
    for i in range(len(arr)):
        if arr.index(i) == alphabet.index(i):
            numbers +=1

    return numbers

print(solve("aeiou"))