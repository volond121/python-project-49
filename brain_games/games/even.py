import random


def colc_result_even(nambe_for_qustion):
    remain = nambe_for_qustion % 2
    if (remain == 0):
        is_true = "yes"
    else:
        is_true = "no"
    return is_true


def gat_res_even():
    nambe_for_qustion = random.randint(1, 100)
    return (str(nambe_for_qustion), colc_result_even(nambe_for_qustion))
