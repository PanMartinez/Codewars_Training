import re
def solve(s):
    numbers = re.findall('\d+', s)
    max_value = max([int(i) for i in numbers])
    return max_value

print(solve('vih61w8oohj5'))