# permutation and combination does not support the repeatation
# but when the repeat is needed and the order is required
# then we have to perform the cartesian product
# in the product function 
# we have to pass the iterator and the repeat arguement for the number

from itertools import product



print('\nThe list of numbers are - \n')
number = [1,2,3,4,5]
print(number)
number = list(map(str,number))
prod = product(number,repeat=3)
print("\nRepeat is there  + Order is maintained as it matters\n")
print("\n\nThe product is defined -\n")
prod = list(prod)
for number in prod:
  number = ''.join(number)
  print(number)