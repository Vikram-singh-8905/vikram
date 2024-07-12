list = [13,16,48,32,34,62,21,75,35,7]

def avg_finder(list) :
    sum = 0
    for i in list :
        sum += i
    return sum / len(list)
print("The average of list is : ",avg_finder(list))

def even_finder(list) :
    container = []
    for i in list :
        if i % 2 == 0 :
         container.append(i)
    return container
even_number = even_finder(list)
print("the all even value of list is : ",even_number)

def avg_even_finder(even_number) :
    sum = 0
    for i in even_number :
        sum += i
        return sum / len(even_number)
print("The average of even numbers is : ",avg_even_finder(even_number))    
    
def my_min(list) :
    min = None
    for i in list :
        if min is None or i < min :
            min = i
    return min
print(my_min(list))

def my_max(list) :
    max = None
    for i in list :
        if max is None or i > max :
            max = i
    return max
print(my_max(list))