# filterfalse just works opposite the filter method
# it takes the first arguement as function
# the second arg is iterator
# it returns the new iterator containing the false values


from itertools import filterfalse

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n\nThe list is - \n")
print(numbers)
def lessThanFive(number):
  if number < 5:
    return True
  return False
filteredValues = list(filterfalse(lessThanFive, numbers))
print("\n\nThe filtered values are - \n")
print(filteredValues)
