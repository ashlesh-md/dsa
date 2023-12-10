from collections import defaultdict, deque

arr = [4, 4, 1, 4, 13, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21]
n = 23
c1, c2 = 9, 2

G = defaultdict(list)
for u, v in enumerate(arr):
    if v == -1:
        continue
    G[u].append(v)


def bfs():
    q = deque([[c1, 1], [c2, 2]])
    vis = [0] * n
    while q:
        node, num = q.popleft()
        if vis[node] == 2 and num == 1 or vis[node] == 1 and num == 2:
            return node

        if vis[node] == num:
            continue

        vis[node] = num
        for nei in G[node]:
            q.append([nei, num])

    return -1


print(bfs())
