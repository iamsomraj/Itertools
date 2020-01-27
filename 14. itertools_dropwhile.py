# dropwhile traverses through the iterator
# until it finds a false value
# the moment he finds the false value
# it returns the rest of the list 
# it drops the list and does not traverse

from itertools import dropwhile

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
print("\n\nThe list is - \n")
print(numbers)


def lessThanFive(number):
    if number < 5:
        return True
    return False


dropped = list(dropwhile(lessThanFive, numbers))
print("\n\nThe dropped values are \n\n")
print(dropped)
