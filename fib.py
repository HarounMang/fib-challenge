# Date : 30-12-2023
# Author : Haroun Mangal

MAX_VALUE = 4_000_000

def dynamic_fib(nth_number):
    """
    Calculates the nth (zero-indexed) Fibonacci number using a dynamic programming approach.
    Raises a ValueErrow for negative inputs.
    nth_number : The nth Fibonacci number to calulate starting from zero.
    return : The nth Fibonacci number.
    """
    if nth_number < 0: raise ValueError("Negative inputs are not allowed!") 
    if nth_number <= 1: return nth_number

    results = [0 for _ in range(nth_number + 1)]
    results[1] = 1
    for i in range(2, nth_number + 1):
        results[i] = results[i - 1] + results[i - 2]
    return results[nth_number]

def calculate_sum(max_value):
    """
    Calculates the sum of all even Fibonacci numbers which are less than the max_value given as a parameter.
    The value i gets incremented by three in each iteration of the loop because the third number in the Finonacci sequence is an even number.
    max_value : Maximum value a Fibonacci number can be for it to be added to the sum.
    return : Sum of all even Fibonacci number which are less than max_value.
    """
    total_sum = 0
    i = 0
    fib_number = dynamic_fib(i)
    while fib_number < max_value:
        total_sum += fib_number
        i += 3
        fib_number = dynamic_fib(i)
    return total_sum

if __name__ ==  '__main__':
    print(calculate_sum(MAX_VALUE)) 