import random


def calc_results_prime(rand_number):
    is_true = "yes"
    if rand_number == 4:
        is_true = 'no'
    else:
        for i in range(2, rand_number // 2):
            if ((rand_number % i) == 0):
                is_true = 'no'
                break
    return is_true


def gat_res_prime():
    rand_number = random.randint(2, 200)
    return (str(rand_number), calc_results_prime(rand_number))
