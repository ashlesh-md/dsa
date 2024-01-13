from functools import lru_cache


@lru_cache(None)
def factorial(number):
    if number == 1 or number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(100))
print(factorial(10))
print(factorial(500))
