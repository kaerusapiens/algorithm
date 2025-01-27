import sys
from typing import Optional


class MiniHeap(object):

    def __init__(self) -> None:
        self.heap = [-1 * sys.maxsize] # # 1-based 인덱스를 위한 초기값. 실제 힙 데이터는 self.heap[1:]에 저장됩니다.
        self.current_size = 0 # 힙에 저장된 요소의 개수

    def parent_index(self, index: int) -> int:
        return index // 2

    def left_child_index(self, index: int) -> int:
        return 2 * index

    def right_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0: #루트 노드까지 반복합니다.
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    # insert 
    def push(self, value: int) -> None:
        self.heap.append(value) #값을 리스트의 끝에 추가.
        self.current_size += 1
        self.heapify_up(self.current_size)

    def min_child_index(self, index: int) -> int:
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if (self.heap[self.left_child_index(index)] <
                self.heap[self.right_child_index(index)]):
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) <= self.current_size:
            min_child_index = self.min_child_index(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.swap(index, min_child_index)
            index = min_child_index

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return

        root = self.heap[1]
        data = self.heap.pop() #힙에서 최소값(루트 노드)을 제거하고 반환합니다.
        if len(self.heap) == 1:
            return root

        # [-x, 5, 6, 2, 9, 13, 11]
        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)
        return root




if __name__ == '__main__':
    min_heap = MiniHeap()
    min_heap.push(5)
    min_heap.push(6)
    min_heap.push(2)
    min_heap.push(9)
    min_heap.push(13)
    min_heap.push(11)
    min_heap.push(1)
    print(min_heap.heap)
    print(min_heap.pop())
    print(min_heap.heap)
