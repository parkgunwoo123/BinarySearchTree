class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySortTree():
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, value):
        currentNode = self.root # insert는 root에서 부터 탐색
        while True:
            if value < currentNode.value: # 현재 탐색 노드의 값이 삽입할 값보다 크다면 
                if currentNode.left is not None: # 왼쪽 자식 노드가 있을 때
                    currentNode = currentNode.left # 왼쪽 자식 노드 탐색
                else:
                    currentNode.left = Node(value) # 자식 노드가 없을 시 삽입
                    break
            
            else:
                if currentNode.right is not None:
                    currentNode = currentNode.right
                else:
                    currentNode.right = Node(value)
                    break
    
    def search(self, value):
        currentNode = self.root  # search는 root 노드부터 탐색
        while currentNode:
            if currentNode.value == value:
                return True
            elif currentNode.value > value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False
    
    def delete(self, value):
        # 삭제의 case는 총 3가지
        # case1: leafnode를 삭제 시 그냥 삭제 가능
        # case2: 자식 노드가 하나인 노드는 삭제할 노드를 삭제 후, 자식 노드를 삭제한 노드의 부모노드랑 연결
        # case3: 자식 노드가 양쪽인 노드는 삭제할 노드보다 작은 값중에서 가장 큰 자식이나, 큰 값 중에서 가장 작은 자식과 위치를 바꾼 후 삭제한다.
        currentNode = self.root
        parentNode = self.root
        isSearch = False

        while currentNode:
            if currentNode.value == value:
                isSearch = True
                break
            elif currentNode.value > value:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                parentNode = currentNode
                currentNode = currentNode.right
        if isSearch:
            # case1
            if currentNode.left is None and currentNode.right is None:
                if parentNode.value > value:
                    parentNode.left = None
                else:
                    parentNode.right = None
            
            # case2중 right child node가 있을 때,
            elif currentNode.left is None and currentNode.right is not None:
                if parentNode.value > value:
                    parentNode.left = currentNode.right
                else:
                    parentNode.right = currentNode.right
          
            # case2중 left child node가 있을 때,
            elif currentNode.left is not None and currentNode.right is None:
                if parentNode.value > value:
                    parentNode.left = currentNode.left
                else:
                    parentNode.right = currentNode.left

            # case3
            elif currentNode.left is not None and currentNode.right is not None:
                changeNode = currentNode.left
                changeParentNode = currentNode.left
                while changeNode.right is not None:
                    changeParentNode = changeNode
                    changeNode = changeNode.right

                currentNode.value = changeNode.value
                if changeNode.left is not None:
                    changeParentNode.right = changeNode.left
                else:
                    changeParentNode.right = None 
        return isSearch
arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
root = 30
bst = BinarySortTree(root)
for i in arr:
    bst.insert(i)

print(bst.search(22)) 
print(bst.search(61)) 
print(bst.search(60)) 
print(bst.delete(60)) 
print(bst.search(60)) 
print(bst.delete(22)) 
print(bst.delete(44)) 
print(bst.search(22)) 
print(bst.search(44)) 
