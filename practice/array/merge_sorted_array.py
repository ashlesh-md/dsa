def sortedArray(a, b):
    i, j = 0, 0
    sol = []
    while i < len(a) and j < len(b):
        if a[i] <= b[i]:
            if len(sol) == 0 or sol[-1] != a[i]:
                sol.append(a[i])
            i += 1
        else:
            if len(sol) == 0 or sol[-1] != b[j]:
                sol.append(b[i])
            j += 1
    while i < len(a):
        sol.append(a[i])
        i += 1

    while j < len(b):
        sol.append(b[j])
        j += 1

    return sol


print(sortedArray([1, 2, 3, 4], [3, 4, 5, 6]))
