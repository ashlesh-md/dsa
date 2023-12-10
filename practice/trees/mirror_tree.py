from collections import deque
class Node:
    def __init__(self , data):
        self.data = data
        self.right = None
        self.left = None

    def inorder(self, array = None):
        if array is None:
            array = []
        if self.left:
            self.left.inorder(array)
        array.append(self.data)
        if self.right:
            self.right.inorder(array)
        return array


    def mirror(self):
        if self:
            self.left , self.right = self.right , self.left
        if self.left : self.left.mirror()
        if self.right: self.right.mirror()

    def mirror_bfs(self):
        _deque = deque()
        _deque.append(self)

        while _deque:
            data = _deque.popleft()
            if data:
                data.left , data.right = data.right , data.left
            if data.left :
                _deque.append(data.left)
            if data.right :
                _deque.append(data.right)


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right.left = Node(25)
    root.right.right = Node(40)

    #       20
    #      /  \
    #     10   30
    #    / \   / \
    #   5  15 25  40


    print(root.inorder())
    root.mirror()
    print(root.inorder())
    root.mirror()
    print(root.inorder())
    root.mirror_bfs()
    print(root.inorder())
    root.mirror_bfs()
    print(root.inorder())
