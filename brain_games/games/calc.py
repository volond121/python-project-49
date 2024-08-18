import random


def calc_results(sign, arg_a, arg_b):
    match sign:
        case '+':
            result = arg_a + arg_b
            answer = f"{str(arg_a)} + {str(arg_b)}"
        case '-':
            result = arg_a - arg_b
            answer = f"{str(arg_a)} - {str(arg_b)}"
        case '*':
            result = arg_a * arg_b
            answer = f"{str(arg_a)} * {str(arg_b)}"
    return (answer, result)


def get_res_calc():
    arg_a = random.randint(1, 100)
    arg_b = random.randint(1, 100)
    math_action = random.choice(['+', '-', '*'])
    return calc_results(math_action, arg_a, arg_b)
