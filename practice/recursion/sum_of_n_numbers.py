def sum_of_n_numbers(number):
    if number <= 0:
        return number

    return number + sum_of_n_numbers(number - 1)


print(sum_of_n_numbers(10))
print(sum_of_n_numbers(5))
print(sum_of_n_numbers(100))
print(sum_of_n_numbers(3))
print(sum_of_n_numbers(8))
print(sum_of_n_numbers(0))
print(sum_of_n_numbers(-100))
