# using inrementing loop and with best TC O(N)
def bubble_sort(array):
	for i in range(len(array) - 1):
		did_swap = False
		for j in range(len(array) - i - 1):

			if array[j] > array[j + 1]:

				array[j] , array[j + 1] = array[j + 1] , array[j]
				did_swap = True

		if not did_swap:
			break

		print(array)

	return array


# # using decrementing loop 
# def bubble_sort(array):
# 	for i in range(len(array) , 0 , -1):

# 		for j in range(0 , i - 1):

# 			if array[j] > array[j + 1]:
# 				array[j] , array[j + 1] = array[j + 1] , array[j]
	
# 		print(array)

# 	return array


if __name__ == '__main__':
	# print(bubble_sort([5 , 4 , 2 , 3 , 1 , 100 , 20 , -10 , 4 , 2 , 10]))
	print(bubble_sort([1 ,2 , 4 , 3, 5, 6]))
