from typing import Dict, List


class Tree:
    def __init__(self, parent=None):
        self.isLocked = False
        self.isLockable = True
        self.id = -1
        self.ma = None
        self.parent = parent
        self.children = []


def locking(node, uuid):
    if not node.isLockable or node.isLocked:
        return False

    queue = [node]
    while queue:
        current_node = queue.pop(0)
        for child in current_node.children:
            if child.isLocked:
                return False
            queue.append(child)

    node.id = uuid
    node.isLocked = True

    queue = [node]
    while queue:
        current_node = queue.pop(0)
        for child in current_node.children:
            child.isLockable = False
            queue.append(child)

    return True


def unlocking(node, uuid):
    if not node.isLockable or not node.isLocked or (node.isLocked and uuid != node.id):
        return False

    node.isLocked = False
    node.id = -1

    queue = [node]
    while queue:
        current_node = queue.pop(0)
        for child in current_node.children:
            child.isLockable = True
            queue.append(child)

    return True


def update(node, uuid):
    if not node.isLockable or node.isLocked:
        return False

    flag = False
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        for child in current_node.children:
            if child.isLocked and child.id != uuid:
                return False
            if child.isLocked:
                flag = True
            queue.append(child)

    if not flag:
        return False

    queue = [node]
    while queue:
        current_node = queue.pop(0)
        for child in current_node.children:
            if child.isLocked:
                if not unlocking(child, uuid):
                    return False
            queue.append(child)

    return locking(node, uuid)


def main():
    n, m, q = 7, 2, 5
    nodes = ["World", "Asia", "Africa", "China", "India", "South Africa", "Egypt"]
    queries = [
        "1 China 9",
        "1 India 9",
        "3 Asia 9",
        "2 India 9",
        "2 Asia 9",
    ]

    sToT: Dict[str, Tree] = {}
    t = Tree()
    sToT[nodes[0]] = t
    queue = [t]
    k = 1

    for i in range(1, n):
        temp = queue.pop(0)
        while k < n and len(temp.children) < m:
            s = nodes[k]
            u = Tree(temp)
            sToT[s] = u
            temp.children.append(u)
            queue.append(u)
            k += 1

    sol: List[bool] = []
    for i in range(n, n + q):
        qn, name, uuid = map(str, queries[i - n].split())
        qn, uuid = int(qn), int(uuid)
        ans = None

        if qn == 1:
            ans = locking(sToT[name], uuid)
        elif qn == 2:
            ans = unlocking(sToT[name], uuid)
        else:
            ans = update(sToT[name], uuid)

        if ans:
            sol.append(True)
        else:
            sol.append(False)

    print(sol)


if __name__ == "__main__":
    main()
