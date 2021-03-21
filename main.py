from VividHues import Clr
import random
#====================
first_val = random.choice([True,False])
second_val = random.choice([True,False])
operators = ["AND","OR","XOR","NOT"]
rand_operator = random.choice(operators)

if rand_operator == "AND":
  print(first_val,rand_operator,second_val)
  actual_result = first_val and second_val
elif rand_operator == "OR":
  print(first_val,rand_operator,second_val)
  actual_result = first_val or second_val
elif rand_operator == "XOR":
  print(first_val,rand_operator,second_val)
  actual_result = first_val ^ second_val
elif rand_operator == "NOT":
  print(rand_operator,first_val)
  actual_result = not first_val

user_answer = input("Enter your answer\n\t--> ").title()

if user_answer == str(actual_result):
  print("Correct!")
else:
  print("Incorrect")
  print(f"The answer was: {actual_result}")