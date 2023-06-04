import time
from datetime import date

today = date.today()

user_input = input("enter date of birth, format yyyy-mm-dd")
user_date = date.fromisoformat(user_input)

if today.month >= user_date.month:
    print(f"Your age is: {today.year - user_date.year}")
else:
    print(f"Your age is: {today.year - 1 - user_date.year}")
