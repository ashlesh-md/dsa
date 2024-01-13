def reverse_array(array, index1, index2):
    if index1 >= index2:
        return array

    array[index1], array[index2] = array[index2], array[index1]

    return reverse_array(array, index1 + 1, index2 - 1)


arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, 4)
print(arr)
