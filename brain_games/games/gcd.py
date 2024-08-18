import random


def get_gcd(arg_a, arg_b):
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

    query_string = f"{str(arg_a)} {str(arg_b)}"
    return (query_string, remains_rull)


def get_res_gcd():
    arg_a = random.randint(1, 100)
    arg_b = random.randint(1, 100)
    return get_gcd(arg_a, arg_b)
