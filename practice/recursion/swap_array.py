# def swap_array(array , start , end):
#     if start >= end:
#         return
#     array[start] , array[end] = array[end] , array[start]
#     swap_array(array , start + 1 , end - 1)

def swap_array(array , index = 0):
    if index >= len(array) // 2:
        return
    array[index] , array[len(array) - index - 1] = array[len(array) - index - 1] , array[index]
    swap_array(array , index + 1)

if __name__ == '__main__':
    array = [1 ,2 , 3 , 4 , 5]
    # print(*array)
    # swap_array(array, 0 , len(array) - 1)
    # print(*array)
    # swap_array(array, 0 , len(array) - 1)
    print(*array)
    swap_array(array)
    print(*array)
    swap_array(array)
    print(*array)
    swap_array(array)
    print(*array)

