from typing import List

def insertion_sort(numbers:List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        