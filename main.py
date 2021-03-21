from VividHues import Clr
import random
#====================
first_val = random.choice([False,True])
second_val = random.choice([False,True])
operators = ["AND","OR","XOR","NOT"]
rand_operator = random.choice(operators)
all_not = random.choice([False,True])

if rand_operator == "AND":
  question = f"{Clr.YELLOW}{first_val} {Clr.PINK}{rand_operator} {Clr.YELLOW}{second_val}{Clr.RESET}"
  actual_result = first_val and second_val
elif rand_operator == "OR":
  question = f"{Clr.YELLOW}{first_val} {Clr.PINK}{rand_operator} {Clr.YELLOW}{second_val}{Clr.RESET}"
  actual_result = first_val or second_val
elif rand_operator == "XOR":
  question = f"{Clr.YELLOW}{first_val} {Clr.PINK}{rand_operator} {Clr.YELLOW}{second_val}{Clr.RESET}"
  actual_result = first_val ^ second_val
elif rand_operator == "NOT":
  question = f"{Clr.PINK}{rand_operator} {Clr.YELLOW}{first_val}{Clr.RESET}"
  actual_result = not first_val

if all_not is True:
  actual_result = not actual_result
  question = f"{Clr.PINK}NOT ({question}{Clr.PINK}){Clr.RESET}"

print(question)
user_answer = input(f"{Clr.LIME}Enter your answer\n\t--> {Clr.RESET}").title()

if user_answer == str(actual_result):
  print(f"{Clr.BOLD + Clr.GREEN}Correct!{Clr.RESET}")
else:
  print(f"{Clr.BOLD + Clr.RED}Incorrect!{Clr.RESET}")
  print(f"{Clr.RED}The answer was: {actual_result}{Clr.RESET}")