# def countDigits(n: int) -> int:
#     temp = n
#     count = 0
#     while temp:
#         if temp % 10 == 0:
#             pass
#         elif n % (temp % 10) == 0:
#             count += 1
#         temp = temp // 10
#     return count

# def add_numbers(n):
#     if n < 10: return n
#     return (n % 10) + add_numbers(n // 10)

# def reverse_numbers(n, reversed_n=0):
#     if n == 0: return reversed_n
#     return reverse_numbers(n // 10, (reversed_n * 10) + n % 10)


# def reverse_numbers(n, is_negative=False):
#     if n == 0:
#         return 0

#     if n < 0:
#         is_negative = True
#         n = -n

#     if n < 10:
#         return -n if is_negative else n

#     reversed_part = reverse_numbers(n // 10, is_negative)
#     last_digit = n % 10

#     if is_negative:
#         return -int(str(last_digit) + str(-reversed_part))
#     else:
#         return int(str(last_digit) + str(reversed_part))

# print(reverse_numbers(123))    # Output: 321
# print(reverse_numbers(-456))   # Output: -654
# print(reverse_numbers(0))      # Output: 0

# def twoSum( nums, target):
#     hashmap = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap:
#             return [i, hashmap[complement]]
#         hashmap[nums[i]] = i

# twoSum([1 , 2 , 3] , 5)

# def common_member(a, b):
#     result = [i for i in b if i not in a]
#     return result

# a = [-1924, -1910, -1840, -1797, -1714, -1640, -1638, -1567, -1564, -1409, -1141, -1115, -1068, -658, -465, -447, -434, -386, -321, -191, -186, -127, -63, 69, 186, 253, 334, 401, 482, 805, 809, 812, 833, 913, 955, 991, 1113, 1128, 1133, 1178, 1204, 1570, 1616, 1725, 1729, 1787, 1853, 1943, 1980]
# b = [-1924, -1910, -1840, -1797, -1714, -1640, -1638, -1567, -1564, -1409, -1141, -1115, -1068, -658, -465, -447, -434, -386, -321, -191, -186, -127, -63, 69, 186, 253, 334, 401, 482, 805, 809, 812, 833, 913, 955, 991, 1113, 1128, 1133, 1178, 1204, 1570, 1616, 1725, 1729, 1787, 1853, 1943, 1980]
# print("The common elements in the two lists are: ")
# print(len(set(a)) , len(b))


# import math
# def maxSubArray(nums):
#     current_maximum = -math.inf
#     sum_of_subarray = 0
#     for i in range(len(nums)):
#         sum_of_subarray += nums[i]
#         if sum_of_subarray > current_maximum:
#             current_maximum = sum_of_subarray
#         if sum_of_subarray < 0:
#             sum_of_subarray = 0
#     return current_maximum
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(nums))


# hashTable = ["", "", "abc", "def", "ghi", "jkl",
# 			"mno", "pqrs", "tuv", "wxyz"]

# def printWordsUtil(number, curr, output, n):
# 	if(curr == n):
# 		print(*output , sep="")
# 		return

# 	for i in range(n):
# 		output.append(hashTable[number[curr]][i])
# 		printWordsUtil(number, curr + 1, output, n)
# 		output.pop()
# 		if(number[curr] == 0 or number[curr] == 1):
# 			return

# def printWords(number, n):
# 	printWordsUtil(number, 0, [], n)


# if __name__ == '__main__':
# 	number = [2, 3, 4]
# 	n = len(number)
# 	printWords(number, n)


def generateWords(number):
    if not number:
        return []

    hashTable = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    queue = ['']
    result = []

    while queue:
        current_word = queue.pop(0)
        if len(current_word) == len(number):
            result.append(current_word)
        else:
            current_digit = number[len(current_word)]
            for letter in hashTable.get(current_digit, ''):
                queue.append(current_word + letter)

    return result

if __name__ == '__main__':
    number = '23'
    words = generateWords(number)
    for word in words:
        print(word)
