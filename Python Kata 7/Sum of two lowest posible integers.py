def sum_two_smallest_numbers(numbers):
    if len(numbers) <= 4 and type(numbers) != int:
        return "at least 4 NUMBERS are needed"
    else:
        sorted_list = sorted(numbers)
        sum = int(sorted_list[0]) + int(sorted_list[1])
        return sum