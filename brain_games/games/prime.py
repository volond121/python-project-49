import random


def is_calc_results_prime(rand_number):
    is_true = True
    if rand_number == 4:
        is_true = False
    else:
        for i in range(2, rand_number // 2):
            if ((rand_number % i) == 0):
                is_true = False
                break
    return is_true


def get_res_prime():
    rand_number = random.randint(2, 200)
    return (str(rand_number),
            "yes" if is_calc_results_prime(rand_number) else "no")
