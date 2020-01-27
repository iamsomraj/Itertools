# islice is used to slice from an iterator
# the arguements are iterator, start index, end index ( included ) , step
# if there are only two arguements as iterator and index
# then it will slice from 0 to index(included)


from itertools import islice
print("\nThe number list is - \n")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers)
print("\n\nSliced numbers, 5 --\n\n")
sliced = islice(numbers, 5)
print(list(sliced))
print("\nSliced numbers, start 1 , end 7, step 1 --\n\n")
sliced = islice(numbers, 1 , 7, 1)
print(list(sliced))
