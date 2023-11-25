# #დავალება 1
#ამოხსნა
# # [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
# # იპოვეთ ყველაზე პატარა რიცხვი აქ
# number = input("Which One Is  Minimal Number From List:")
# print(number) #Minimal Number From List Is:
# list = [ 7, 5, 2 , 7, 20, 652, 6, 3, 62, 9]
# for minimal in list:
#     if minimal < 3:
#      print(minimal)


#დავალება 2
# input ფუნქციით შემოატანინეთ წინადადება და შემოტანილ წინადადებაში პროგრამას დაათვლევინეთ თანხმოვნები
#ამოხსნა
# sentence = input("Enter a sentence: ") #I want to play basketball, but I can't.

# consonant_count = 0

# consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# for char in sentence:
#     if char in consonants:
#         consonant_count += 1

# print(f"Number of consonants in the sentence: {consonant_count}")


#დავალება 3
# მომხმარებელს შემოატანინეთ ორი სახელი და გვარი,და შეადარეთ ერთი მეორეს,დაითვალეთ a-ს 
# რაოდენობა რომელ სახელში არის მეტი,და დაპრინტეთ მიღებული შედეგი
  #ამოხსნა

# user1 = input("")  #noi tsomaia
# user2 = input("")  #allen iverson
# a_counter = 0
# for name in user1,user2:
#     for char in name:
#         if char == "a":
#            a_counter += 1
# print(a_counter)


#დავალება 4
# ნივთმა დაიკლო ფასში 10% ით,საიდანაც გამყიდველმა აიღო 8% მოგება, რამდენ % იან მოგებას 
# აიღებდა ის ფასის დაკლებამდე? ჩაწერეთ ეს ყველა მონაცემი პითონში და დაათვლევინეთ მას
 #ამოხსნა
# price = 100  # Change this to the actual price
# discounted_percentage = 10
# profit_percentage = 8

# cost_price = price - (price * discounted_percentage / 100)
# profit_before_discount = (price * profit_percentage / 100) / cost_price * 100

# print(f"Profit Percentage before Price Reduction: {profit_before_discount:.2f}%")


#დავალება 5
# შევქმნათ ორი List-ი. ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების. დავპრინტოთ დაწყვილებულად   
# აი დააკომენტარეთ და დაგაწყვილებთო რო იცოდნენ ფბზე ეგრე დაახლოებით  :
 #ამოხსნა
# girls = ["Tako", "Salome", "Maiko", "Khatia", "Ana", "Keso", "Noi"]
# boys = ["Saba", "Honza", "Giorgi", "Giorgi", "Luka", "Anzori", "Basketball"]
# print(girls[0], "+", boys[0], "=", "<3")
# print(girls[1], "+", boys[1], "=", "<3")
# print(girls[2], "+", boys[2], "=", "<3")
# print(girls[3], "+", boys[3], "=", "<3")
# print(girls[4], "+", boys[4], "=", "<3")
# print(girls[5], "+", boys[5], "=", "<3")
# print(girls[6], "+", boys[6], "=", "<3")

#მეორე ვარიანტი input-ით

# girl_list = []
# boy_list = []
# for i in range (4):
#    girl_name = input("Enter Girls Name: ")
#    boy_name = input("Enter boys Name:")
# girl_list.append(girl_name)
# boy_list.append (boy_name)

#დავალება 6
# sheqmenit tqveni sayvareli mwerlis nawarmoebebis sia da daprintet tqventvis sauketeso
 #ამოხსნა
# writer = input("Who is Your Favourite Writer:") 
# novela = input("Which One is Your Favourite Book Of Her:")

# books = ["The Mysterious Affair at Styles","Murder on the Orient Express.", "The Murder of Roger Ackroyd",
#          "Death on the Nile", "The Mystery of the Blue Train", "The Mystery of the Blue Train",
#          "The Murder at the Vicarage", "Curtain: Poirot's Last Case", "Sleeping Murder", "Passenger to Frankfurt", "Passenger to Frankfurt", "The Clocks"]

