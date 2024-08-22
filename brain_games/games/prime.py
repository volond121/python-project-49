import random


def is_calc_results_prime(n):
    if n == 4:
        return False
    for i in range(2, n // 2):
        if ((n % i) == 0):
            return False
    return True


def get_round_params_prime():
    rand_number = random.randint(2, 200)
    return (str(rand_number),
            "yes" if is_calc_results_prime(rand_number) else "no")
