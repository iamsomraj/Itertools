# takewhile takes the list untill it encounters a false


from itertools import takewhile
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
print("\n\nThe list is - \n")
print(numbers)


def lessThan5(number):
    if number < 5:
        return True
    return False


print("\n\nThe values that are taken are -\n")
taken = list(takewhile(lessThan5, numbers))
print(taken)
