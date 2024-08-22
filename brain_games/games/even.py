import random


def is_even(n):
    remain = n % 2
    return remain == 0


def get_round_params_even():
    numbe_for_qustion = random.randint(1, 100)
    return (str(numbe_for_qustion),
            "yes" if is_even(numbe_for_qustion) else "no")
