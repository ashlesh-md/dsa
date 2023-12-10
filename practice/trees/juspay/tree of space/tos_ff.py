import math


class Node:
    def __init__(self, val):
        self.val = val
        self.uid = None
        self.parent = None
        self.children = []
        self.isLocked = False
        self.isDescendantLocked = 0


class Tree:
    def __init__(self, n, m, node_lst, queries):
        # Initialize an empty list to store nodes and a dictionary for quick access using node values
        self.node_lst = []
        self.node_map = {}

        # Convert node values to Node objects and populate the node_lst and node_map
        for node in node_lst:
            converted = Node(node)
            self.node_lst.append(converted)
            self.node_map[node] = converted

        # Create the N-ary tree structure with m children per node
        for i in range(int(n / m)):
            start = i * m + 1
            end = i * m + m
            if end > n - 1:
                end -= end % (n - 1)
            if end < n:
                self.node_lst[i].children = self.node_lst[start : end + 1]

        # Set parent-child relationships
        for i in range(1, n):
            self.node_lst[i].parent = self.node_lst[math.ceil(i / m) - 1]

        # Set the root of the tree
        self.root = self.node_lst[0]

        # Process queries into a list of lists
        self.processed_queries = [query.split() for query in queries]

    # Lock operation
    def lock(self, node, uid):
        if (
            node.isDescendantLocked > 0
            or node.isLocked
            or self.isAncestorLocked(node.parent)
        ):
            return False

        node.uid = uid
        node.isLocked = True
        parent_node = node.parent

        # Update isDescendantLocked for ancestors
        while parent_node:
            parent_node.isDescendantLocked += 1
            parent_node = parent_node.parent
        return True

    # Unlock operation
    def unlock(self, node, uid):
        if uid != node.uid or not node.isLocked:
            return False

        node.isLocked = False
        node.uid = None
        parent_node = node.parent

        # Update isDescendantLocked for ancestors
        while parent_node:
            parent_node.isDescendantLocked -= 1
            parent_node = parent_node.parent
        return True

    # UpgradeLock operation
    def upgrade(self, node, uid):
        if node.isDescendantLocked == 0 or self.isAncestorLocked(node.parent):
            return False

        # Unlock children and lock the node
        self.unlockChildren(node, uid)
        self.lock(node, uid)

        return True

    # Helper function to check if any ancestor is locked
    def isAncestorLocked(self, node):
        while node:
            if node.isLocked:
                return True
            node = node.parent
        return False

    # Helper function to unlock children recursively
    def unlockChildren(self, node, uid):
        for child in node.children:
            self.unlock(child, uid)
            self.unlockChildren(child, uid)

    # Helper function to print the tree structure
    def __print_tree(self, node, out):
        out += (
            node.val
            + " No of Descendants Locked: "
            + str(node.isDescendantLocked)
            + " is Node Locked: "
            + str(node.isLocked)
            + ",\n"
        )
        for child in node.children:
            out = self.__print_tree(child, out)
        return out

    def __str__(self):
        return self.__print_tree(self.root, "")


# Example usage
n = 7  # Number of nodes
m = 2  # Number of children per node
nodes = ["World", "Asia", "Africa", "China", "India", "SouthAfrica", "Egypt"]
# queries = ["1 China 9", "1 India 9", "3 Asia 9", "2 India 9", "2 Asia 9"]
queries = ["1 China 9", "2 India 9", "3 Asia 9"]
obj = Tree(n, m, nodes, queries)

res = []

# Process queries and store results in 'res'
for query in obj.processed_queries:
    if query[0] == "1":
        res.append(obj.lock(obj.node_map[query[1]], query[2]))
    elif query[0] == "2":
        res.append(obj.unlock(obj.node_map[query[1]], query[2]))
    elif query[0] == "3":
        res.append(obj.upgrade(obj.node_map[query[1]], query[2]))

print(str(obj))
# Print the results
print(res)
