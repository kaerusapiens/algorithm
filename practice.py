#python timsort algorithm
numbers = [5, 3, 8, 6]

numbers.sort()  # In-place sorting
print(numbers)  # Output: [3, 5, 6, 8]


sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(sorted_numbers)  # Output: [3, 5, 6, 8]


#numpy default sort algorithm is quicksort
#but optaionally, can use mergesort,heapsort, stable
# Quicksort (default): Fast but not stable.
# Mergesort: Stable and efficient for large datasets.
# Heapsort: Memory-efficient but slower than quicksort.
# Stable: Guarantees stability for equal elements.
import numpy as np

arr = np.array([5, 2, 9, 1, 5, 6])
sorted_arr = np.sort(arr)
#sorted_arr = np.sort(arr, kind='mergesort')

print( sorted_arr)