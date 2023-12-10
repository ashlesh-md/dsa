from collections import deque


def largest_sum_cycle(n, edge):
    cnt = [0] * n

    for i in edge:
        if i != -1 and 0 <= i < n:
            cnt[i] += 1

    q = deque()
    vis = [0] * n

    for i in range(n):
        if cnt[i] == 0:
            vis[i] = 1
            q.append(i)

    while q:
        node = q.popleft()
        if edge[node] == -1:
            continue
        if 0 <= edge[node] < n:
            cnt[edge[node]] -= 1
            if cnt[edge[node]] == 0:
                vis[edge[node]] = 1
                q.append(edge[node])

    ans = -1

    for i in range(n):
        if vis[i]:
            continue
        val = 0
        st = i
        while vis[st] == 0:
            vis[st] = 1
            val += st
            st = edge[st]
        ans = max(ans, val)

    return ans


# Example usage:
# n = 10
# edge = [4, 4, 1, 4, 13, 8, 8, 8, 0, 8]
n = 23
edge = [
    4,
    4,
    1,
    4,
    13,
    8,
    8,
    8,
    0,
    8,
    14,
    9,
    15,
    11,
    -1,
    10,
    15,
    22,
    22,
    22,
    22,
    22,
    21,
]
result = largest_sum_cycle(n, edge)
print(result)
