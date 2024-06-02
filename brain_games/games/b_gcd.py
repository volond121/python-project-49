import random
from brain_games.games_fun import answer_user


def colc_resoults_gcd(arg_a, arg_b):
    if arg_a < arg_b:
        find_a = arg_b
        find_b = arg_a
    else:
        find_a = arg_a
        find_b = arg_b

    remains = find_a % find_b
    remains_rull = find_b
    divisible = find_b
    divider = remains
    while remains != 0:
        remains = divisible % divider
        remains_rull = divider
        divisible = divider
        divider = remains

    str_qust = str(arg_a) + " " + str(arg_b)
    return (str_qust, remains_rull)

def games_gcd(rounds):
    for i in range(rounds):
        arg_a = random.randint(1, 100)
        arg_b = random.randint(1, 100)
        (str_qust, remains_rull) = colc_resoults_gcd(arg_a, arg_b)
        answer = answer_user(str_qust, remains_rull, 'int_arg')
        if not (answer):
            return False

    return True
