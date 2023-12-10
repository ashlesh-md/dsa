import math
import threading


class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.descendantLock = 0
        self.lock = threading.Lock()  # Add a lock for each node


class Tree:
    def __init__(self, n, m, node_lst, queries):
        self.node_lst = []
        self.node_map = {}
        self.tree_lock = threading.Lock()  # Add a lock for the entire tree

        for node in node_lst:
            converted = Node(node)
            self.node_lst.append(converted)
            self.node_map[node] = converted

        for i in range(int(n / m)):
            start = i * m + 1
            end = i * m + m
            if end > n - 1:
                end -= end % (n - 1)
            if end < n:
                self.node_lst[i].children = self.node_lst[start : end + 1]

        for i in range(1, n):
            self.node_lst[i].parent = self.node_lst[math.ceil(i / m) - 1]

        self.root = self.node_lst[0]
        self.processed_queries = [query.split() for query in queries]

    def lock_node(self, node, uid):
        with node.lock:
            return self._lock(node, uid)

    def unlock_node(self, node, uid):
        with node.lock:
            return self._unlock(node, uid)

    def upgrade_node(self, node, uid):
        with node.lock:
            return self._upgrade(node, uid)

    def lock(self, node, uid):
        with self.tree_lock:
            return self.lock_node(node, uid)

    def unlock(self, node, uid):
        with self.tree_lock:
            return self.unlock_node(node, uid)

    def upgrade(self, node, uid):
        with self.tree_lock:
            return self.upgrade_node(node, uid)

    def _lock(self, node, uid):
        if (
            node.descendantLock > 0
            or node.isLocked
            or self.isAncestor_locked(node.parent)
        ):
            return False

        node.uid = uid
        node.isLocked = True
        parent_node = node.parent

        while parent_node:
            parent_node.descendantLock += 1
            parent_node = parent_node.parent
        return True

    def _unlock(self, node, uid):
        if uid != node.uid or not node.isLocked:
            return False

        node.isLocked = False
        node.uid = None
        parent_node = node.parent

        while parent_node:
            parent_node.descendantLock -= 1
            parent_node = parent_node.parent
        return True

    def _upgrade(self, node, uid):
        if node.descendantLock == 0 or self.isAncestor_locked(node.parent):
            return False

        self._unlock_children(node, uid)
        self._lock(node, uid)

        return True

    def isAncestor_locked(self, node):
        while node:
            if node.isLocked:
                return True
            node = node.parent
        return False

    def _unlock_children(self, node, uid):
        for child in node.children:
            self._unlock(child, uid)
            self._unlock_children(child, uid)

    def __print_tree(self, node, out):
        out += (
            node.val
            + " No of Descendants Locked: "
            + str(node.descendantLock)
            + " is Node Locked: "
            + str(node.isLocked)
            + ",\n"
        )
        for child in node.children:
            out = self.__print_tree(child, out)
        return out

    def __str__(self):
        with self.tree_lock:
            return self.__print_tree(self.root, "")


# Test cases
queries = [
    "1 China 9",  # Lock China with UID 9
    "1 India 9",  # Lock India with UID 9
    "3 Asia 9",  # Upgrade lock on Asia with UID 9
    "2 India 9",  # Unlock India with UID 9
    "2 Asia 9",  # Unlock Asia with UID 9
    "3 SouthAfrica 9",  # Attempt upgrade on SouthAfrica with UID 9 (should fail, no descendants locked)
]

# Expected output
# Locking China with UID 9 should succeed.
# Locking India with UID 9 should succeed.
# Upgrading lock on Asia with UID 9 should succeed.
# Unlocking India with UID 9 should succeed.
# Unlocking Asia with UID 9 should fail (descendant SouthAfrica is locked).
# Attempting to upgrade SouthAfrica with UID 9 should fail (no descendants locked).
expected_output = [True, True, True, True, False, False]

# Example usage
n = 7
m = 2
nodes = ["World", "Asia", "Africa", "China", "India", "SouthAfrica", "Egypt"]
obj = Tree(n, m, nodes, queries)

# Process queries and store results in 'res'
res = []
for query in obj.processed_queries:
    if query[0] == "1":
        res.append(obj.lock(obj.node_map[query[1]], query[2]))
    elif query[0] == "2":
        res.append(obj.unlock(obj.node_map[query[1]], query[2]))
    elif query[0] == "3":
        res.append(obj.upgrade(obj.node_map[query[1]], query[2]))

# Print the tree structure
print(str(obj))

# Print the results and compare with expected output
print("Actual Output:", res)
print("Expected Output:", expected_output)
