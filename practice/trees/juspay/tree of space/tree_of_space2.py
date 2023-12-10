class TreeNode:
    def __init__(self, node_id, parent=None):
        self.node_id = node_id
        self.locked = False
        self.locked_by = None
        self.children = []
        self.parent = parent


class LockableTree:
    def __init__(self):
        self.node_map = {}

    def lock(self, node_id, user_id):
        node = self.find_node(node_id)
        if (
            not node
            or node.locked
            or self.is_locked_ancestor(node)
            or self.is_locked_descendant(node)
        ):
            return False
        self.lock_node(node, user_id)
        return True

    def unlock(self, node_id, user_id):
        node = self.find_node(node_id)
        if not node or not node.locked or node.locked_by != user_id:
            return False
        self.unlock_node(node)
        return True

    def upgrade(self, node_id, user_id):
        node = self.find_node(node_id)
        if (
            not node
            or node.locked
            or self.is_locked_ancestor(node)
            or not self.has_locked_descendants(node)
        ):
            return False
        self.unlock_descendants(node)
        self.lock_node(node, user_id)
        return True

    def get_parent(self, node):
        return node.parent

    def find_node(self, node_id):
        return self.node_map.get(node_id)

    def is_locked_ancestor(self, node):
        while node:
            if node.locked:
                return True
            node = node.parent
        return False

    def is_locked_descendant(self, node):
        if node.locked:
            return True
        return any(self.is_locked_descendant(child) for child in node.children)

    def has_locked_descendants(self, node):
        return any(self.is_locked_descendant(child) for child in node.children)

    def unlock_descendants(self, node):
        for child in node.children:
            self.unlock_node(child)
            self.unlock_descendants(child)

    def lock_node(self, node, user_id):
        node.locked = True
        node.locked_by = user_id

    def unlock_node(self, node):
        node.locked = False
        node.locked_by = None


# Example usage:

# Create a lockable tree
tree = LockableTree()

# Create nodes and add them to the tree
node1 = TreeNode(1)
node2 = TreeNode(2, parent=node1)
node3 = TreeNode(3, parent=node1)
node4 = TreeNode(4, parent=node2)
node5 = TreeNode(5, parent=node2)
node6 = TreeNode(6, parent=node3)

tree.node_map = {1: node1, 2: node2, 3: node3, 4: node4, 5: node5, 6: node6}

# Lock a node
print(tree.lock(4, "user1"))  # True

# Attempt to lock a node with locked descendants
print(tree.lock(1, "user2"))  # False

# Unlock a node
print(tree.unlock(4, "user1"))  # True

# Upgrade a node
print(tree.upgrade(2, "user2"))  # False
print(tree.lock(5, "user2"))  # True
print(tree.upgrade(2, "user2"))  # True
