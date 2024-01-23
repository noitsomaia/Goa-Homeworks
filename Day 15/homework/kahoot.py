#Kahoot questions answers and examples

# 1. What is the function used to display text in Python?
# Print() 
##example   #print("hello world")
# 2. In Python, which data type is used to store a whole number?                                
#Integer      (integer is whole number like 0,1,2,3,4,5,6,7,8,9...)
# 3. Which of the following data types is used to store text in Python             
 #string       (text in python is called string)
# 4. What is the result of the expression 10 + 5 * 2 in Python?                                    
#20       #print(10+5*2)
# 5. Which of the following is the correct way to assign the value 42 to a variable named answer in Python?
# answer = 42    #(variable is "answer" and value is "42")
# 6. What is the process of identifying and fixing errors in a program called?
#Debugging 
# 7. Which is commonly used in Python for naming variables and functions, where words are separated by underscores?
#snake_case      #(user_name for example)
# 8. What is the primary purpose of adding comments to your Python code.        
 #to provide explanations and documentation for the code #(It's for humans to understand code)
# 9. How can you take user input in Python?
#input()       #for example user = input()
# 10. Which of the following is not a built-in data type in Python?
# Array      #(An array is a data structure that stores values of the same type)
# 11. What function can be used to check the data type of a variable in Python?
#type()        #for example 
# noi = 20
# print(type(noi))
# 12.    How can you convert an integer to a string in Python?                                  
#str()    
# noi = 20
# print(str(noi))
# 13.    What is the term for converting one data type into another in Python?
#converting/casting
# 14.    Which operator is used to check if two values are equal in Python?           
#==   
# if 20 == 20:
#     print("it equals")
# 15.    What is the result of the logical AND operation between True and False in Python?                                                
#False 
# example = 2==2 and 2==3
# print(example)
# 16.    What will the expression (5 > 3) and (10 < 20) evaluate to in Python?        
#True
# example = 5 > 3 and 10 < 20
# print(example)
# 17.    In Python, what is used to make decisions and execute different code blocks based on conditions?
#control flow 
# 18. Which type of loop is used to iterate over a sequence (e.g., a list or string) in Python?
# For loop
# my_list=[0,1,2,3]
# for i in range(5):
#     print(my_list)
# 19 . What type of loop is used when you want to repeat a block of code as long as a condition is true?
# While loop
# i = 1
# while i < 5:
#     print(i)
#     i += 1
# 20. What does the range() function in Python print(?
#a sequence of numbers
# number = 3
# for i in range(3):
#     print(number)
# 21.    Which keyword is used to start an "if" statement in Python?                              
#if
# if 3 == 3:
#     print("Goa Is Cool")
# 22.    What is the purpose of the "else" statement in Python's "if-else" construct?
#to execute code when the "if" and "elif" conditions are false
# noi = 20
# salome = 17
# if noi > 25:
#     print("rame")
# elif salome < 3:
#     print("ravici")
# else:
#     print("Good Job")
# 23.    Which data structure is used to store an ordered collection of items in Python?                                                   
#list
# my_list = [1,2,3,4,5]
# 24.    In Python, which index represents the first element of a sequence?                            
#0        #count starts from zero so first elements index will be 0
# 25.    How can you access the third element of a list in Python?              
#my_list[2]
# my_list = [3,33,30,19]
# print(my_list[2])
# 26.    What does slicing allow you to do with a sequence in Python?
#access a part of a list
# text = "Hello, World!"
# print(text[2:])
# 27.    How can you extract a subsequence of a list from index 2 to index 5 (5 must be included) in Python?                      
#my_list[2:6]
# my_list = [3,14,19,21,30,77]
# print(my_list[2:6])
# 28.    What does the "step" value in slicing indicate? 
#the increment between elements     #[start:stop:step]
# 29.    What is a reusable block of code in Python that performs a specific task called?                                            
#Function
# 30.    In Python, what are the values passed to a function called?
#arguments
# 31. Which string method is used to convert a string to uppercase in Python?          
#upper()
# 32.    What list method is used to add an element to the end of a list in Python? 
#append()
# my_list = [1,2,3,4,5]
# my_list.append(6)
# print(my_list)
# 33.    In Python, which keyword is used to define a new function?                                
#def
# 34.    What keyword is used to print( a value from a function in Python?       
#print(




# codewars 
#  homework 1
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# solution

# def summation(num):   
#     print( num * (1 + num) / 2
# print(num)


#homework 2
# Make a function that will print( a greeting statement that uses an input; your program should print(, "Hello, <name> how are you doing today?".
# solution

# def greet(name):
#     print( f"Hello, {name} how are you doing today?"

# print(f"Hello, {name} how are you doing today?")

#homework 3
# Clock shows h hours, m minutes and s seconds after midnight.
# Your task is to write a function which print(s the time since midnight in milliseconds.
#solution

# def past(h, m, s):
#    print( (h * 3600 + m * 60 + s ) * 1000

#homework 4
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 print( 0.
#solution

# def paperwork(n, m):
#     if n > 0 and m > 0:
#         print( m * n
#     print( 0


#homework 5
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

#solution

# def abbrev_name(name):
#     my_list = name.split()
#     list_name = my_list[0]
#     list_surname = my_list[1]
#     print( (list_name[0] + "." + list_surname[0]).upper()


#homework 6
# Implement a function which convert the given boolean value into its string representation.
# Note: Only valid inputs will be given.

#solution

# def boolean_to_string(b):
#     print( str(b)
# print(str(b))


#homework 7
# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should print( result of numbers after applying the chosen operation.

#solution

# def basic_op(operator, value1, value2):
#     if operator == "+": 
#         print( value1 + value2
#     if operator == "-": 
#         print( value1 - value2
#     if operator == "*":
#         print( value1 * value2
#     if operator == "/": 
#         print( value1 / value2

# def basic_op(operator, value1, value2):
#     if operator == "+": 
#         print( value1 + value2)
#     if operator == "-": 
#         print( value1 - value2)
#     if operator == "*":
#         print( value1 * value2)
#     if operator == "/": 
#         print( value1 / value2)