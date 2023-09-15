from collections import deque
class Node:
    def __init__(self , data):
        self.data = data
        self.right = None
        self.left = None

    def topview(self , res = {} , level = 0):
        if self.data:
            if level in res:
                res[level].append(self.data)
            else:
                res[level] = [self.data]

        if self.right: self.right.topview(level = level + 1)

        if self.left: self.left.topview(level = level - 1)


        return [res[key][0] for key in sorted(res.keys())]


    def bottomview(self , res = {} , level = 0):
        if self.left: self.left.bottomview(level = level - 1)
        if self.data:
            if level in res:
                res[level].append(self.data)
            else:
                res[level] = [self.data]
        if self.right: self.right.bottomview(level = level + 1)

        return [res[key][-1] for key in res.keys()]


    def topview_by_levelorder(self , res = {}):
        _deque = deque()
        _deque.append((self , 0))
        level = 0
        while _deque:
            node , level = _deque.popleft()
            if node:
                if level in res:
                    res[level].append(node.data)
                else:
                    res[level] = [node.data]
            if node.left:
                 _deque.append((node.left , level - 1))

            if node.right:
                 _deque.append((node.right , level + 1))

        return [res[key][0] for key in sorted(res.keys())]

    def bottomview_by_levelorder(self , res = {}):
        _deque = deque()
        _deque.append((self , 0))
        level = 0
        while _deque:
            node , level = _deque.popleft()
            if node:
                if level in res:
                    res[level].append(node.data)
                else:
                    res[level] = [node.data]
            if node.left:
                 _deque.append((node.left , level - 1))

            if node.right:
                 _deque.append((node.right , level + 1))

        return [res[key][-1] for key in sorted(res.keys())]



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


    print(root.topview())
    print(root.topview_by_levelorder())

    print(root.bottomview())
    print(root.bottomview_by_levelorder())
