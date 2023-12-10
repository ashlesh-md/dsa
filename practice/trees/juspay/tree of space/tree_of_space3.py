class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.is_locked = False
        self.locked_by = None


class LockableTree:
    def __init__(self, nodes):
        self.node_map = {name: TreeNode(name) for name in nodes}

    def add_edge(self, parent_name, child_name):
        parent = self.node_map[parent_name]
        child = self.node_map[child_name]
        parent.children.append(child)
        child.parent = parent

    def lock(self, node_name, user_id):
        node = self.node_map[node_name]
        if not self.is_valid_lock(node, user_id):
            return False

        node.is_locked = True
        node.locked_by = user_id
        return True

    def unlock(self, node_name, user_id):
        node = self.node_map[node_name]
        if not self.is_valid_unlock(node, user_id):
            return False

        node.is_locked = False
        node.locked_by = None
        return True

    def upgrade(self, node_name, user_id):
        node = self.node_map[node_name]
        if not self.is_valid_upgrade(node, user_id):
            return False

        # Unlock all descendants
        self.unlock_descendants(node)

        # Lock the current node
        node.is_locked = True
        node.locked_by = user_id
        return True

    def is_valid_lock(self, node, user_id):
        if self.is_descendant_locked(node) or self.is_ancestor_locked_by_different_user(
            node, user_id
        ):
            return False

        return True

    def is_valid_unlock(self, node, user_id):
        return node.is_locked and node.locked_by == user_id

    def is_valid_upgrade(self, node, user_id):
        if self.is_descendant_locked(node) or self.is_ancestor_locked_by_different_user(
            node, user_id
        ):
            return False

        return True

    def is_descendant_locked(self, node):
        return any(
            descendant.is_locked or self.is_descendant_locked(descendant)
            for descendant in node.children
        )

    def is_ancestor_locked_by_same_user(self, node, user_id):
        current = node.parent
        while current:
            if current.is_locked and current.locked_by == user_id:
                return True
            current = current.parent
        return False

    def is_ancestor_locked_by_different_user(self, node, user_id):
        current = node.parent
        while current:
            if current.is_locked and current.locked_by != user_id:
                return True
            current = current.parent
        return False

    def unlock_descendants(self, node):
        for descendant in node.children:
            self.unlock_descendants(descendant)
            descendant.is_locked = False
            descendant.locked_by = None


# Example Usage:
nodes = ["World", "Asia", "Africa", "China", "India", "SouthAfrica", "Egypt"]
queries = ["1 China 9", "1 India 9", "3 Asia 9", "2 India 9", "2 Asia 9"]

tree = LockableTree(nodes)
tree.add_edge("World", "Asia")
tree.add_edge("World", "Africa")
tree.add_edge("Asia", "China")
tree.add_edge("Asia", "India")
tree.add_edge("Africa", "SouthAfrica")
tree.add_edge("Africa", "Egypt")

results = []
for query in queries:
    operation, node_name, user_id = query.split()
    if operation == "1":
        results.append(tree.lock(node_name, user_id))
    elif operation == "2":
        results.append(tree.unlock(node_name, user_id))
    elif operation == "3":
        results.append(tree.upgrade(node_name, user_id))

print(results)  # Output: [True, True, True, False, True]
