from typing import List

def insertion_sort(numbers:List[int]) -> List[int]:
    print(numbers)
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i] #比較対象の値を臨時保存
        j = i - 1 #前の数値がより大きいかを検証
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
            print(numbers)
        
        numbers[j+1] = temp
        print(numbers)
        print()
    print(numbers)


if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    insertion_sort(nums)

