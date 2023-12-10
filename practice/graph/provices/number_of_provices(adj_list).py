from collections import deque


from collections import deque


def number_of_provinces(graph):
    provinces = 0
    visited = set()

    def bfs(start):
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for node in graph:
        if node not in visited:
            provinces += 1
            bfs(node)

    return provinces


if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: [5, 6],
        5: [4, 6],
        6: [4, 5],
        7: [8],
        8: [7],
    }
    print(number_of_provinces(graph))


def number_of_provinces(graph):
    provinces = 0
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            provinces += 1
            dfs(node)

    return provinces


if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: [5, 6],
        5: [4, 6],
        6: [4, 5],
        7: [8],
        8: [7],
    }
    print(number_of_provinces(graph))
