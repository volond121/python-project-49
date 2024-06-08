#!/usr/bin/env python3

from brain_games.cli import welcome_user
import brain_games.game_engine as game_engine


def main():
    name_user = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_engine.play_game('prime', name_user)


if __name__ == '__main__':
    main()
