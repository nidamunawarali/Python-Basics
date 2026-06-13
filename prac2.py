# #------------------------Weight Converter Programs-----------------------------------
# weight = int(input("Enter Weight: "))
# unit = input("(L)bs or (K)gs: ")

# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"Weight in Kgs: {converted}")

# elif unit.upper() == "K":
#     converted = weight / 0.45
#     print(f"Weight in Lbs: {converted}")
# else:
#     print("Wrong Input. Please enter L or K")

#------------------------- While Loop --------------------------------
# i = 1
# while i<=5:
#     print('* ' * i)
#     i+=1


# #--------------Guessing Game-----------------
# secret_number = 12
# guess_count = 1
# while guess_count <= 3:
#     guess = int(input("Guess: "))
#     guess_count+=1
#     if guess==secret_number:
#         print("You Won!")
#         break
# else:
#     print("Sorry, You Failed!")


#----------------Building the Car Game------------
# command =""
# is_started = False
# while True:
#     command = input("> ").lower()
#     if command == "help":
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
# ''')
#     elif command == "start":  
#         if is_started:
#             print("Car is already started")
#         else:
#             is_started = True
#             print("Car started... Ready to go!")

#     elif command == "stop":
#         if not is_started:
#             print("Car is already stopped.")
#         else:
#             is_started = False
#             print("Car stopped.")
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand that...")


#---------------------------------------FOR LOOP--------------------------------------------

# for item in 'Python':
#     print(item)


# for item in ['Mosh', 'John', 'Sarah']:
#     print(item)

# for item in range(10):
#     print(item)

# for item in range(5, 10):
#     print(item)

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total = 0

# for item in prices:
#     total += item
# print(f"Total: {total}")

#---------Nested loops------------------

# for x in range(4):
#     for y in range(3):
#         print(f"({x} , {y})")


# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     print("x" * item)


# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output=''
#     for count in range(x_count):
#         output+= 'x'
#     print(output)

# numbers = [2, 2, 2, 2, 7]
# for x_count in numbers:
#     output=''
#     for count in range(x_count):
#         output+= 'x'
#     print(output)


#-----------------------------------LISTS-------------------------------------

# names =["Nida", "Rija", "Hiba", "Mohsin", "Zara", "Hamza"]
# print(names[2:4])

# names =["Nida", "Rija", "Hiba", "Mohsin", "Zara", "Hamza"]
# names[0] = "Nidaaaa"
# print(names)

# numbers = [12, 34, 56 , 75, 45, 177, 345, 234, 12]
# max = numbers[0]
# for number in numbers:
#     if number> max:
#         max = number
# print(f"Largest number is: {max}")


#--------------2D LISTS----------------

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[0][2] = 20
# print(matrix[0][2])

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for item in row:
#         print(item)



# numbers = [2, 34, 34, 56, 88]
# numbers.append(12)     #add number end of the list
# numbers.insert(0, 1)    # add number of the given index
# numbers.remove(88)       # remove any number
# numbers.pop()        # remove last number
# #numbers.clear()         # remove whole list
# #print(numbers)
# print(numbers.index(34))
# print( 100 in numbers)
# print(56 in numbers)
# print(numbers.count(34))
# numbers.sort()
# numbers.reverse()
# print(numbers)

# numbers = [1, 2, 3 ,4, 5, 7]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)


#write a program to remove duplicate in a list

# numbers = [2, 3, 5, 7, 2, 5, 6, 10]
# uniques = []

# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)


#------------------------------TUPLES----------------------------------------------
#we cannot mutate or change tuples, they are immutable

# numbers = (1, 2, 2, 4, 3)
# print(numbers)
# print(numbers[0])
# print(numbers.count(2))
# print(numbers.index(3))


#------------------Unpacking----------------------

# coordinates = (1, 2, 3)            # tuples
# x, y, z = coordinates        # x = 1, y = 2, z = 3
# print(x)


# coordinates = [1, 2, 3]           # list
# x, y, z = coordinates
# print(y)


#---------------------------DICTIONARIES-------------------------------
# customer = {
#     "Name": "John Smith",
#     "Age": 30,
#     "is_verified": True
# }

# customer["Name"] = "Jack Smith"
# customer["birth_date"] = "Jan 1 1978"
# #print(customer["Name"])
# print(customer.get("Name"))
# print(customer.get("birth_date"))
# print(customer.get("name"))


# phone = input("Phone: ")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }

# output = ""
# for ch in phone:
#    output+= digits_mapping.get(ch, "!") + " "

# print(output)


#----------Emoji Converter-----------------

# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",      # shortcut key press window dot 
#     ":(": "😞"
# }

# output =""
# for word in words:
#    output+= emojis.get(word, word) + " "
# print(output)


