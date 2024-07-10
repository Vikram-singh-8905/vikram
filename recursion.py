# _______Recursion_______
# def.- recursive function call to itself for dividing problem in subproblms
# recursion have two parts - 1. Base case & 2. Recursive case
# Base case - when function will return value without calling itself OR stoping point of recursive function is called base case
# Recursive case - when function will call itself for solving subproblem
# memory me recurtion work karta hai with help of call stack - LIFO(last in first out)

# Factorial of n ---
def factorial(n) :
    # base case
    if n == 0 :
        return 1
    # recursive case
    ans = n * factorial(n-1)
    return ans
n = int(input("Enter the value of n : "))
print(factorial(n))

# Q.- Write a program to print numbers from n to 1.
def print_numbers(n) :
    # base case
    if n == 0 :
        return 
    #print(n)
    # recursive case
    print_numbers(n-1)
    print(n)
n = int(input("Enter the value of n : "))
print_numbers(n)

# Q. - write a program to print sum from 1 to n.
def sum(n) :
    # base case
    if n == 1 :
        return 1
    # recursive case
    ans = n + sum(n-1)
    return ans 
n = int(input("Enter the value of n : "))
print(sum(n))

# Q. - Make a function which calculates 'a' raised to power 'b' using recursion.
def power(a,b) :
    # base case
    if b == 0 :
        return 1
    # recursive case
    ans = a * power(a,b-1)
    return ans
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print(power(a,b))

# # Q. - Make a function which calculates Fibonacci sequence using recursion.
def fibonacci(n) :
    # base case
    if n == 1 : # base case
        return 0
    elif n == 2 : # base case
        return 1
    else :   # recursive case
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the value of n : "))
# print(fibonacci(n))
for i in range (1,n+1) :
    print(fibonacci(i))