class Node:
    def __init__(self , data):
        self.data = data
        self.right = None
        self.left = None

    def inorder(self , array = []):
        if self.left: self.left.inorder()
        array.append(self.data)
        if self.right: self.right.inorder()
        return array

    def preorder(self , array = []):
        if self: array.append(self.data)
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()
        return array

    def postorder(self , array = []):
        if self.left: self.left.postorder()
        if self.right: self.right.postorder()
        array.append(self.data)
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


    print(root.inorder())
    print(root.preorder())
    print(root.postorder())
