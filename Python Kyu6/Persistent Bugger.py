def persistence(n):

    counter = 0
    while len(str(n)) != 1:
        total = 1
        for number in str(n):
            total *= int(number)

        n = total
        counter +=1


    return counter


print(persistence(25))