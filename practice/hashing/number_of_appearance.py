def number_of_appearance(array):
	storage = {}
	for element in array:

		if element in storage:
			storage[element] += 1

		else:
			storage[element] = 1

	return storage;


if __name__ == '__main__':
	numbers = number_of_appearance([1 , 2 , 3 , 1 , 2 , 2, 3 , 5 ,1 , 5 , 5 , 5])
	print(numbers)
	print(dict(sorted(numbers.items())))
	print(dict(sorted(numbers.items(), key = lambda x: (x[1] , x[0]))))
