import random


def is_calc_result_even(numbe_for_qustion):
    remain = numbe_for_qustion % 2
    return remain == 0


def get_res_even():
    numbe_for_qustion = random.randint(1, 100)
    return (str(numbe_for_qustion),
            "yes" if is_calc_result_even(numbe_for_qustion) else "no")
