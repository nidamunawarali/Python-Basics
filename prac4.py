#-----------------------MODULES-----------------------------
#1st method
# import converter

# print(converter.kgs_to_lbs(70))

#2nd Method
# from converter import lbs_to_kgs 
# from converter import kgs_to_lbs
# print(lbs_to_kgs(160))
# print(kgs_to_lbs(70))

# from utils import find_max
# numbers = [12, 13, 15, 17, 8]
# result = find_max(numbers)
# print(f"Maximum number is: {result}")


#------------PACKAGES-----------------------------------
#------------- 1st Approach -------------
# import mypackage.shipping
# mypackage.shipping.calc_shipping()

#-------------- 2nd Approach ----------------

# from mypackage.shipping import calc_shipping
# calc_shipping()

#but when we have one or more functions then 
# from mypackage.shipping import calc_shipping, print_shipping
# calc_shipping()
# print_shipping()
 # -------OR-------

# from mypackage import shipping
# shipping.calc_shipping()
# shipping.print_shipping()


#----------------- GENERATING RANDOM VALUES -----------------
# import random

# for i in range(3):
#     print(random.random())

# for i in range(3):
#     print(random.randint(10, 20))

# members = [ "Nida", "Rija", "Hiba", "Mohsin", "Hamza", "Zoya", "Zara", "Irha"]
# leader = random.choice(members)
# print(leader)

# class Dice:
#     def roll(self):
#         first = random.randint(1, 8)
#         second = random.randint(1, 8)
#         return first, second

# d1 = Dice()
# print(d1.roll())


#-------------------- WORKING WITH DIRECTORIES -------------------------

# from pathlib import Path

# path = Path("mypackage")
# print(path.exists())

# path = Path("emails")
# #print(path.mkdir())   # make directory
# print(path.rmdir())   # remove directory

# path = Path()
# for file in path.glob("*.py"):     #print all .py file
#     print(file)


# path = Path()
# for file in path.glob("*"):     #print all directories and .py files
#     print(file)