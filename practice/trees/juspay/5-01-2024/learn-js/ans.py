import heapq


def shortest_time_to_reach_b(N, followers, E, messages, A, B):
    graph = {i: [] for i in range(1, N + 1)}
    for follower in followers:
        graph[follower] = []
    for follower, following, time in messages:
        graph[follower].append((following, time))

    def dijkstra(start, target):
        min_heap = [(0, start)]
        visited = set()

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)

            if node == target:
                return time

            for neighbor, neighbor_time in graph[node]:
                heapq.heappush(min_heap, (time + neighbor_time, neighbor))

        return -1

    return dijkstra(A, B)


N = int(input())
followers = [int(input()) for _ in range(N)]
E = int(input())
messages = [tuple(map(int, input().split())) for _ in range(E)]
A = int(input())
B = int(input())

result = shortest_time_to_reach_b(N, followers, E, messages, A, B)
print(result)
