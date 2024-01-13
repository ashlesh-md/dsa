# def print_all_substrings(input_string):
#     n = len(input_string)

#     for i in range(n):
#         for length in range(1, n - i + 1):
#             substring = input_string[i : i + length]
#             print(substring)


# # Example usage:
# input_str = "abc"
# print("All non-empty substrings of '{}' are:".format(input_str))
# print_all_substrings(input_str)


# def non_repeated_string_length(arr):
#     left = 0
#     right = 0
#     length = 0
#     visited = []

#     while right < len(arr):
#         if arr[right] not in visited:
#             visited.append(arr[right])
#             right += 1
#             length = max(length, right - left)

#         else:
#             visited.remove(arr[right])
#             left += 1

#     return length


# print(non_repeated_string_length(["a", "b", "c", "a", "a", "b", "c", "d", "b", "a"]))

N = int(input())
dic = {}


def addnode(u, v):
    dic[u].append(v)


for i in range(N):
    n1 = int(input())
    dic[n1] = []

edge = int(input())
for i in range(edge):
    u, v = map(int, input().split())
    addnode(u, v)
start = int(input())
end = int(input())
tr = []
tr.append(start)


def traverse(dic, start):
    for i in dic[start]:
        if i == end:
            return
        if len(dic[start]) == 0:
            return
        else:
            tr.append(i)
            traverse(dic, i)


traverse(dic, start)
tr = sorted(tr)
for i in tr:
    print(i, end=" ")
