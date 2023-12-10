from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def bfs(self, array=[]):
        _deque = deque()
        _deque.append(self)

        while _deque:
            data = _deque.popleft()
            if data:
                array.append(data.data)
            if data.left:
                _deque.append(data.left)
            if data.right:
                _deque.append(data.right)
        return array


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

    print(root.bfs())
