import random
import prompt


def games_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        nambe_for_qustion = random.randint(1, 100)
        remain = nambe_for_qustion % 2
        print(f"Question:{nambe_for_qustion}")
        answer = prompt.string("Your answer:").lower()
        if (remain == 0):
            if (answer != "yes"):
                print(f"'{answer}' is wrong answer ;(."
                      " Correct answer wos 'yes'")
                return "wrong"
            else:
                print("Correct!")
        elif (remain == 1):
            if (answer != "no"):
                print(f"'{answer}' is wrong answer ;(. Correct answer wos 'no'")
                return "wrong"
            else:
                print("Correct!")

    return "no_wrong"
