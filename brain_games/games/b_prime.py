import random
from brain_games.cli import answer_user


def games_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        rand_number = random.randint(2, 200)
        asc_rull = "yes"
        if rand_number == 4:
            asc_rull = 'no'
        else:
            for i in range(2, rand_number // 2):
                if ((rand_number % i) == 0):
                    asc_rull = 'no'
                    break
        answer = answer_user(str(rand_number), asc_rull, 'int_arg')
        if not (answer):
            return False

    return True
