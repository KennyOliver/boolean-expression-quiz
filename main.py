from VividHues import Clr
import random
#====================
first_val = random.choice([True,False])
second_val = random.choice([True,False])
operators = ["AND","OR","XOR","NOT"]
rand_operator = random.choice(operators)

print(first_val,rand_operator,second_val)
if rand_operator == "AND":
  actual_result = first_val and second_val
elif rand_operator == "OR":
  actual_result = first_val or second_val
elif rand_operator == "XOR":
  actual_result = first_val ^ second_val
elif rand_operator == "NOT":
  actual_result = not second_val

user_answer = input("Enter your answer\n\t--> ")

if user_answer == str(actual_result):
  print("YAY")
else:
  print("NO")