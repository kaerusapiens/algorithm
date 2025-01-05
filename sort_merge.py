from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1: #list が1になったらrecursive終了
        return numbers
    center = len(numbers) //2

    left = numbers[:center]
    right = numbers[center:]
    print(f"Before merge_sort(left): left={left}, right={right}")
    merge_sort(left)
    print(f"After merge_sort(left): left={left}, right={right}")
    print(f"numbers={numbers}")
    print()
    # 1st recursive [7, 2, 9]
        # left = [7], right = [2, 9]
        # merge_sort(left) -> skipped
        # merge_sort(right) -> [2,9] sorted.
        # left =[2], right[9]
        # 2,9 sorted.
    print(f"Before merge_sort(right): left={left}, right={right}")
    merge_sort(right)
    print(f"After merge_sort(right): left={left}, right={right}")
    print(f"numbers={numbers}")
    print()



    i = j = k = 0
    # i : left index
    # j : right index
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1



if __name__ == '__main__':
    import random
    #nums = [random.randint(0,1000) for _ in range(10)]
    nums = [5,4,1,8,7,3,2,9]
    print(nums)
    print(merge_sort(nums))
    