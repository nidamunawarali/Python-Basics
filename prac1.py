#-------Receiving Input---------------
#name = input("What is your name? ")
#color = input("What is your fvrt color? ")
#print(name +" likes "+color)

#-------Type Conversion---------------
# birth_year = input("What is your birth year? ")
# age = 2026 - int(birth_year)
# print(f"Your age is: {age} ")

# lb = input("What's your weight in pounds (lb): ? ")
# kg = int(lb) * 0.45
# print(f"Weight is kgs: {kg}")


#------------------Strings---------------------
# course = 'Python for beginners'
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[1:])
# print(course[:5])

# first = "John"
# last = "Smith"
# message = first + " [" + last + "] is a coder"
# print(message)
# msg = f'{first} [{last}] is a coder'
# print(msg)


#--------------------String Methods------------------------
# course = "Python for beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find('P'))
# print(course.replace('beginners', 'Absolute Beginners'))
# print('Python' in course)
# print('PHYTHON' in course)

#-----------------------Arithmatic Operations----------------------
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 ** 3)
# print(10 // 3)
# print(10 % 3)

# x = 10 + 3 * 2 ** 2    #follow BODMAS rule 
# print(x)

# x = (10 + 3) * 2 ** 2 
# print(x)

#-------------------Math Function----------------
# import math
# x = 2.9
# print(round(x))
# print(abs(-2.9))
# print(math.ceil(2.9))
# print(math.floor(2.9))
# is_hot = False
# is_cold = True


#--------------------- IF Statements ----------------------
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")


# price = 100000
# has_good_credit = False

# if has_good_credit:
#     down_payment = price * 10 /100
# else:
#   down_payment = price * 20 /100

# print(f"Down Payment: ${down_payment}")
# print("Thank You!")

#----------------------Logical Operators--------------------------
#---------AND OPERATOR-----------
# has_high_income = False
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print("Eligible for Loan")

# #---------OR OPERATOR-----------
# has_high_income = False
# has_good_credit = True

# if has_high_income or has_good_credit:
#     print("Eligible for Loan")

# #---------NOT OPERATOR-----------
# has_good_credit = True
# has_criminal_record = True

# if has_good_credit and not has_criminal_record :
#     print("Eligible for Loan")


# #----------------------Comparison Operator---------------------------------
# temp = int(input("Enter Temperaturein celcius: "))

# if temp > 30:
#     print("It's a hot day")
# elif temp < 10:
#     print("It's a cold day")
# else:
#     print("Neither hot nor cold")
# print("Thank You!")


# name = input("Enter your name: ")
# length = len(name)

# if length < 3:
#     print("Name must be atleast 3 characters")
# elif length > 50:
#     print("Name can't be maximum of 50 characters")
# else:
#     print("Name looks good!")

