import random


def get_progression(start, length, step):
    return list(range(start, start + length * step, step))


def get_res_progression():
    start = random.randint(1, 100)
    length = random.randint(5, 10)
    step = random.randint(2, 10)
    random_index = random.randint(0, length - 1)
    progression = get_progression(start, length, step)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    generated_query_string = ' '.join(str(el) for el in progression)
    return (generated_query_string, right_answer)
