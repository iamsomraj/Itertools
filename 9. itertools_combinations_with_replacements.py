# in case of permutation and combination, the repeat is not allowed
# but when the repeat is required
# and the order does not matter ,
# then we can use itertools.combinations_with_replacement
from itertools import combinations_with_replacement

numbers = [1, 2, 3, 4, 5, 6]
numbers = list(map(str,numbers))
print("\nThe list of numbers are - \n")
print("\n{}\n".format(numbers))
print("\n\nThe combinations where elements are repeated and\nalso the order does not matter is - \n")
comb = combinations_with_replacement(numbers,3)
for num in comb:
  num = "".join(num)
  print(num)