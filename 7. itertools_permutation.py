# permutation is a selection of objects where the order does matter
# selecting numbers 1,2 and forming the values - 12 and 21
# here the order matters

from itertools import permutations

print("\nThe numbers are --\n")
numbers = [1, 2, 3, 4, 5]
numbers = list(map(str,numbers))
print(numbers)
per = permutations(numbers,3)
per = list(per)
print("\nThe 3 digit numbers without repeating that can be formed using 5 number are - \n")
for i in per:
  print("".join(list(i)))
