import random
from brain_games.games_fun import answer_user

def calc_resoult_progress(start_arg, long_str, step_str, find_number):
    str_form = list(range(start_arg, start_arg + long_str * step_str, step_str))
    str_form[find_number] = '..'
    str_qwes = ' '.join(str(el) for el in str_form)
    brain_numb = str(start_arg + find_number * step_str)
    return (str_qwes, brain_numb)

def games_progression(rounds):
    for i in range(rounds):
        start_arg = random.randint(1, 100)
        long_str = random.randint(5, 10)
        step_str = random.randint(2, 10)
        find_number = random.randint(0, long_str - 1)
        (str_qwes, brain_numb) = calc_resoult_progress(start_arg, long_str, step_str, find_number)
        answer = answer_user(str_qwes, brain_numb, 'int_arg')
        if not (answer):
            return False

    return True
