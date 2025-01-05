from typing import List, NewType

IndexNum = NewType('IndexNum', int)
#返却値のintをわかりやすくするため



def linear_search(numbers:List[int], target:int) -> IndexNum:
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1 #見つからなかった場合
        

if __name__ == '__main__':
    nums = [0,1,5,7,9,11]
    result = linear_search(nums, 7)
    print(result)