import random
from brain_games.cli import answer_user


def games_calc():
    print("What is the result of the expression?")
    for i in range(3):
        arg_a = random.randint(1, 100)
        arg_b = random.randint(1, 100)
        math_action = random.choice(['+', '-', '*'])
        match math_action:
            case '+':
                result = arg_a + arg_b
                str_qust = str(arg_a) + " + " + str(arg_b)
                answer = answer_user(str_qust, result, 'int_arg')
            case '-':
                result = arg_a - arg_b
                str_qust = str(arg_a) + " - " + str(arg_b)
                answer = answer_user(str_qust, result, 'int_arg')
            case '*':
                result = arg_a * arg_b
                str_qust = str(arg_a) + " * " + str(arg_b)
                answer = answer_user(str_qust, result, 'int_arg')
        if not(answer):
            return False
    
    return True