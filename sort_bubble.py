from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):

        #数字が6個だから　indexは0~5。 -1をすることで全てが参照できる。
        #-iをすることで、 limitを1個ずつさげる。
        for j in range(len_numbers-i-1):
            if numbers[j] >numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        print(numbers)
        print()
    print("--------------------")
    return numbers



if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    #nums = [2,5,1,8,7,3]
    print(bubble_sort(nums))
    