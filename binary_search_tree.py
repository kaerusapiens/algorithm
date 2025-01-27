"""binary serach tree"""
class Node(object):
    
    def __init__(self,value:int) -> None:
        self.value = value
        self.left = None
        self.right = None
    
def insert(node:Node,value:int)-> Node:
    if node is None:
        return Node(value) #root value

    if value < node.value:
        node.left = insert(node.left,value)
    else:
        node.right = insert(node.right,value)
    return node

# 중위 순회(inorder traversal)
# 전위순회(preorder traversal)
# 후위 순회(postorder traversal)
def inorder(node:Node) -> None:
    if node is not None:
        inorder(node.left) # 재귀적으로 왼쪽서브트리 순회
        print(node.value) # 현재노드 방문
        inorder(node.right) # 재귀적으로 오른쪽 서브트리 순회
    

def search(node:Node, value:int) -> bool:
    if node is None:
        return False
    
    if node.value == value:
        return True
    elif node.value > value:
        return search(node.left, value)
    elif node.value < value:
        return search(node.right, value)


if __name__ == '__main__':
    root = None
    root = insert(root,3)
    root = insert(root,6)
    root = insert(root,5)
    root = insert(root,7)
    root = insert(root,1)    
    root = insert(root,10)  
    root = insert(root,2)  
    # print(root.value)
    # print(root.right.value)
    # print(root.right.left.value)

    #inorder(root)
    print(serach(root,3))