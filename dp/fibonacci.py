def fibonacci(number , storage = {}):
    """
    The function calculates the Fibonacci sequence up to a given number using dynamic programming (DP) approach with memoization, 
    commonly referred to as a "top-down" DP approach to store
    previously calculated values.
    
    :param number: The number parameter represents the index of the Fibonacci sequence that we want to
    calculate. For example, if number is 5, we want to calculate the 5th number in the Fibonacci
    sequence
    :param storage: The `storage` parameter is a dictionary that is used to store previously calculated
    Fibonacci numbers. This is done to avoid redundant calculations and improve the efficiency of the
    function
    :return: the nth Fibonacci number.
    """
    if number in storage:
        return storage[number]
    
    if number <= 1:
        return number
    
    storage[number] = fibonacci(number - 1 , storage) + fibonacci(number - 2 , storage)
        
    return storage[number]



def fibonacci(n):
    """
    The above function calculates the nth Fibonacci number using bottom-up dynamic programming.
    
    :param n: The parameter `n` represents the position of the Fibonacci number you want to find. For
    example, if `n` is 5, the function will return the 5th Fibonacci number
    :return: the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def fibonacci(n):
    """
    The above function calculates the nth Fibonacci number using an iterative approach.
    
    :param n: The parameter `n` represents the position of the Fibonacci number you want to calculate.
    For example, if `n` is 5, the function will return the 5th Fibonacci number
    :return: the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev, current = 0, 1

    for _ in range(2, n + 1):
        next_fib = prev + current
        prev, current = current, next_fib

    return current



if __name__ == '__main__':
    n = 10000
    print(f"Fibonacci({n}) = {fibonacci(n)}")