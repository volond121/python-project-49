import random


def calc_result_progress(start_arg, long_str, step_str, find_number):
    query_string = list(range(start_arg, start_arg + long_str * step_str,
                              step_str))
    right_answer = query_string[find_number]
    query_string[find_number] = '..'
    generated_query_string = ' '.join(str(el) for el in query_string)
    return (generated_query_string, right_answer)


def gat_res_progression():
    start_arg = random.randint(1, 100)
    long_str = random.randint(5, 10)
    step_str = random.randint(2, 10)
    find_number = random.randint(0, long_str - 1)
    (generated_query_string, right_answer) = calc_result_progress(start_arg,
                                                                  long_str,
                                                                  step_str,
                                                                  find_number)
    return (generated_query_string, right_answer)
