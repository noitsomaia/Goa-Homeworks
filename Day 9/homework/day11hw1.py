# #პირველი დავალება

# # დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
# # რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს 
# # მოემატება 1 ქულა და გადავალთ შემდეგზე(ოღონდ ეს ვეღარ უპასუხებს იმ დღეს)( ანუ remove დაგჭირდებათ),
# #ცალკე უნდა იყოს ქულების სიაც


# # #india, 1997, red, allen iverson, 1939 september ,leonardo da vinci

# import random
# #creating list of students and import them by a random choice
# students = ["noi tsomaia", "cotne sartania", "giorgi gorgiladze", "dachi abashidze", "luka suxiashvili",]
# #creating while loop
# while students:
#     # select one of random member from list
#     selected_member = random.choice(students)
#     #creating question and add selecte member who will answer this question
#     question = f"{selected_member}, answer this question: Which country are you visiting if you are in the Taj Mahal? "
#     #input question in input and let student answer by herself
#     response = input(question)
#     #creating if and else to print if answer is right or not
#     if response  == "india":
#        print(f"{selected_member} answered correctly! 10 point added")
#     else:
#        print(f"{selected_member} did not answer correctly")
       
#     #Remove selected member
#     students.remove(selected_member)

#     selected_member2 = random.choice(students)

#     question2 = f"{selected_member2}, answer this question:  What year was the movie Titanic released: "

#     response2 = input(question2)

#     if response2 == 1997:
#        print(f"{selected_member2} answered correctly! 10 point added")
#     else:
#        print(f"{selected_member2} did not answer correctly")

#        students.remove(selected_member2)

#        selected_member3 = random.choice(students)

#     question3 = f"{selected_member3}, answer this question:  Who is best basketball player: "

#     response3 = input(question3)

#     if response3 == "allen iverson":
#        print(f"{selected_member3} answered correctly! 10 point added")
#     else:
#        print(f"{selected_member3} did not answer correctly")

#        students.remove(selected_member3)

#        selected_member4 = random.choice(students)

#     question4 = f"{selected_member4}, answer this question: When did World War II begin : "

#     response4 = input(question4)

#     if response4 == "1939, september 1":
#        print(f"{selected_member4} answered correctly! 10 point added")
#     else:
#        print(f"{selected_member4} did not answer correctly")

#        students.remove(selected_member4)

#        selected_member5 = random.choice(students)

#     question5 = f"{selected_member5}, answer this question: Who painted the Mona Lisa : "

#     response5 = input(question5)

#     if response5 == "Leonardo da vinci":
#        print(f"{selected_member5} answered correctly! 10 point added")
#     else:
#        print(f"{selected_member5} did not answer correctly")

#        students.remove(selected_member5)

# print("All Group Members Have Answered For The Day")



# #დავალება 2

# #შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი, 8 სიმბოლოიანი, სადაც აუცილებლად 
# #სიმბოლო იქნება !#*#%(*#)^#, 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347
# #მაგ: !n8391k*

# import random
# #creating lists for numbers sy and letters. with this we are creating passwords
# symbols =  ["!", "@", "#" , "$" , "%" , "^" , "&", "*"]
# letters = ("A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h","I", "i","J", "j",  "K" "k", "L", "l", 
#            "M", "m","N", "n", "O", "o","P", "p","Q", "q", "R", "r","S", "s","T", "t", "U", "u","V", "v","W", "w", "X","x", "Y ", "y","Z", "z")
# numbers = [0,1,2,3,4,5,6,7,8,9]
# password = ""
# #creating for loop in range 2 for symbols because condition is to have 2 sy in password
# for i in range (2):
#     #select sy with random choice
#     selected_symbols = random.choice(symbols)
#     #selected sy will add in random password
#     password += selected_symbols
#     #we need only need 4 for number from list so creating for loop in range 4
# for i in range (4):
#     selected_numbers = random.choice(numbers)
#     password += str(selected_numbers)
#     #and also 2 letters so for loop in range 4
# for i in range (2):
#     selected_letters = random.choice(letters)
#     password += selected_letters
#     #print result
# print("This Is Random Password:", password)


# #მესამე დავალება

# from turtle import *
# import random
# speed(100000)
# colors = ["red", "green", "purple", "blue", "yellow" ]

# for i in range(10000):
#     width(random.randint(1,10))
#     color(random.choice(colors))
#     forward(random.randint(0,100))
#     right(random.randint(0,100))
   
# exitonclick()