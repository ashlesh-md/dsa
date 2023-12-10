def max_weight_cell(n, edge):
    cnt = [0] * n

    for i in range(n):
        if edge[i] != -1:
            cnt[edge[i]] += i

    ans = -1
    maxi = float("-inf")

    for i in range(n):
        if maxi <= cnt[i]:
            maxi = cnt[i]
            ans = i

    return ans


# Example usage:
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
result = max_weight_cell(n, edge)
print(result)
