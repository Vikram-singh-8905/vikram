#defining the function
def sumOneToN(n) :
     sum = 0
     for i in range(1, n+1):
         sum += i
     return sum

n = int(input("Enter the n : "))
# call function
output = sumOneToN(n)
print("The sum of 1 to n is : ", output)
n1 = int(input("Enter the n1 : "))
output2 = sumOneToN(n1)
print("The sum of 1 to n1 is : ", output2)

# Nested function 
def outer_function() :
    x = 1
    def inner_function() :
        y = 2
        result = x+y
        return result
    return inner_function()
output = outer_function()
print(output)