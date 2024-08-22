import random


def apply_operator(sign, arg_a, arg_b):
    match sign:
        case '+':
            result = arg_a + arg_b
        case '-':
            result = arg_a - arg_b
        case '*':
            result = arg_a * arg_b
    return result


def get_round_params_calc():
    arg_a = random.randint(1, 100)
    arg_b = random.randint(1, 100)
    math_action = random.choice(['+', '-', '*'])
    answer = f"{str(arg_a)} {math_action} {str(arg_b)}"
    return (answer, apply_operator(math_action, arg_a, arg_b))
