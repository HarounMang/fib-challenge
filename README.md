# Challenge – Even Fibonacci numbers

In fib.py is my attempt at solving the even Fibonacci number challenge. That is, by considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms. 

The way I solved this is by noticing that only that each third number in the Fibonacci number is an even number starting from index 3. So the 3th, 6th, 9th, etc. are only even numbers in the Fibonacci sequence (starting from 0). 

Firstly, all even Fibonacci numbers less than four million are calculated using a dynamic programming approach. Then each third element in the sequence gets summed up starting from index 3. Even though 0 is also an even number, we discard since adding it won't change the total sum.

To run the code:
1. Clone the repository
2. Open a terminal
3. Make sure to cd to the correct folder
4. Run the file by typing either 'python fib.py' or 'python3 fib.py' in your terminal
