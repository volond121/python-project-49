import prompt

def question_and_cheer() -> str:
        name = prompt.string('May I have your name?')
        return "Hello, " + name + "!"

