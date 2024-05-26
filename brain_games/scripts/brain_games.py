#!/usr/bin/env python3

from brain_games.cli import question_and_cheer
import brain_games.scripts.brain_even as brain_even


def main():
    print('Welcome to the Brain Games!')
    name_user = question_and_cheer()
    brain_even.main(name_user)


if __name__ == '__main__':
    main()
