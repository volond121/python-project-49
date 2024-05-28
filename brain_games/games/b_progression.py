import random
from brain_games.cli import answer_user


def games_progression():
    print("What number is missing in the progression?")
    for i in range(3):
        start_arg = random.randint(1, 100)
        long_str = random.randint(5, 10)
        step_str = random.randint(2, 10)
        find_number = random.randint(0, long_str - 1)
        str_qwes = ''
        for i in range(long_str):
            calc_next_num = start_arg + i * step_str
            if i == find_number:
                brain_numb = calc_next_num
                str_qwes = str_qwes + '.. '
            else:
                str_qwes = str_qwes + str(calc_next_num) + ' '
        answer = answer_user(str_qwes, brain_numb, 'int_arg')
        if not (answer):
            return False

    return True
