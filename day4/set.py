# Sets are mutable, unordered and doesn't allow duplicates...

# Last-In-First-Out Data Model

sample_set = {1, 2, 3, 4, 5}

sample_set.add(6)  # Adds a single value to the set
sample_set.update([1, 2, 9, 10, 11])  # Adds a grouped data into the set


sample_set.pop()
sample_set.pop()

sample_set.clear()

print(sample_set)


if 9 in sample_set:
    print(True)


sample_list = list(sample_set)  # Converting one grouped data type into another
