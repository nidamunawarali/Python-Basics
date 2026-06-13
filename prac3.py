#-----------------------------------FUNCTIONS---------------------------------------------

# def greeting():
#     print("Hello 👋")
#     print("Welcome here")


# print("Start")
# greeting()
# print("Finish")


#-----------PARAMETERS---------------
# def greeting(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome here")


# print("Start")
# greeting("John", "Smith")   #this is positional argument
# greeting(first_name = "John", last_name = "Smith")   # this is keyword Argument
# greeting("John", last_name = "Smith")    # this is the combination of positional and keyword argume
# # but in case we keep keyword argument first and then positional argument is gives error
# #greeting(first_name ="John","Smith")  # see there is error because pythin doesn't like it
# greeting("Marry", "William")
# print("Finish")

#--------------return statement----------
# def square(number):
#     return number * number


# # result = square(2)
# # print(result)

# print(square(3))

#-------------creating a reusable function---------------

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😊",
#         ":(": "😞"
#     }
#     output = ''
#     for word in words:
#         output+= emojis.get(word, word) + " "
#     return output

# message = input(">")
# print(emoji_converter(message))



#------------------Exceptions------------------

# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
#     print(risk)
# except ZeroDivisionError:
#     print("Age cannot be zero")
# except ValueError:
#     print("Invalid Value")


#----------------------------CLASSES-----------------------------------

# class Point:
#     def move(self):
#         print("Move")
    
#     def draw(self):
#         print("Draw")

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)
# point2.move()


#-----------------CONSTRUCTOR-------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("MOVE")

#     def draw(self):
#         print("DRAW")

# point1 = Point(10, 20)
# point1.x = 11
# print(point1.x)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hi, i am {self.name}")

# p1 = Person("Nida")
# print(p1.name)
# p1.talk()

# p2 = Person("Zara")
# p2.talk()


#--------------------------------INHERITANCE-------------------------------------

# class Mammal:
#     def walk(self):
#         print("Wak")

# class Cat(Mammal):
#     pass               # pass means this class doesn't have additional methods just pass it 

# class Dog(Mammal):
#     def bark(self):
#         print("Dog bark")

# d1 = Dog()
# d1.walk()
# d1.bark()

# c1 = Cat()
# c1.walk()