# from collections import deque


# #  BFS
# def number_of_provinces(graph):
#     provinces = 0
#     n = len(graph)
#     visited = set()

#     def bfs(start):
#         queue = deque([start])
#         visited.add(start)

#         while queue:
#             node = queue.popleft()
#             for neighbor in range(n):
#                 if graph[node][neighbor] == 1 and neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(neighbor)

#     for node in range(n):
#         if node not in visited:
#             provinces += 1
#             bfs(node)

#     return provinces


# if __name__ == "__main__":
#     graph = [
#         [0, 1, 1, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 0, 0, 0, 0],
#         [1, 1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 1, 1, 0, 0],
#         [0, 0, 0, 1, 0, 1, 0, 0],
#         [0, 0, 0, 1, 1, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 1],
#         [0, 0, 0, 0, 0, 0, 1, 0],
#     ]
#     print(number_of_provinces(graph))


# DFS
def number_of_provinces(graph):
    provinces = 0
    n = len(graph)
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in range(n):
            if graph[node][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            provinces += 1
            dfs(node)

    return provinces


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
    ]
    print(number_of_provinces(graph))
