def selection_sort(array):
    if len(array) <= 1:
        return array

    for i in range(len(array)):
        min_index = i + array[i:].index(min(array[i:]))
        
        array[i], array[min_index] = array[min_index], array[i]

    return array


def selection_sort(array):
    if len(array) <= 1:
        return array

    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        array[i], array[min_index] = array[min_index], array[i]

    return array

if __name__ == '__main__':
	print(selection_sort([5 , 4 , 3 , 2 , 1 , 1 , 2, 3 , 4, 5]))