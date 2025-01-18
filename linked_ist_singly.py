from __future__ import annotations
from typing import Any



class Node(object):
    def __init__(self,data:Any,next_node :Node = None): # next_Node는 다음 클래스 node를 불러옴
        self.data = data
        self.next = next_node



class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, data:Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data:Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data:Any) -> None:
        current_node = self.head 
        if current_node and current_node.data == data: #先頭のものが存在する場合
            self.head = current_node.next #削除
            current_node = None
            return
        
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node #headから探しにいく
            current_node = current_node.next
        
        if current_node is None: #最後まで行ったが、削除するものはなかった
            return
        
        previous_node.next = current_node.next # current_node.data == dataだった
        current_node = None


    def reverse_recursivce(self) -> None: #1 -> 2 -> 3 -> None
        def _reverse_recursive(current_node:Node, previous_node:Node) -> Node:
            if not current_node:
                return previous_node
            
            next_node = current_node.next  # current_node = 1, next_node = 2
            current_node.next = previous_node # 1의 화살표를 None으로 바꿈
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)

        self.head = _reverse_recursive(self.head, None)



    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next



if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()
    l.reverse_recursivce()
    l.print()