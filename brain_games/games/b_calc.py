import random
from brain_games.games_fun import answer_user


def calc_resoults(sign, arg_a, arg_b):
    match sign:
        case '+':
            result = arg_a + arg_b
            str_qust = str(arg_a) + " + " + str(arg_b)
        case '-':
            result = arg_a - arg_b
            str_qust = str(arg_a) + " - " + str(arg_b)
        case '*':
            result = arg_a * arg_b
            str_qust = str(arg_a) + " * " + str(arg_b)
    return (str_qust, result)

def games_calc(rounds):
    for i in range(rounds):
        arg_a = random.randint(1, 100)
        arg_b = random.randint(1, 100)
        math_action = random.choice(['+', '-', '*'])
        (str_qust, result) = calc_resoults(math_action, arg_a, arg_b)
        answer = answer_user(str_qust, result, 'int_arg')
        if not (answer):
            return False

    return True
