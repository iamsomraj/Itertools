import itertools

# count is a function for counting - starting from 0
# it returns an iterator
# it has two arguments such as start ( first element ) and step ( difference )

print("\nitertools.count() is checked using the next method 2 times : \n")
counter = itertools.count() # by default , start is 0 and step is 1
print(next(counter))
print(next(counter))

# it can also be used for indexing a list for the values
# here a value of list is indexed with the help of itertools.count and zip
# zip clubs consecutive elements of its arguement into a tuple
# as zip returns an iterator , therefore we have to convert it to list


print("\n\nReal life example of count is - List Indexing \n")

numbers = [100, 200, 300, 400]
print("List is - ")
print("\n{}\n".format(numbers))
real_data = zip(itertools.count(),numbers)
real_data = list(real_data)
print("\nResult after zipping - \n")
print(real_data)
