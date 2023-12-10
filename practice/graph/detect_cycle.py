from collections import deque


def detect_cycle(adj, v, e):
    visited = set()

    def bfs(start):
        _deque = deque([(start, None)])

        while _deque:
            current_node, parent = _deque.popleft()

            visited.add(current_node)

            for neighbor in adj[current_node]:
                if neighbor not in visited:
                    _deque.append((neighbor, current_node))
                elif parent != neighbor:
                    return True

        return False

    for i in range(v):
        if i not in visited:
            if bfs(i):
                return True

    return False


if __name__ == "__main__":
    adj = [[], [2], [1, 3], [2]]
    print(detect_cycle(adj, 4, 2))
