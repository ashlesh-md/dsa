from collections import deque


# def detect_cycle(matrix):
#     visited = set()
#     path = [False] * len(matrix)

#     def bfs(start):
#         _deque = deque([start])
#         while _deque:
#             node = _deque.popleft()

#             for adj_node in matrix[node]:
#                 if adj_node == node:
#                     return True
#                 elif adj_node not in visited:
#                     _deque.append(adj_node)
#                     visited.add(adj_node)
#                     path[adj_node] = not path[adj_node]
#                 elif adj_node in visited and path[adj_node]:
#                     return False
#         return True

#     for i, j in matrix:
#         if i not in visited and not bfs(i):
#             return False

#     return True


def detect_cycle(matrix):
    visited = set()
    path = [False] * len(matrix)

    def dfs(node):
        visited.add(node)
        path[node] = True

        for element in matrix[node]:
            if node not in visited and dfs(element) and path[element]:
                return True

        path[node] = False
        return False

    for i in range(len(matrix)):
        if i not in visited and not dfs(i):
            return False
    return True


if __name__ == "__main__":
    adjecency_matrix = [[0, 1], [1, 2], [2, 3], [3, 0], [3, 3]]
    print(detect_cycle(adjecency_matrix))
