class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kth_smallest_element(root, k, count=[0]):
    print(count)
    if not root:
        return -1

    if root.left: 
        count[0] += 1
        kth_smallest_element(root.left, k, count)

        
    if count[0] == k:
        return root.data
    
    if root.right: 
        kth_smallest_element(root.right, k, count)


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    root.left.right = Node(2)

    #   3
    #  / \
    # 1   4
    #  \
    #   2

    print(kth_smallest_element(root, 1))
    print(kth_smallest_element(root, 2))
    print(kth_smallest_element(root, 3))
    print(kth_smallest_element(root, 4))
    print(kth_smallest_element(root, 5))
