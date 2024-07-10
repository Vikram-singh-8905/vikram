# Factorial of a number
# function for calculating factorial of a number
def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for i in range (1,n+1) :
            ans *= i
    return ans


n = int(input("Enter n : "))

output = factorial(n)
print("the factorial is : ",output)


# Question -1
x = 50 
def func(x) :
    x = 2
    print(x)
func(x)
print('x is now',x)


# Question - 2
def say(message, times=1) :
    print(message * times)
say('hello')
say('world',5)    