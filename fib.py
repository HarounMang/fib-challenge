# Date : 31-12-2023
# Author : Haroun Mangal

MAX_VALUE = 4_000_000

def calculate_fib_sequence(max_value):
    """
    Calculates the Fibonacci sequence, using a dynamic programming approach, 
    up until the last Fibonacci numer is bigger than the ax_value given as a parameter.
    Raises a ValueErrow for negative inputs.
    max_value : No number in the sequence can exceed this value.
    return : The Fibonacci sequence of all numbers less than max_value.
    """
    if max_value < 0: raise ValueError("Negative inputs are not allowed!") 
    if max_value <= 1: return range(max_value)

    fib_sequence = [0, 1]
    while fib_sequence[-1] < max_value:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def sum_even_fib_numbers(fib_sequence):
    """
    Calculates the sum of all even Fibonacci numbers. The value i gets incremented by three in each iteration of the loop because starting from 2
    (index 3) the third number in the Finonacci sequence is an even number.
    fib_sequence : Array containing the Fibonacci sequence.
    return : Sum of all even Fibonacci numbers.
    """
    total_sum = 0
    for i in range(3, len(fib_sequence), 3):
        total_sum += fib_sequence[i]
    return total_sum

if __name__ ==  '__main__':
    fib_sequence = calculate_fib_sequence(MAX_VALUE)
    print(sum_even_fib_numbers(fib_sequence))
