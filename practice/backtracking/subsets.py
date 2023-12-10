def subsets(nums):
    def backtrack(start, path):
        subsets.append(path[:])
        print("Main ", subsets)

        print("Start", start)

        for i in range(start, len(nums)):
            path.append(nums[i])
            print("path", path)
            backtrack(i + 1, path)
            print("In loop", subsets)
            print("Pop", path.pop())

        print("_" * 100)

    subsets = []
    backtrack(0, [])
    return subsets


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
