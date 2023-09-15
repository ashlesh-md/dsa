# def tapping_rain_water(heights):
#     ans = 0
#     n = len(heights)
#     for index in range(1 , n - 1 ):
#         right = heights[index]
#         for right_index in range(index):
#             right = max(heights[right_index] , right)
#         left = heights[index]
#         for left_index in range(index + 1 , n):
#             left = max(heights[left_index] , left)
#         ans += (min(left , right) - heights[index])
#     return ans
def tapping_rain_water(heights):
    ans = 0
    n = len(heights)
    right , left = n - 1 , 0
    left_max , right_max = 0 , 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] > left_max:
                left_max = heights[left]
            else:
                ans += (left_max - heights[left])
            left += 1
        else:
            if heights[right] > right_max:
                right_max = heights[right]
            else:
                ans += (right_max - heights[right])
            right -= 1
    return ans


print(tapping_rain_water([2 , 0 , 2]))
print(tapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(tapping_rain_water([3, 0, 2, 0, 4]))
print(tapping_rain_water([0,2,0]))
print(tapping_rain_water([4,2,3]))
print(tapping_rain_water([0 , 1 , 0 , 1 , 0 , 1, 0]))
