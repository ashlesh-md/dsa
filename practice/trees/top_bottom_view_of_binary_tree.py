from collections import deque
class Node:
    def __init__(self , data):
        self.data = data
        self.right = None
        self.left = None

    def rightview(self , res = [] , level = 0):
        if self and len(res) == level:
            res.append(self.data)

        if self.right: self.right.rightview(level = level + 1)

        if self.left: self.left.rightview(level = level + 1)

        return res

    def rightview_level_order(self):
        _deque = deque()
        _deque.append((self , 0))
        sol = []
        while _deque:
            node , level = _deque.popleft()
            if node:
                if level == len(sol):
                    sol.append(node.data)

                if node.right:
                    _deque.append((node.right , level + 1))

                if node.left:
                    _deque.append((node.left , level + 1))

        return sol

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


    print(root.rightview())
    print(root.rightview_level_order())
