import random
from brain_games.games_fun import answer_user


def calc_resoults_prime(rand_number):
    asc_rull = "yes"
    if rand_number == 4:
        asc_rull = 'no'
    else:
        for i in range(2, rand_number // 2):
            if ((rand_number % i) == 0):
                asc_rull = 'no'
                break
    return asc_rull


def games_prime(rounds):
    for i in range(rounds):
        rand_number = random.randint(2, 200)
        answer = answer_user(str(rand_number),
                             calc_resoults_prime(rand_number), 'int_arg')
        if not (answer):
            return False

    return True
