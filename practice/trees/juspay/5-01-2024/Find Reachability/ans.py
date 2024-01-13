from collections import defaultdict


def solve(src, dest, mp, adj):
    mp[src] = 1
    for neighbor in adj[src]:
        if not mp[neighbor]:
            solve(neighbor, dest, mp, adj)


def main():
    n = int(input())
    mp = defaultdict(int)

    for _ in range(n):
        x = int(input())
        mp[x] = 0

    e = int(input())
    adj = defaultdict(list)

    for _ in range(e):
        x, y = map(int, input().split())
        adj[x].append(y)

    src = int(input())
    dest = int(input())
    solve(src, dest, mp, adj)
    print(mp[dest])


if __name__ == "__main__":
    main()
