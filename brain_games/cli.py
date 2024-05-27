import prompt


def question_and_cheer():
    name = prompt.string('May I have your name?')
    print(f"Hello, {name}!")
    return name
