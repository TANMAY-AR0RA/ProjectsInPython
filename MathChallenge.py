import random
import time

MIN_OPERAND = 2
MAX_OPERAND = 13
OPERATORS = ['+','-','*']
QUESTIONS = 10

def problemGenerator():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    expr = str(left) + " " + random.choice(OPERATORS) + " "+ str(right)
    answer = eval(expr)
    return expr,answer

print("Press enter to start the Quiz")
input("Waiting...")
start_time = time.time()

for q in range(QUESTIONS):
    expr,answer=problemGenerator()
    print("Question #",q+1,": ",expr)
    while True:
        guess = input("Type answer: ")
        if guess == str(answer):
            break
end_time = time.time()
time_to_solve = end_time-start_time
print("Quiz finished!")
print("Your total time to solve was:",round(time_to_solve,2))