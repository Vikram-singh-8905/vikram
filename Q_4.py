""" Q. Given a string and a number N, we need to mirror the characters the characters from the N-th position up to the lenght of the string in alphbetical order . In mirror operation we change 'a' to 'z','b' to 'y', and so on."""
# zip()- use to combine corrosponding values of 2 lists and change into adictonary
input_string = input("enter string : ")
n = int(input("enter number : "))

# creating dictionary for mirror operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1]
dict1 = dict(zip(alphabets,reverse_alphabets))

# finding the part of string on which we will do mirror operation
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

# finding the mirro string 
mirror = ""
for i in range(0,len(suffix)) :
    mirror +=  dict1[suffix[i]]
# creating the final string
final_string = prefix + mirror
print("the result is : ",final_string)