# print(writer, "Is my favourite writer and", novela,"my favourite book of her is:", str(books[1]))


#დავალება 7
# შექმენით ლისტი სადაც სტრინგის სახით ჩაწერთ სამ ელემენტს (სამივე განსხვავებული ზომის ),
# გამოთვალეთ ელემენტების სიმბოლოების რაოდენობა და რომელიც საშუალო იქნება ის დაპრინტეთ .
#ამოხსნა
# sport = ["rugby", "football", "basketball"]
# rugby = len(sport [0])
# football = len(sport [1])
# basketball = len(sport [2])
# if rugby > football and rugby <basketball:
#    print (sport [0])
# elif football > rugby and football < basketball :
#    print (sport[1])
# else :
#    print (sport [21])


#დავალება 8
# შექმენით მეოთხე ჯგუფის წევრების სია .დაწერეთ კოდი ისე,
# რომ გაიგოთ ყველა სახელსა და გვარში ერთად რამდენი  ,,ი" და ,,ა"   იქნება.
#ამოხსნა
# a_counter = 0
# i_counter = 0
# list = ["guriko", "tinatin zuzadze", "lukas vishtekaliu", "giorgi lobjanidze","luka atabegashvili",
#         "gio abuladze", "tekla papava", "rezi nefaridze", "davit chilashvili", "gio kacitadze",
#         "mirian gelashvili", "rati murgulia", "nino solomonia", "beka giorgobiani", "beka berashvili",
#         "nini goglichadze", "giorgi chxetiani", "temo labadze", "giorgi mgeladze", "temo solomonishvili",
#         "demetre xaratishvili" "davit demuradze", "salome miladze", "rostom chagunava", "mariam cicxvaia",
#         "gio chixradze", "gigi gabitadze", "maziashvili luka", "dato quparashvili", "nika andoevi",
#         "ilia adamia", "anri zubashvili", "luka chxitunidze", "dachi vashagishvili","luka kechexmadze",
#          "noi tsomaia", "cotne sartania", "giorgi gorgiladze", "dachi abashidze", "luka suxiashvili",
#           "luka siradze", "misho chubinidze", "gigi gabitadze", "ako mitiashvili", "dito muladze",
#            "omiko mshvildadze", "nika bregvadze", "tato chogovadze"]
# for element in list:
#     for char in element:
#         if char == "a":
#              a_counter += 1
# print(a_counter)
# for element in list:
#     for char in element:
#         if char == "i":
#             i_counter += 1
# print(i_counter)

#დავალება 9
# შექმენით თქვენი ფილმების სია, რომელშიც ჩაწერთ უკვე ნანახ ფილმებს.
# მომხმარებელს(თქვენს პირობით მეგობარს) შემოატანინეთ მის მიერ რეკომენდირებული ფილმი. 
# თუ ფილმი დაემთხვევა თქვენს სიაში არსებულ ფილმს დაწერეთ “ძალიან მომეწონა ეს ფილმი ან არ მომეწონა ეს ფილმი” 
# თუ არ გაქვს ნანახი “ჩავინიშნავ და აუცილებლად ვნახავ”
 #ამოხსნა
# movies = ["Interstellar", "Me Before You", "Midnight Sun", "The Notebook", "Fast And Furious",
#           "The Maze Runner", "Hunger Games", "Good Will Hunting", "Divergent"]
# question = input("") #You Should Watch
# friend = input("")   #The Notebook
# if friend == movies[3]:
#     print("I really liked this movie")
#     print(movies[3])
# else:
#     print("I will add it to my watchlist")


#დავალება 11:
##შექმენით სია სადაც შემოიტანთ რამდენმე რიცხვს 
#მაგ:"24,50,25,90" და რომელიმე რიცხვი ჩაანაცვლეთ "69"_ით და გამოითვალეთ ამ რიცხვევის ჯამი
#ამოხსნა

# numbers = [82,77, 2, 3, 33, 30, 55]
# numbers[2] = 69
# total = 0
# for num in numbers:
#     total += num

# print("The Sum Of The Numbers Is:", total)



