from collections import deque


# Consider two colours Red and Green
def bipartite(graph):
    n = len(graph)
    colors = [None] * n

    def dfs(start):
        _deque = deque([(start, "Red")])
        visited = set()
        colors[start] = "Red"
        visited.add(start)

        while _deque:
            node, color = _deque.popleft()
            for element in graph[node]:
                if element not in visited and color == "Red":
                    colors[element] = "Green"
                    _deque.append((element, "Green"))
                    visited.add(element)
                elif element not in visited and color == "Green":
                    colors[element] = "Red"
                    _deque.append((element, "Red"))
                    visited.add(element)
                elif element in visited and colors[element] == color:
                    return False
        return True

    for i in range(n):
        if not colors[i] and not dfs(i):
            return False

    return True


if __name__ == "__main__":
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(bipartite(graph))
