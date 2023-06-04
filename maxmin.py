import re

user_input = input("please enter a list of integers, this will return the highest and lowest")

user_list = re.split(',| ', user_input)

user_list.sort()

lowest_highest = [user_list[0], user_list[-1]]
print(f"Your lowest and highest numbers are {lowest_highest}")