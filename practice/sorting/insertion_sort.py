def insertion_sort(array):
    for i in range(0, len(array)):
        j = i 

        while j > 0 and array[j - 1] > array[j]:
            array[j - 1] , array[j] = array[j] , array[j -1]
            j -= 1

    return array


if __name__ == '__main__':
	print(insertion_sort([1 , 3 , 2 , 5 , 7 , 6]))
