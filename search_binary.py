from typing import List, NewType

IndexNum = NewType('IndexNum', int)
#返却値のintをわかりやすくするため



def linear_search(numbers:List[int], target:int) -> IndexNum:
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1 #見つからなかった場合

#whileで使用する場合
# def binary_serach(numbers:List[int],value:int) -> IndexNum:
#     left,right = 0, len(numbers)-1
#     while left <= right:
#         mid = (left + right) //2
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# recursiveで使用
def binary_serach(numbers:List[int],value:int) -> IndexNum:
    def _binary_serach(numbers:List[int],value:int,left:IndexNum,right:IndexNum)-> IndexNum:
        if left > right:
            return -1
        mid = (left + right) //2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_serach(numbers,value,mid+1,right)
        else:
            return _binary_serach(numbers,value,left,mid-1)
    return _binary_serach(numbers,value,0,len(numbers)-1)





if __name__ == '__main__':
    nums = [0,1,5,7,9,11]
    result = linear_search(nums, 7)
    print(result)
    result = binary_serach(nums, 7)
    print(result)